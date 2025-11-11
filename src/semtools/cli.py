import asyncio
import os
import sys
from pathlib import Path

import click

from .parse import LlamaParseBackend, LlamaParseConfig
from .search import Searcher
from .workspace import Store, Workspace
from .workspace.store import DocMeta, LineEmbedding


@click.command(help="A CLI tool for parsing documents using various backends")
@click.option(
    "-c",
    "--parse-config",
    "config_path",
    type=click.Path(),
    default=str(Path.home() / ".parse_config.json"),
    help="Path to the config file. Defaults to ~/.parse_config.json",
)
@click.option(
    "-b",
    "--backend",
    default="llama-parse",
    help="The backend type to use for parsing. Defaults to `llama-parse`",
)
@click.option("-v", "--verbose", is_flag=True, help="Verbose output while parsing")
@click.argument("files", nargs=-1, type=click.Path(exists=True), required=True)
def parse(config_path, backend, verbose, files):
    if backend != "llama-parse":
        click.echo(f"Error: Unknown backend '{backend}'. Supported backends: llama-parse", err=True)
        sys.exit(1)

    config = LlamaParseConfig.from_config_file(Path(config_path))
    parser = LlamaParseBackend(config, verbose=verbose)

    results = asyncio.run(parser.parse(list(files)))

    for result_path in results:
        click.echo(result_path)


def _run_workspace_search(query, files, n_lines, top_k, max_distance, ignore_case):
    """Handles the search logic when a workspace is active."""
    ws = Workspace.open()
    store = Store(ws.config.root_dir)
    searcher = Searcher()

    # 1. Analyze document states
    existing_docs = store.get_existing_docs(files)
    docs_to_upsert = []
    lines_to_upsert = []

    for file_path in files:
        try:
            stat = os.stat(file_path)
            current_meta = DocMeta(
                path=file_path, size_bytes=stat.st_size, mtime=int(stat.st_mtime)
            )
        except FileNotFoundError:
            continue

        existing_meta = existing_docs.get(file_path)
        if not existing_meta or existing_meta.mtime != current_meta.mtime or existing_meta.size_bytes != current_meta.size_bytes:
            # Document is new or has changed
            with open(file_path, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\n") for line in f.readlines()]

            if not lines:
                continue

            lines_for_embedding = [line.lower() for line in lines] if ignore_case else lines
            embeddings = searcher.model.encode(lines_for_embedding)

            for i, emb in enumerate(embeddings):
                lines_to_upsert.append(
                    LineEmbedding(path=file_path, line_number=i, embedding=emb.tolist())
                )
            docs_to_upsert.append(current_meta)

    # 2. Update workspace if necessary
    if lines_to_upsert:
        store.upsert_line_embeddings(lines_to_upsert)
    if docs_to_upsert:
        store.upsert_document_metadata(docs_to_upsert)

    # 3. Search the workspace
    processed_query = query.lower() if ignore_case else query
    query_embedding = searcher.model.encode([processed_query])[0]
    ranked_lines = store.search_line_embeddings(
        query_embedding.tolist(), files, top_k, max_distance
    )

    # 4. Print results
    is_tty = sys.stdout.isatty()
    for ranked_line in ranked_lines:
        start = max(0, ranked_line.line_number - n_lines)
        click.echo(f"{ranked_line.path}:{start}::{ranked_line.line_number + n_lines + 1} ({ranked_line.distance:.4f})")
        
        try:
            with open(ranked_line.path, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\n") for line in f.readlines()]
            
            end = min(len(lines), ranked_line.line_number + n_lines + 1)
            context_lines = lines[start:end]

            for i, line in enumerate(context_lines):
                line_num = start + i
                if line_num == ranked_line.line_number:
                    if is_tty:
                        # Use click.style for robust highlighting
                        styled_line = click.style(f"{line_num + 1:4}: {line}", bg="yellow", fg="black")
                        click.echo(styled_line)
                    else:
                        click.echo(f"{line_num + 1:4}: {line}")
                else:
                    click.echo(f"{line_num + 1:4}: {line}")
            click.echo() # Newline between results
        except (IOError, UnicodeDecodeError):
            click.echo("    [Error: Could not read file content]")
            click.echo()


@click.command(help="A CLI tool for fast semantic keyword search")
@click.argument("query")
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option(
    "-n", "--n-lines", default=3, help="How many lines before/after to return as context"
)
@click.option(
    "--top-k", default=3, help="The top-k files or texts to return (ignored if max_distance is set)"
)
@click.option(
    "-m", "--max-distance", type=float, help="Return all results with distance below this threshold (0.0+)"
)
@click.option(
    "-i", "--ignore-case", is_flag=True, help="Perform case-insensitive search (default is false)"
)
def search(query, files, n_lines, top_k, max_distance, ignore_case):
    files = list(files)
    
    # Check for active workspace
    if os.getenv("SEMTOOLS_WORKSPACE") and files:
        _run_workspace_search(query, files, n_lines, top_k, max_distance, ignore_case)
        return
    
    # Standard in-memory search
    searcher = Searcher()
    results = searcher.search(
        query, files, n_lines, top_k, max_distance, ignore_case
    )

    is_tty = sys.stdout.isatty()
    for res in results:
        end = res.context_start_line + len(res.context_lines)
        click.echo(f"{res.file_path}:{res.context_start_line}::{end} ({res.distance:.4f})")
        
        for i, line in enumerate(res.context_lines):
            line_num = res.context_start_line + i
            if line_num == res.match_line_index:
                if is_tty:
                    # Use click.style for robust highlighting
                    styled_line = click.style(f"{line_num + 1:4}: {line}", bg="yellow", fg="black")
                    click.echo(styled_line)
                else:
                    click.echo(f"{line_num + 1:4}: {line}")
            else:
                click.echo(f"{line_num + 1:4}: {line}")
        click.echo() # Newline between results


@click.group(help="Manage semtools workspaces")
def workspace():
    pass


@workspace.command("use", help="Use or create a workspace (prints export command to run)")
@click.argument("name")
def use_workspace(name):
    try:
        root_dir = Workspace._get_root_path(name)
        config = Workspace(config=WorkspaceConfig(name=name, root_dir=str(root_dir)))
        config.save()
        click.echo(f"Workspace '{name}' configured.")
        click.echo("To activate it, run:")
        click.echo(f"  export SEMTOOLS_WORKSPACE={name}")
        click.echo()
        click.echo("Or add this to your shell profile (.bashrc, .zshrc, etc.)")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@workspace.command("status", help="Show active workspace and basic stats")
def status_workspace():
    try:
        ws = Workspace.open()
        click.echo(f"Active workspace: {ws.config.name}")
        click.echo(f"Root: {ws.config.root_dir}")

        store = Store(ws.config.root_dir)
        stats = store.get_stats()

        click.echo(f"Documents: {stats.total_documents}")
        if stats.has_index:
            index_info = stats.index_type or "Unknown"
            click.echo(f"Index: Yes ({index_info})")
        else:
            click.echo("Index: No")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@workspace.command("prune", help="Remove stale or missing files from store")
def prune_workspace():
    try:
        ws = Workspace.open()
        store = Store(ws.config.root_dir)
        
        all_paths = store.get_all_document_paths()
        missing_paths = [p for p in all_paths if not os.path.exists(p)]

        if not missing_paths:
            click.echo("No stale documents found. Workspace is clean.")
            return

        click.echo(f"Found {len(missing_paths)} stale documents:")
        for path in missing_paths:
            click.echo(f"  - {path}")

        store.delete_documents(missing_paths)
        click.echo(f"Removed {len(missing_paths)} stale documents from workspace.")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)