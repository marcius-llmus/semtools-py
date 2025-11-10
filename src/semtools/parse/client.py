import asyncio
import time
from pathlib import Path
from typing import Any, Dict

import httpx

from .config import LlamaParseConfig
from .errors import ParseHttpError, ParseRetryExhaustedError, ParseTimeoutError


class ParseClient:
    """A client for interacting with the LlamaParse API."""

    def __init__(self, config: LlamaParseConfig, verbose: bool = False):
        self.config = config
        self.verbose = verbose

    async def create_parse_job(
        self, client: httpx.AsyncClient, file_path: str
    ) -> str:
        """Creates a parse job for a single file."""
        url = f"{self.config.base_url}/api/parsing/upload"
        headers = {"Authorization": f"Bearer {self.config.api_key}"}

        with open(file_path, "rb") as f:
            files = {"file": (Path(file_path).name, f.read())}
            response = await client.post(
                url, headers=headers, files=files, data=self.config.parse_kwargs
            )

        if not response.is_success:
            raise ParseHttpError(
                f"Upload failed with status {response.status_code}: {response.text}"
            )

        return response.json()["id"]

    async def get_job_result(
        self, client: httpx.AsyncClient, job_id: str
    ) -> str:
        """Polls for the result of a parsing job until completion or timeout."""
        start_time = time.monotonic()
        status_url = f"{self.config.base_url}/api/parsing/job/{job_id}"
        result_url = f"{status_url}/result/markdown"
        headers = {"Authorization": f"Bearer {self.config.api_key}"}

        while True:
            if time.monotonic() - start_time > self.config.max_timeout:
                raise ParseTimeoutError(f"Job {job_id} timed out.")

            await asyncio.sleep(self.config.check_interval)

            try:
                status_response = await client.get(status_url, headers=headers)
                status_response.raise_for_status()
                status = status_response.json()["status"]

                if status == "SUCCESS":
                    result_response = await client.get(result_url, headers=headers)
                    result_response.raise_for_status()
                    return result_response.json()["markdown"]
                elif status in ["ERROR", "CANCELED"]:
                    raise ParseHttpError(f"Job {job_id} failed with status: {status}")
                elif status == "PENDING":
                    continue

            except httpx.HTTPStatusError as e:
                # Continue polling on server errors, fail on client errors
                if 500 <= e.response.status_code < 600:
                    if self.verbose:
                        print(
                            f"Server error while polling job {job_id}, retrying..."
                        )
                    continue
                raise ParseHttpError(f"HTTP error while polling job {job_id}: {e}")

    async def _execute_with_retry(self, coro: Any) -> Any:
        """Executes a coroutine with retry logic."""
        last_exception = None
        for attempt in range(self.config.max_retries + 1):
            try:
                return await coro
            except (httpx.ConnectError, httpx.TimeoutException, httpx.HTTPStatusError) as e:
                is_server_error = (
                    isinstance(e, httpx.HTTPStatusError)
                    and 500 <= e.response.status_code < 600
                )
                if not (isinstance(e, (httpx.ConnectError, httpx.TimeoutException)) or is_server_error):
                    raise ParseHttpError(str(e)) from e

                last_exception = e
                if attempt == self.config.max_retries:
                    break

                delay = (
                    self.config.retry_delay_ms
                    / 1000.0
                    * (self.config.backoff_multiplier**attempt)
                )
                if self.verbose:
                    print(
                        f"Request failed (attempt {attempt + 1}/{self.config.max_retries + 1}): {e}. "
                        f"Retrying in {delay:.2f}s..."
                    )
                await asyncio.sleep(delay)

        raise ParseRetryExhaustedError(
            f"Operation failed after {self.config.max_retries + 1} attempts."
        ) from last_exception

    async def create_job_with_retry(
        self, client: httpx.AsyncClient, file_path: str
    ) -> str:
        """Creates a parse job with retry logic."""
        return await self._execute_with_retry(self.create_parse_job(client, file_path))

    async def poll_for_result_with_retry(
        self, client: httpx.AsyncClient, job_id: str
    ) -> str:
        """Polls for a job result with retry logic on the polling loop itself."""
        try:
            return await self.get_job_result(client, job_id)
        except ParseHttpError as e:
            # The inner poll loop already handles retries for transient server errors.
            # This top-level error indicates a more permanent failure.
            raise e