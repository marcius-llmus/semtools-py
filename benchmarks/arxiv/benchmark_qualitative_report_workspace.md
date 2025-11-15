# Semtools Qualitative Benchmark Report

- **Mode:** `workspace`
- **Oracle:** `gemini-2.5-flash`


## Detailed Analysis per Query

### 1. Query: What is the primary purpose of the WikiMixQA benchmark?

- **Query ID:** `simple_1`
- **Query Type:** Simple
- **Curated Source Files:** `full_text/2505.07796v2.txt, full_text/2506.15594v1.txt, full_text/2506.22309v1.txt, full_text/2507.15152v1.txt, full_text/2508.14302v1.txt, full_text/2508.15370v1.txt`

#### LLM Ground Truth Answer

> The primary purpose of the WikiMixQA benchmark is to evaluate cross-modal reasoning in Vision-Language Large Models (VLLMs) over tables and charts, specifically emphasizing complex reasoning by requiring models to synthesize information from multiple modalities from long, digital-only Wikipedia documents.

**Source Document(s):** `full_text/2506.15594v1.txt`

#### `search` Tool Performance

**Command Executed:**

```bash
search "What is the primary purpose of the WikiMixQA benchmark?" full_text/*.txt --top-k 10 --n-lines 7
```

**Retrieval Precision:** `0.33`
**Retrieval Recall:** `1.00`

**Documents Returned by `search`:** `full_text/2506.15594v1.txt, full_text/2506.19037v3.txt, full_text/2507.20059v1.txt`

#### LLM Search-Augmented Answer

> The provided search results describe the composition and construction of the WikiMixQA benchmark but do not explicitly state its primary purpose. The benchmark is a dataset comprising 1000 question-answer pairs derived from 526 unique Wikipedia documents. These pairs were created through an annotation and revision process, with approximately half involving reasoning across two tables. The dataset was also validated by an AI evaluator (InternVL2-Llama3-76B model), with a focus on enhancing dataset diversity. However, the snippets do not specify the overarching goal or aim for which this benchmark was developed.

<details><summary>View Original `search` Tool Output</summary>

```
full_text/2506.15594v1.txt:105::119 (0.2430)
 105: 2.
 106: 
 107: Answer Assessment: For question-answer pairs deemed valid, annotators assessed the correctness of the provided answers, labeling each pair as “Correct”, “Wrong”, or “Small Edit”. The “Small Edit” label was used for cases where the question could be retained after minor revisions. During this step, annotators also verified that incorrect answer options were plausible and contextually grounded.
 108: 
 109: Using majority voting, 595 questions were labeled as Correct.
 110: Invalid pairs were revised for issues like overly detailed questions or multiple correct answers. Pairs labeled “Small Edit” were refined, resulting in 405 additional corrected pairs being added to the final dataset. Figure 8 shows the interface of our annotation tool.
 111: 
 112: 2.5 The WikiMixQA benchmark
 113: 
 114: Combining questions labeled as Correct with the revised questions, the final dataset comprises 1000 question-answer pairs derived from 526 unique Wikipedia documents. The distribution of question-answer pairs across topics is relatively balanced, reflecting the natural topical distribution of Wikipedia, as shown in Figure 3.
 115: 
 116: Approximately 515 of the 1000 pairs were validated as Correct by our AI evaluator (InternVL2-Llama3-76B model), underscoring the value of sampling from initially rejected questions to enhance dataset diversity. The distribution of question-answer pairs by modality type is illustrated in Figure 3. Notably, nearly half of the pairs involve reasoning across two tables. Figure 4 indicates the distribution of questions’ and answers’ lengths.
 117: 
 118: 3 Evaluation
 119: 

full_text/2506.15594v1.txt:1687::1701 (0.2430)
1687: 2.
1688: 
1689: Answer Assessment: For question-answer pairs deemed valid, annotators assessed the correctness of the provided answers, labeling each pair as “Correct”, “Wrong”, or “Small Edit”. The “Small Edit” label was used for cases where the question could be retained after minor revisions. During this step, annotators also verified that incorrect answer options were plausible and contextually grounded.
1690: 
1691: Using majority voting, 595 questions were labeled as Correct.
1692: Invalid pairs were revised for issues like overly detailed questions or multiple correct answers. Pairs labeled “Small Edit” were refined, resulting in 405 additional corrected pairs being added to the final dataset. Figure 8 shows the interface of our annotation tool.
1693: 
1694: 2.5 The WikiMixQA benchmark
1695: 
1696: Combining questions labeled as Correct with the revised questions, the final dataset comprises 1000 question-answer pairs derived from 526 unique Wikipedia documents. The distribution of question-answer pairs across topics is relatively balanced, reflecting the natural topical distribution of Wikipedia, as shown in Figure 3.
1697: 
1698: Approximately 515 of the 1000 pairs were validated as Correct by our AI evaluator (InternVL2-Llama3-76B model), underscoring the value of sampling from initially rejected questions to enhance dataset diversity. The distribution of question-answer pairs by modality type is illustrated in Figure 3. Notably, nearly half of the pairs involve reasoning across two tables. Figure 4 indicates the distribution of questions’ and answers’ lengths.
1699: 
1700: 2 DATASET CONSTRUCTION
1701: 

full_text/2506.15594v1.txt:1829::1843 (0.2430)
1829: Answer Assessment: For question-answer pairs deemed valid, annotators assessed the correctness of the provided answers, labeling each pair as “Correct”, “Wrong”, or “Small Edit”. The “Small Edit” label was used for cases where the question could be retained after minor revisions. During this step, annotators also verified that incorrect answer options were plausible and contextually grounded.
1830: 
1831: Answer Assessment: For question-answer pairs deemed valid, annotators assessed the correctness of the provided answers, labeling each pair as “Correct”, “Wrong”, or “Small Edit”. The “Small Edit” label was used for cases where the question could be retained after minor revisions. During this step, annotators also verified that incorrect answer options were plausible and contextually grounded.
1832: 
1833: Using majority voting, 595 questions were labeled as Correct.
1834: Invalid pairs were revised for issues like overly detailed questions or multiple correct answers. Pairs labeled “Small Edit” were refined, resulting in 405 additional corrected pairs being added to the final dataset. Figure 8 shows the interface of our annotation tool.
1835: 
1836: 2.5 The WikiMixQA benchmark
1837: 
1838: Combining questions labeled as Correct with the revised questions, the final dataset comprises 1000 question-answer pairs derived from 526 unique Wikipedia documents. The distribution of question-answer pairs across topics is relatively balanced, reflecting the natural topical distribution of Wikipedia, as shown in Figure 3.
1839: 
1840: Approximately 515 of the 1000 pairs were validated as Correct by our AI evaluator (InternVL2-Llama3-76B model), underscoring the value of sampling from initially rejected questions to enhance dataset diversity. The distribution of question-answer pairs by modality type is illustrated in Figure 3. Notably, nearly half of the pairs involve reasoning across two tables. Figure 4 indicates the distribution of questions’ and answers’ lengths.
1841: 
1842: 2.5 THE WIKIMIXQA BENCHMARK
1843: 

full_text/2506.19037v3.txt:852::866 (0.3053)
 852: 
 853: Wang et al. (2024)
 854: 
 855: Wang, Y.; Ma, X.; Zhang, G.; Ni, Y.; Chandra, A.; Guo, S.; Ren, W.; Arulraj,
 856: A.; He, X.; Jiang, Z.; et al. 2024.
 857: 
 858: Mmlu-pro: A more robust and challenging multi-task language
 859: understanding benchmark.
 860: 
 861: In The Thirty-eight Conference on Neural Information Processing
 862: Systems Datasets and Benchmarks Track.
 863: 
 864: Xia et al. (2022)
 865: 
 866: Xia, H.; Ge, T.; Wang, P.; Chen, S.-Q.; Wei, F.; and Sui, Z. 2022.

full_text/2506.19037v3.txt:2978::2992 (0.3053)
2978: 
2979: Wang et al. (2024)
2980: 
2981: Wang, Y.; Ma, X.; Zhang, G.; Ni, Y.; Chandra, A.; Guo, S.; Ren, W.; Arulraj,
2982: A.; He, X.; Jiang, Z.; et al. 2024.
2983: 
2984: Mmlu-pro: A more robust and challenging multi-task language
2985: understanding benchmark.
2986: 
2987: In The Thirty-eight Conference on Neural Information Processing
2988: Systems Datasets and Benchmarks Track.
2989: 
2990: Xia et al. (2022)
2991: 
2992: Xia, H.; Ge, T.; Wang, P.; Chen, S.-Q.; Wei, F.; and Sui, Z. 2022.

full_text/2507.20059v1.txt:282::296 (0.3064)
 282: As shown in Figure 3, reranking yields only marginal gains across datasets. This suggests that improving retrieval quality through reranking is insufficient in mixture-of-knowledge scenarios. The retriever’s limited capacity and restricted access to relevant knowledge highlight the need for deeper integration between knowledge sources, retrieval mechanisms, and generative models.
 283: 
 284: 2.5 RQ 4: Evaluating LLMs as Routers for Mixture-of-Knowledge Retrieval
 285: 
 286: Previous analyses highlight the need for adaptive retrieval mechanisms that dynamically route queries to the most relevant corpus based on topic context. Here, we investigate whether current LLMs can effectively perform query routing.
 287: Figure 4 evaluates LLMs from the Qwen-3 series (4B, 8B, and 32B parameters) as “routers” that select among heterogeneous knowledge sources at inference time. We compare plain prompting versus chain-of-thought prompting on the MMLU and MMLU-Pro datasets, which cover diverse general and professional domains.
 288: 
 289: Specifically, we benchmark:
 290: (1) no-retrieval baselines;
 291: (2) static retrieval from all corpora (“all sources”);
 292: (3) LLM-prompted routing variants (plain and chain-of-thought); and
 293: (4) an oracle router upper bound.
 294: Surprisingly, neither prompting strategy consistently outperforms static retrieval. In fact, both routing approaches often underperform compared to simply retrieving from all sources, and occasionally fall below no-retrieval baselines. Chain-of-thought prompting provides only marginal improvements, while scaling model size yields negligible or even negative returns.
 295: 
 296: We attribute this failure to two main factors:

full_text/2507.20059v1.txt:2593::2607 (0.3064)
2593: As shown in Figure 3, reranking yields only marginal gains across datasets. This suggests that improving retrieval quality through reranking is insufficient in mixture-of-knowledge scenarios. The retriever’s limited capacity and restricted access to relevant knowledge highlight the need for deeper integration between knowledge sources, retrieval mechanisms, and generative models.
2594: 
2595: 2.5 RQ 4: Evaluating LLMs as Routers for Mixture-of-Knowledge Retrieval
2596: 
2597: Previous analyses highlight the need for adaptive retrieval mechanisms that dynamically route queries to the most relevant corpus based on topic context. Here, we investigate whether current LLMs can effectively perform query routing.
2598: Figure 4 evaluates LLMs from the Qwen-3 series (4B, 8B, and 32B parameters) as “routers” that select among heterogeneous knowledge sources at inference time. We compare plain prompting versus chain-of-thought prompting on the MMLU and MMLU-Pro datasets, which cover diverse general and professional domains.
2599: 
2600: Specifically, we benchmark:
2601: (1) no-retrieval baselines;
2602: (2) static retrieval from all corpora (“all sources”);
2603: (3) LLM-prompted routing variants (plain and chain-of-thought); and
2604: (4) an oracle router upper bound.
2605: Surprisingly, neither prompting strategy consistently outperforms static retrieval. In fact, both routing approaches often underperform compared to simply retrieving from all sources, and occasionally fall below no-retrieval baselines. Chain-of-thought prompting provides only marginal improvements, while scaling model size yields negligible or even negative returns.
2606: 
2607: We attribute this failure to two main factors:

full_text/2507.20059v1.txt:3092::3106 (0.3064)
3092: As shown in Figure 3, reranking yields only marginal gains across datasets. This suggests that improving retrieval quality through reranking is insufficient in mixture-of-knowledge scenarios. The retriever’s limited capacity and restricted access to relevant knowledge highlight the need for deeper integration between knowledge sources, retrieval mechanisms, and generative models.
3093: 
3094: 2.5 RQ 4: Evaluating LLMs as Routers for Mixture-of-Knowledge Retrieval
3095: 
3096: Previous analyses highlight the need for adaptive retrieval mechanisms that dynamically route queries to the most relevant corpus based on topic context. Here, we investigate whether current LLMs can effectively perform query routing.
3097: Figure 4 evaluates LLMs from the Qwen-3 series (4B, 8B, and 32B parameters) as “routers” that select among heterogeneous knowledge sources at inference time. We compare plain prompting versus chain-of-thought prompting on the MMLU and MMLU-Pro datasets, which cover diverse general and professional domains.
3098: 
3099: Specifically, we benchmark:
3100: (1) no-retrieval baselines;
3101: (2) static retrieval from all corpora (“all sources”);
3102: (3) LLM-prompted routing variants (plain and chain-of-thought); and
3103: (4) an oracle router upper bound.
3104: Surprisingly, neither prompting strategy consistently outperforms static retrieval. In fact, both routing approaches often underperform compared to simply retrieving from all sources, and occasionally fall below no-retrieval baselines. Chain-of-thought prompting provides only marginal improvements, while scaling model size yields negligible or even negative returns.
3105: 
3106: We attribute this failure to two main factors:

full_text/2507.20059v1.txt:3112::3126 (0.3064)
3112: 
3113: Previous analyses highlight the need for adaptive retrieval mechanisms that dynamically route queries to the most relevant corpus based on topic context. Here, we investigate whether current LLMs can effectively perform query routing.
3114: Figure 4 evaluates LLMs from the Qwen-3 series (4B, 8B, and 32B parameters) as “routers” that select among heterogeneous knowledge sources at inference time. We compare plain prompting versus chain-of-thought prompting on the MMLU and MMLU-Pro datasets, which cover diverse general and professional domains.
3115: 
3116: Previous analyses highlight the need for adaptive retrieval mechanisms that dynamically route queries to the most relevant corpus based on topic context. Here, we investigate whether current LLMs can effectively perform query routing.
3117: Figure 4 evaluates LLMs from the Qwen-3 series (4B, 8B, and 32B parameters) as “routers” that select among heterogeneous knowledge sources at inference time. We compare plain prompting versus chain-of-thought prompting on the MMLU and MMLU-Pro datasets, which cover diverse general and professional domains.
3118: 
3119: Specifically, we benchmark:
3120: (1) no-retrieval baselines;
3121: (2) static retrieval from all corpora (“all sources”);
3122: (3) LLM-prompted routing variants (plain and chain-of-thought); and
3123: (4) an oracle router upper bound.
3124: Surprisingly, neither prompting strategy consistently outperforms static retrieval. In fact, both routing approaches often underperform compared to simply retrieving from all sources, and occasionally fall below no-retrieval baselines. Chain-of-thought prompting provides only marginal improvements, while scaling model size yields negligible or even negative returns.
3125: 
3126: Specifically, we benchmark:

full_text/2507.20059v1.txt:3119::3133 (0.3064)
3119: Specifically, we benchmark:
3120: (1) no-retrieval baselines;
3121: (2) static retrieval from all corpora (“all sources”);
3122: (3) LLM-prompted routing variants (plain and chain-of-thought); and
3123: (4) an oracle router upper bound.
3124: Surprisingly, neither prompting strategy consistently outperforms static retrieval. In fact, both routing approaches often underperform compared to simply retrieving from all sources, and occasionally fall below no-retrieval baselines. Chain-of-thought prompting provides only marginal improvements, while scaling model size yields negligible or even negative returns.
3125: 
3126: Specifically, we benchmark:
3127: (1) no-retrieval baselines;
3128: (2) static retrieval from all corpora (“all sources”);
3129: (3) LLM-prompted routing variants (plain and chain-of-thought); and
3130: (4) an oracle router upper bound.
3131: Surprisingly, neither prompting strategy consistently outperforms static retrieval. In fact, both routing approaches often underperform compared to simply retrieving from all sources, and occasionally fall below no-retrieval baselines. Chain-of-thought prompting provides only marginal improvements, while scaling model size yields negligible or even negative returns.
3132: 
3133: We attribute this failure to two main factors:


```

</details>


---

### 2. Query: How do Wang et al. define "loss potential" in the context of CPT for LLMs?

- **Query ID:** `simple_2`
- **Query Type:** Simple
- **Curated Source Files:** `full_text/2505.07796v2.txt, full_text/2506.15594v1.txt, full_text/2506.22309v1.txt, full_text/2507.15152v1.txt, full_text/2508.14302v1.txt, full_text/2508.15370v1.txt`

#### LLM Ground Truth Answer

> Wang et al. define "loss potential" as the "height" of the current model state in the annealing view of the loss surface. Quantitatively, it is defined as the ratio of the final annealed learning rate (LR) of the pre-training (PT) phase to the peak learning rate in the PT phase, capturing the potential for future loss drop via LR annealing.

**Source Document(s):** `full_text/2505.07796v2.txt`

#### `search` Tool Performance

**Command Executed:**

```bash
search "How do Wang et al. define \"loss potential\" in the context of CPT for LLMs?" full_text/*.txt --top-k 10 --n-lines 7
```

**Retrieval Precision:** `0.00`
**Retrieval Recall:** `0.00`

**Documents Returned by `search`:** `full_text/2507.11017v1.txt, full_text/2507.14204v1.txt, full_text/2507.16795v2.txt, full_text/2508.04482v1.txt`

#### LLM Search-Augmented Answer

> The provided search results do not contain a definition of "loss potential" by Wang et al. in the context of CPT for LLMs. While "Wang et al." is mentioned in relation to approximate attention mechanisms and dynamic KV cache eviction methods (Wang et al., 2020; Wang et al., 2024), these mentions do not include a definition of "loss potential." Additionally, the term "CPT" is not present in the provided snippets. "Quantization loss" is mentioned in a different context regarding Post-training Quantization (PTQ) techniques like GPTQ, but it is not attributed to Wang et al. nor is it referred to as "loss potential" or linked to CPT.

<details><summary>View Original `search` Tool Output</summary>

```
full_text/2507.14204v1.txt:54::68 (0.3512)
  54: 
  55: We evaluate and validate the effectiveness of LaCache through a series of experiments and ablation studies. Results across multiple benchmarks consistently demonstrate that LaCache enhances long-range capabilities and supports continuous generation. Additionally, due to its compatibility with FlashAttention, it outperforms importance-based methods such as H2O in terms of achievable accuracy-throughput trade-offs.
  56: 
  57: Figure 1: Illustrative comparisons among (a) recency-based KV cache (Xiao et al., 2023b), (b) retrieval-based KV cache (Tang et al., 2024), and (c) our proposed LaCache featuring a ladder-shaped pattern. Previous KV cache storage strategies struggle to simultaneously balance the needs for both continuous generation without OOM and robust long-range capabilities. In contrast, our proposed LaCache allows LLMs to simultaneously satisfy the two requirements.
  58: 
  59: 2 Related Work
  60: 
  61: Long-context LLM.
  62: The demand for long-context modeling has surged due to its ability to handle complex, multi-step tasks and maintain coherent interactions. This has spurred extensive research on enhancing long-context generation (Li et al., 2023; Peng et al., 2023; Ye et al., 2025), enabling models to process more tokens per forward pass. While approximate attention mechanisms (Beltagy et al., 2020; Kitaev et al., 2020; Wang et al., 2020) have improved efficiency, they usually lead to degradation in task accuracy. Recent advances in positional embeddings, such as position interpolation and fine-tuning (Chen et al., 2023; Peng & Quesnelle, 2023), have further extended context windows. However, inference efficiency remains a bottleneck for long input sequences. In our proposed LaCache, we leverage token eviction to enhance efficiency in long-context generation, including continuous or infinite generation tasks.
  63: 
  64: KV cache eviction.
  65: KV cache eviction techniques mitigate excessive cache growth by removing non-essential tokens. Early methods (Xiao et al., 2023b; Han et al., 2024) rely on static, naive retention strategies that overlook model processing patterns and input context, leading to accuracy degradation. To improve long-context handling, dynamic approaches (Adnan et al., 2024; Liu et al., 2024; Zhang et al., 2024; Wan et al., 2024) utilize attention weights to identify important tokens. For example, Liu et al. (2024) detects repetitive patterns to estimate token significance, while Wang et al. (2024); Shi et al. (2024); Yu et al. (2024) merge similar tokens. However, these methods depend on full attention weights, making them incompatible with state-of-the-art (SOTA) efficient inference frameworks such as FlashAttention (Dao et al., 2022), which do not explicitly compute attention maps. This constraint limits their real-device efficiency. To overcome this, LaCache introduces an attention-free KV cache eviction strategy, ensuring high accuracy while maintaining real-device efficiency.
  66: 
  67: Efficient LLM inference.
  68: While traditional efficiency techniques such as quantization, pruning, and distillation (Frantar et al., 2022; Lin et al., 2024; Fu et al., 2024b; Shi et al., 2023; Zhang et al., 2023; Yuan et al., 2025) remain valuable, system-level optimizations, such as FlashAttention (Dao et al., 2022; Dao, 2023; Shah et al., 2024) and memory offloading (Sheng et al., 2023), have emerged as key enablers for large efficiency gains in LLM inference. Unlike most dynamic KV cache eviction methods, LaCache can be seamlessly integrated with these system-level approaches, enhancing real-device efficiency with SOTA inference frameworks.

full_text/2507.14204v1.txt:1474::1488 (0.3512)
1474: 
1475: We evaluate and validate the effectiveness of LaCache through a series of experiments and ablation studies. Results across multiple benchmarks consistently demonstrate that LaCache enhances long-range capabilities and supports continuous generation. Additionally, due to its compatibility with FlashAttention, it outperforms importance-based methods such as H2O in terms of achievable accuracy-throughput trade-offs.
1476: 
1477: We evaluate and validate the effectiveness of LaCache through a series of experiments and ablation studies. Results across multiple benchmarks consistently demonstrate that LaCache enhances long-range capabilities and supports continuous generation. Additionally, due to its compatibility with FlashAttention, it outperforms importance-based methods such as H2O in terms of achievable accuracy-throughput trade-offs.
1478: 
1479: 2 Related Work
1480: 
1481: Long-context LLM.
1482: The demand for long-context modeling has surged due to its ability to handle complex, multi-step tasks and maintain coherent interactions. This has spurred extensive research on enhancing long-context generation (Li et al., 2023; Peng et al., 2023; Ye et al., 2025), enabling models to process more tokens per forward pass. While approximate attention mechanisms (Beltagy et al., 2020; Kitaev et al., 2020; Wang et al., 2020) have improved efficiency, they usually lead to degradation in task accuracy. Recent advances in positional embeddings, such as position interpolation and fine-tuning (Chen et al., 2023; Peng & Quesnelle, 2023), have further extended context windows. However, inference efficiency remains a bottleneck for long input sequences. In our proposed LaCache, we leverage token eviction to enhance efficiency in long-context generation, including continuous or infinite generation tasks.
1483: 
1484: KV cache eviction.
1485: KV cache eviction techniques mitigate excessive cache growth by removing non-essential tokens. Early methods (Xiao et al., 2023b; Han et al., 2024) rely on static, naive retention strategies that overlook model processing patterns and input context, leading to accuracy degradation. To improve long-context handling, dynamic approaches (Adnan et al., 2024; Liu et al., 2024; Zhang et al., 2024; Wan et al., 2024) utilize attention weights to identify important tokens. For example, Liu et al. (2024) detects repetitive patterns to estimate token significance, while Wang et al. (2024); Shi et al. (2024); Yu et al. (2024) merge similar tokens. However, these methods depend on full attention weights, making them incompatible with state-of-the-art (SOTA) efficient inference frameworks such as FlashAttention (Dao et al., 2022), which do not explicitly compute attention maps. This constraint limits their real-device efficiency. To overcome this, LaCache introduces an attention-free KV cache eviction strategy, ensuring high accuracy while maintaining real-device efficiency.
1486: 
1487: Efficient LLM inference.
1488: While traditional efficiency techniques such as quantization, pruning, and distillation (Frantar et al., 2022; Lin et al., 2024; Fu et al., 2024b; Shi et al., 2023; Zhang et al., 2023; Yuan et al., 2025) remain valuable, system-level optimizations, such as FlashAttention (Dao et al., 2022; Dao, 2023; Shah et al., 2024) and memory offloading (Sheng et al., 2023), have emerged as key enablers for large efficiency gains in LLM inference. Unlike most dynamic KV cache eviction methods, LaCache can be seamlessly integrated with these system-level approaches, enhancing real-device efficiency with SOTA inference frameworks.

full_text/2507.14204v1.txt:1485::1499 (0.3512)
1485: KV cache eviction techniques mitigate excessive cache growth by removing non-essential tokens. Early methods (Xiao et al., 2023b; Han et al., 2024) rely on static, naive retention strategies that overlook model processing patterns and input context, leading to accuracy degradation. To improve long-context handling, dynamic approaches (Adnan et al., 2024; Liu et al., 2024; Zhang et al., 2024; Wan et al., 2024) utilize attention weights to identify important tokens. For example, Liu et al. (2024) detects repetitive patterns to estimate token significance, while Wang et al. (2024); Shi et al. (2024); Yu et al. (2024) merge similar tokens. However, these methods depend on full attention weights, making them incompatible with state-of-the-art (SOTA) efficient inference frameworks such as FlashAttention (Dao et al., 2022), which do not explicitly compute attention maps. This constraint limits their real-device efficiency. To overcome this, LaCache introduces an attention-free KV cache eviction strategy, ensuring high accuracy while maintaining real-device efficiency.
1486: 
1487: Efficient LLM inference.
1488: While traditional efficiency techniques such as quantization, pruning, and distillation (Frantar et al., 2022; Lin et al., 2024; Fu et al., 2024b; Shi et al., 2023; Zhang et al., 2023; Yuan et al., 2025) remain valuable, system-level optimizations, such as FlashAttention (Dao et al., 2022; Dao, 2023; Shah et al., 2024) and memory offloading (Sheng et al., 2023), have emerged as key enablers for large efficiency gains in LLM inference. Unlike most dynamic KV cache eviction methods, LaCache can be seamlessly integrated with these system-level approaches, enhancing real-device efficiency with SOTA inference frameworks.
1489: 
1490: 2 RELATED WORK
1491: 
1492: Long-context LLM.
1493: The demand for long-context modeling has surged due to its ability to handle complex, multi-step tasks and maintain coherent interactions. This has spurred extensive research on enhancing long-context generation (Li et al., 2023; Peng et al., 2023; Ye et al., 2025), enabling models to process more tokens per forward pass. While approximate attention mechanisms (Beltagy et al., 2020; Kitaev et al., 2020; Wang et al., 2020) have improved efficiency, they usually lead to degradation in task accuracy. Recent advances in positional embeddings, such as position interpolation and fine-tuning (Chen et al., 2023; Peng & Quesnelle, 2023), have further extended context windows. However, inference efficiency remains a bottleneck for long input sequences. In our proposed LaCache, we leverage token eviction to enhance efficiency in long-context generation, including continuous or infinite generation tasks.
1494: 
1495: Long-context LLM.
1496: The demand for long-context modeling has surged due to its ability to handle complex, multi-step tasks and maintain coherent interactions. This has spurred extensive research on enhancing long-context generation (Li et al., 2023; Peng et al., 2023; Ye et al., 2025), enabling models to process more tokens per forward pass. While approximate attention mechanisms (Beltagy et al., 2020; Kitaev et al., 2020; Wang et al., 2020) have improved efficiency, they usually lead to degradation in task accuracy. Recent advances in positional embeddings, such as position interpolation and fine-tuning (Chen et al., 2023; Peng & Quesnelle, 2023), have further extended context windows. However, inference efficiency remains a bottleneck for long input sequences. In our proposed LaCache, we leverage token eviction to enhance efficiency in long-context generation, including continuous or infinite generation tasks.
1497: 
1498: KV cache eviction.
1499: KV cache eviction techniques mitigate excessive cache growth by removing non-essential tokens. Early methods (Xiao et al., 2023b; Han et al., 2024) rely on static, naive retention strategies that overlook model processing patterns and input context, leading to accuracy degradation. To improve long-context handling, dynamic approaches (Adnan et al., 2024; Liu et al., 2024; Zhang et al., 2024; Wan et al., 2024) utilize attention weights to identify important tokens. For example, Liu et al. (2024) detects repetitive patterns to estimate token significance, while Wang et al. (2024); Shi et al. (2024); Yu et al. (2024) merge similar tokens. However, these methods depend on full attention weights, making them incompatible with state-of-the-art (SOTA) efficient inference frameworks such as FlashAttention (Dao et al., 2022), which do not explicitly compute attention maps. This constraint limits their real-device efficiency. To overcome this, LaCache introduces an attention-free KV cache eviction strategy, ensuring high accuracy while maintaining real-device efficiency.

full_text/2507.14204v1.txt:1488::1502 (0.3512)
1488: While traditional efficiency techniques such as quantization, pruning, and distillation (Frantar et al., 2022; Lin et al., 2024; Fu et al., 2024b; Shi et al., 2023; Zhang et al., 2023; Yuan et al., 2025) remain valuable, system-level optimizations, such as FlashAttention (Dao et al., 2022; Dao, 2023; Shah et al., 2024) and memory offloading (Sheng et al., 2023), have emerged as key enablers for large efficiency gains in LLM inference. Unlike most dynamic KV cache eviction methods, LaCache can be seamlessly integrated with these system-level approaches, enhancing real-device efficiency with SOTA inference frameworks.
1489: 
1490: 2 RELATED WORK
1491: 
1492: Long-context LLM.
1493: The demand for long-context modeling has surged due to its ability to handle complex, multi-step tasks and maintain coherent interactions. This has spurred extensive research on enhancing long-context generation (Li et al., 2023; Peng et al., 2023; Ye et al., 2025), enabling models to process more tokens per forward pass. While approximate attention mechanisms (Beltagy et al., 2020; Kitaev et al., 2020; Wang et al., 2020) have improved efficiency, they usually lead to degradation in task accuracy. Recent advances in positional embeddings, such as position interpolation and fine-tuning (Chen et al., 2023; Peng & Quesnelle, 2023), have further extended context windows. However, inference efficiency remains a bottleneck for long input sequences. In our proposed LaCache, we leverage token eviction to enhance efficiency in long-context generation, including continuous or infinite generation tasks.
1494: 
1495: Long-context LLM.
1496: The demand for long-context modeling has surged due to its ability to handle complex, multi-step tasks and maintain coherent interactions. This has spurred extensive research on enhancing long-context generation (Li et al., 2023; Peng et al., 2023; Ye et al., 2025), enabling models to process more tokens per forward pass. While approximate attention mechanisms (Beltagy et al., 2020; Kitaev et al., 2020; Wang et al., 2020) have improved efficiency, they usually lead to degradation in task accuracy. Recent advances in positional embeddings, such as position interpolation and fine-tuning (Chen et al., 2023; Peng & Quesnelle, 2023), have further extended context windows. However, inference efficiency remains a bottleneck for long input sequences. In our proposed LaCache, we leverage token eviction to enhance efficiency in long-context generation, including continuous or infinite generation tasks.
1497: 
1498: KV cache eviction.
1499: KV cache eviction techniques mitigate excessive cache growth by removing non-essential tokens. Early methods (Xiao et al., 2023b; Han et al., 2024) rely on static, naive retention strategies that overlook model processing patterns and input context, leading to accuracy degradation. To improve long-context handling, dynamic approaches (Adnan et al., 2024; Liu et al., 2024; Zhang et al., 2024; Wan et al., 2024) utilize attention weights to identify important tokens. For example, Liu et al. (2024) detects repetitive patterns to estimate token significance, while Wang et al. (2024); Shi et al. (2024); Yu et al. (2024) merge similar tokens. However, these methods depend on full attention weights, making them incompatible with state-of-the-art (SOTA) efficient inference frameworks such as FlashAttention (Dao et al., 2022), which do not explicitly compute attention maps. This constraint limits their real-device efficiency. To overcome this, LaCache introduces an attention-free KV cache eviction strategy, ensuring high accuracy while maintaining real-device efficiency.
1500: 
1501: KV cache eviction.
1502: KV cache eviction techniques mitigate excessive cache growth by removing non-essential tokens. Early methods (Xiao et al., 2023b; Han et al., 2024) rely on static, naive retention strategies that overlook model processing patterns and input context, leading to accuracy degradation. To improve long-context handling, dynamic approaches (Adnan et al., 2024; Liu et al., 2024; Zhang et al., 2024; Wan et al., 2024) utilize attention weights to identify important tokens. For example, Liu et al. (2024) detects repetitive patterns to estimate token significance, while Wang et al. (2024); Shi et al. (2024); Yu et al. (2024) merge similar tokens. However, these methods depend on full attention weights, making them incompatible with state-of-the-art (SOTA) efficient inference frameworks such as FlashAttention (Dao et al., 2022), which do not explicitly compute attention maps. This constraint limits their real-device efficiency. To overcome this, LaCache introduces an attention-free KV cache eviction strategy, ensuring high accuracy while maintaining real-device efficiency.

full_text/2507.16795v2.txt:2449::2463 (0.3584)
2449: 
2450: Tokens
2451: 1B
2452: 
2453: Batch size
2454: 4096
2455: 
2456: LLM context length
2457: 2048
2458: 
2459: Learning rate
2460: 3e-4
2461: 
2462: Learning rate warmup (from 0)
2463: 1000 steps

full_text/2507.16795v2.txt:7519::7533 (0.3584)
7519: 
7520: Tokens
7521: 1B
7522: 
7523: Batch size
7524: 4096
7525: 
7526: LLM context length
7527: 2048
7528: 
7529: Learning rate
7530: 3e-4
7531: 
7532: Learning rate warmup (from 0)
7533: 1000 steps

full_text/2507.16795v2.txt:7714::7728 (0.3584)
7714: 
7715: Tokens
7716: 1B
7717: 
7718: Batch size
7719: 4096
7720: 
7721: LLM context length
7722: 2048
7723: 
7724: Learning rate
7725: 3e-4
7726: 
7727: Learning rate warmup (from 0)
7728: 1000 steps

full_text/2508.04482v1.txt:305::319 (0.4254)
 305: -
 306: -
 307: ✓
 308: 10/2023
 309: 
 310: WebAgent (Iong et al., 2024)
 311: 
 312: Concat. LLMs
 313: ✓
 314: ✓
 315: -
 316: 07/2023
 317: 
 318: WebGUM (Furuta et al., 2023)
 319: 

full_text/2508.04482v1.txt:3448::3462 (0.4254)
3448: -
3449: -
3450: ✓
3451: 10/2023
3452: 
3453: WebAgent (Iong et al., 2024)
3454: 
3455: Concat. LLMs
3456: ✓
3457: ✓
3458: -
3459: 07/2023
3460: 
3461: WebGUM (Furuta et al., 2023)
3462: 

full_text/2507.11017v1.txt:26::40 (0.4288)
  26: 
  27: 2 Related Work
  28: 
  29: Post-training Quantization.
  30: 
  31: Quantization not only reduces memory consumption by mapping full-precision weights to low-bit fixed-point formats such as int8 or int4, but also enables dynamic quantization of activations into low-bit representations. This facilitates efficient operations, including multiplication of low-bit matrixes. To alleviate accuracy degradation caused by the transition from full-precision to low-bit formats, reconstruction-based methods such as AdaRound (nagel2020up, ), BRECQ (li2021brecq, ), and QDrop (wei2022qdrop, ) have been developed. These techniques measure and minimize quantization errors within layers or blocks, demonstrating strong performance on architectures such as ResNet. However, because of the substantial computational cost incurred during calibration, these approaches are challenging to apply directly to large language models (LLMs), which typically contain billions of parameters.
  32: 
  33: PTQ Methods for LLMs.
  34: 
  35: Numerous PTQ strategies have been proposed to address the outlier characteristics commonly observed in LLM. Some methods preserve outliers by maintaining them in higher-bit precision formats, such as LLM.int8() (dettmers2022gpt3, ) and AWQ. Others employ smoothing-based scaling techniques (e.g., SmoothQuant (xiao2023smoothquant, ), OmniQuant (shao2023omniquant, )), rotation-based transformations (e.g., QuaRot (ashkboos2024quarot, ), SpinQuant (liu2024spinquant, )), or channel rearrangement methods (e.g., RPTQ (yuan2023rptq, )). These approaches primarily focus on adjusting the distributional properties of weights and activations and have demonstrated promising results in the quantization of activations.
  36: In contrast to these transformation-based methods, which typically apply scaling or clipping prior to quantization, techniques like GPTQ (frantar2022gptq, ) explicitly model the quantization loss and directly modify the full-precision latent weights during calibration. This loss-aware strategy can be effectively combined with other advanced quantization techniques, such as SpinQuant (liu2024spinquant, ), and has recently led to significant improvements exemplified by methods like GPTAQ (li2025gptqv2, ).
  37: 
  38: Figure 1: Overview of the first-order compensation item in our proposed FOEM.
  39: 
  40: 3 Method


```

</details>


---

### 3. Query: According to Gutekunst et al., what is the core limitation of word clouds for comparing content across different directories in large datasets?

- **Query ID:** `simple_3`
- **Query Type:** Simple
- **Curated Source Files:** `full_text/2505.07796v2.txt, full_text/2506.15594v1.txt, full_text/2506.22309v1.txt, full_text/2507.15152v1.txt, full_text/2508.14302v1.txt, full_text/2508.15370v1.txt`

#### LLM Ground Truth Answer

> The core limitation of word clouds for comparing content across different directories in large datasets, according to Gutekunst et al., is that while they are intuitive and provide an overview of frequent terms, it is complicated to compare the content of different directories due to their unstructured nature. They also fail to capture semantic relationships and their quality depends on the text extraction process.

**Source Document(s):** `full_text/2506.22309v1.txt`

#### `search` Tool Performance

**Command Executed:**

```bash
search "According to Gutekunst et al., what is the core limitation of word clouds for comparing content across different directories in large datasets?" full_text/*.txt --top-k 10 --n-lines 7
```

**Retrieval Precision:** `1.00`
**Retrieval Recall:** `1.00`

**Documents Returned by `search`:** `full_text/2506.22309v1.txt`

#### LLM Search-Augmented Answer

> According to Gutekunst et al., the core limitation of word clouds for comparing content across different directories in large datasets is twofold. Firstly, comparing multiple directories using word clouds is challenging due to their unstructured nature. Secondly, for large-scale datasets, the sheer number of directories further complicates the interpretation of the visualization, making this approach ineffective.

<details><summary>View Original `search` Tool Output</summary>

```
full_text/2506.22309v1.txt:652::666 (0.3526)
 652: Our evaluation demonstrates that the proposed FCA-based method FAT-CAT
 653: offers superior insights into the dataset’s structure.
 654: 
 655: Word clouds provide an intuitive overview by highlighting frequently occurring terms,
 656: enabling the identification of noteworthy directories.
 657: However, they fail to capture semantic relationships and
 658: depend heavily on the text extraction quality.
 659: Additionally, comparing multiple directories using word clouds is challenging
 660: due to their unstructured nature.
 661: In contrast, embedding-based visualization techniques allows directly comparing directories
 662: based on their content.
 663: Not only does the quality of the reducers affect the results,
 664: but the large number of directories also complicates the interpretation of the visualization.
 665: This approach is therefore ineffective for large-scale datasets.
 666: NER-based clustering of category entities suffers from frequent misclassification.

full_text/2506.22309v1.txt:2322::2336 (0.3526)
2322: Our evaluation demonstrates that the proposed FCA-based method FAT-CAT
2323: offers superior insights into the dataset’s structure.
2324: 
2325: Word clouds provide an intuitive overview by highlighting frequently occurring terms,
2326: enabling the identification of noteworthy directories.
2327: However, they fail to capture semantic relationships and
2328: depend heavily on the text extraction quality.
2329: Additionally, comparing multiple directories using word clouds is challenging
2330: due to their unstructured nature.
2331: In contrast, embedding-based visualization techniques allows directly comparing directories
2332: based on their content.
2333: Not only does the quality of the reducers affect the results,
2334: but the large number of directories also complicates the interpretation of the visualization.
2335: This approach is therefore ineffective for large-scale datasets.
2336: NER-based clustering of category entities suffers from frequent misclassification.

full_text/2506.22309v1.txt:2850::2864 (0.3526)
2850: Our evaluation demonstrates that the proposed FCA-based method FAT-CAT
2851: offers superior insights into the dataset’s structure.
2852: 
2853: Word clouds provide an intuitive overview by highlighting frequently occurring terms,
2854: enabling the identification of noteworthy directories.
2855: However, they fail to capture semantic relationships and
2856: depend heavily on the text extraction quality.
2857: Additionally, comparing multiple directories using word clouds is challenging
2858: due to their unstructured nature.
2859: In contrast, embedding-based visualization techniques allows directly comparing directories
2860: based on their content.
2861: Not only does the quality of the reducers affect the results,
2862: but the large number of directories also complicates the interpretation of the visualization.
2863: This approach is therefore ineffective for large-scale datasets.
2864: NER-based clustering of category entities suffers from frequent misclassification.

full_text/2506.22309v1.txt:2882::2896 (0.3526)
2882: Our evaluation demonstrates that the proposed FCA-based method FAT-CAT
2883: offers superior insights into the dataset’s structure.
2884: 
2885: Word clouds provide an intuitive overview by highlighting frequently occurring terms,
2886: enabling the identification of noteworthy directories.
2887: However, they fail to capture semantic relationships and
2888: depend heavily on the text extraction quality.
2889: Additionally, comparing multiple directories using word clouds is challenging
2890: due to their unstructured nature.
2891: In contrast, embedding-based visualization techniques allows directly comparing directories
2892: based on their content.
2893: Not only does the quality of the reducers affect the results,
2894: but the large number of directories also complicates the interpretation of the visualization.
2895: This approach is therefore ineffective for large-scale datasets.
2896: NER-based clustering of category entities suffers from frequent misclassification.

full_text/2506.22309v1.txt:2902::2916 (0.3526)
2902: this method remains the most effective for uncovering the relationships between directory topics.
2903: Among the evaluated methods, FAT-CAT proves to be the most effective for structured data exploration.
2904: 
2905: Word clouds provide an intuitive overview by highlighting frequently occurring terms,
2906: enabling the identification of noteworthy directories.
2907: However, they fail to capture semantic relationships and
2908: depend heavily on the text extraction quality.
2909: Additionally, comparing multiple directories using word clouds is challenging
2910: due to their unstructured nature.
2911: In contrast, embedding-based visualization techniques allows directly comparing directories
2912: based on their content.
2913: Not only does the quality of the reducers affect the results,
2914: but the large number of directories also complicates the interpretation of the visualization.
2915: This approach is therefore ineffective for large-scale datasets.
2916: NER-based clustering of category entities suffers from frequent misclassification.

full_text/2506.22309v1.txt:377::391 (0.4164)
 377: 
 378: Word clouds
 379: 
 380: An initial approach for visualizing topics involves using word clouds,
 381: a simple and intuitive method for displaying the most frequent words in a document.
 382: A word cloud is a visual representation of text data where words are displayed in varying sizes based on their frequency or importance. It helps identify key themes and trends in textual content at a glance.
 383: Since we are interested in the content of the directories,
 384: we generate word clouds for each directory in the dataset.
 385: The Figures 9(a) and 9(b)
 386: show examples of word clouds.
 387: 
 388:  Embedding - Dimension Reduction (EDR)
 389: 
 390: The second baseline approach EDR, whose workflow is illustrated in Figure 4,
 391: aims to cluster documents by directories

full_text/2506.22309v1.txt:1810::1824 (0.4164)
1810: 
1811: Word clouds
1812: 
1813: An initial approach for visualizing topics involves using word clouds,
1814: a simple and intuitive method for displaying the most frequent words in a document.
1815: A word cloud is a visual representation of text data where words are displayed in varying sizes based on their frequency or importance. It helps identify key themes and trends in textual content at a glance.
1816: Since we are interested in the content of the directories,
1817: we generate word clouds for each directory in the dataset.
1818: The Figures 9(a) and 9(b)
1819: show examples of word clouds.
1820: 
1821:  Embedding - Dimension Reduction (EDR)
1822: 
1823: The second baseline approach EDR, whose workflow is illustrated in Figure 4,
1824: aims to cluster documents by directories

full_text/2506.22309v1.txt:1897::1911 (0.4164)
1897: 
1898: Word clouds
1899: 
1900: An initial approach for visualizing topics involves using word clouds,
1901: a simple and intuitive method for displaying the most frequent words in a document.
1902: A word cloud is a visual representation of text data where words are displayed in varying sizes based on their frequency or importance. It helps identify key themes and trends in textual content at a glance.
1903: Since we are interested in the content of the directories,
1904: we generate word clouds for each directory in the dataset.
1905: The Figures 9(a) and 9(b)
1906: show examples of word clouds.
1907: 
1908: WORD CLOUDS
1909: 
1910: An initial approach for visualizing topics involves using word clouds,
1911: a simple and intuitive method for displaying the most frequent words in a document.

full_text/2506.22309v1.txt:1907::1921 (0.4164)
1907: 
1908: WORD CLOUDS
1909: 
1910: An initial approach for visualizing topics involves using word clouds,
1911: a simple and intuitive method for displaying the most frequent words in a document.
1912: A word cloud is a visual representation of text data where words are displayed in varying sizes based on their frequency or importance. It helps identify key themes and trends in textual content at a glance.
1913: Since we are interested in the content of the directories,
1914: we generate word clouds for each directory in the dataset.
1915: The Figures 9(a) and 9(b)
1916: show examples of word clouds.
1917: 
1918: An initial approach for visualizing topics involves using word clouds,
1919: a simple and intuitive method for displaying the most frequent words in a document.
1920: A word cloud is a visual representation of text data where words are displayed in varying sizes based on their frequency or importance. It helps identify key themes and trends in textual content at a glance.
1921: Since we are interested in the content of the directories,

full_text/2506.22309v1.txt:1915::1929 (0.4164)
1915: The Figures 9(a) and 9(b)
1916: show examples of word clouds.
1917: 
1918: An initial approach for visualizing topics involves using word clouds,
1919: a simple and intuitive method for displaying the most frequent words in a document.
1920: A word cloud is a visual representation of text data where words are displayed in varying sizes based on their frequency or importance. It helps identify key themes and trends in textual content at a glance.
1921: Since we are interested in the content of the directories,
1922: we generate word clouds for each directory in the dataset.
1923: The Figures 9(a) and 9(b)
1924: show examples of word clouds.
1925: 
1926: Embedding - Dimension Reduction (EDR)
1927: 
1928: The second baseline approach EDR, whose workflow is illustrated in Figure 4,
1929: aims to cluster documents by directories


```

</details>


---

### 4. Query: Compare and contrast how "multimodal risks" in MLLMs (as defined by Zhang et al.) relate to "distribution shift" in CPT (as discussed by Wang et al.), focusing on the source or nature of these challenges.

- **Query ID:** `synthesis_1`
- **Query Type:** Synthesis
- **Curated Source Files:** `full_text/2505.07796v2.txt, full_text/2506.15594v1.txt, full_text/2506.22309v1.txt, full_text/2507.15152v1.txt, full_text/2508.14302v1.txt, full_text/2508.15370v1.txt`

#### LLM Ground Truth Answer

> Wang et al. discuss "distribution shift" in Continual Pre-Training (CPT) as a deviation in the loss curve caused by the distributional distance between the pre-training (PT) and CPT data. It affects model learning dynamics and contributes to a trade-off between general and downstream domain performance. Its term is influenced by learning rate values and replay ratio. In contrast, Zhang et al. define "multimodal risks" in Multimodal Large Language Models (MLLMs) as trustworthiness concerns arising in new multimodal scenarios, such as image-specific threats or image-text pairs, where misguiding factors and adversarial noises are imposed on images in multimodal QA or image captioning tasks. While both concepts address challenges related to data distribution and model behavior, Wang et al.'s "distribution shift" describes a fundamental learning dynamic in sequential domain adaptation, whereas Zhang et al.'s "multimodal risks" are specifically about security and reliability vulnerabilities stemming from the integration of the visual input modality and its interactions with language.

**Source Document(s):** `full_text/2505.07796v2.txt, full_text/2508.15370v1.txt`

#### `search` Tool Performance

**Command Executed:**

```bash
search "Compare and contrast how \"multimodal risks\" in MLLMs (as defined by Zhang et al.) relate to \"distribution shift\" in CPT (as discussed by Wang et al.), focusing on the source or nature of these challenges." full_text/*.txt --top-k 10 --n-lines 7
```

**Retrieval Precision:** `0.33`
**Retrieval Recall:** `0.50`

**Documents Returned by `search`:** `full_text/2505.07796v2.txt, full_text/2507.14200v1.txt, full_text/2508.01191v3.txt`

#### LLM Search-Augmented Answer

> The provided search results contain no information about "multimodal risks" in MLLMs as defined by Zhang et al. Therefore, a comprehensive comparison and contrast focusing on this aspect cannot be performed. 
> 
> However, the search results do discuss "distribution shift" in CPT (Continual Pre-training) and in the context of CoT (Chain-of-Thought) reasoning, with references to Wang et al.'s work on the impact of Learning Rate Schedules (LRS). 
> 
> In CPT, the nature of "distribution shift" is defined as the deviation from the hidden Pre-training (PT) curve and reflects the 'distributional distance' between the pre-training data (Dpt) and the continual pre-training data (Dcpt). This shift is affected by the LRS during the CPT stage. 
> 
> In the context of CoT, distributional shifts are identified along three critical dimensions, revealing the pattern-matching nature of CoT: 
> 1.  **Task generalization:** Occurs when novel tasks introduce unique elements and underlying logical structures that differ from the learned reasoning patterns. 
> 2.  **Length generalization:** Arises when test cases require reasoning chains that are substantially longer or shorter than those present in the training data, creating a discrepancy in sequence length. 
> 3.  **Format generalization:** Refers to sensitivity to variations in prompt formulation and structure, which can be challenging to manage due to diverse training data or user backgrounds. 
> 
> The underlying source of these CoT-related challenges is the model's reliance on pattern-matching from the statistical regularities in its training distribution rather than genuine reasoning. Performance degrades predictably as this distributional discrepancy increases.

<details><summary>View Original `search` Tool Output</summary>

```
full_text/2508.01191v3.txt:126::140 (0.4007)
 126: 
 127: (4)
 128: 
 129: where Λ>0\Lambda>0 is a Lipschitz constant that depends on the model architecture and task complexity, nn is the training sample size, and the bound holds with probability 1−δ1-\delta, where δ\delta is the failure probability.
 130: 
 131: The proof is provided in Appendix A.1
 132: 
 133: Building on this data distribution perspective, we identify three critical dimensions along which distributional shifts can occur, each revealing different aspects of CoT’s pattern-matching nature: ➊ Task generalization examines how well CoT transfers across different types of reasoning tasks. Novel tasks may have unique elements and underlying logical structure, which introduces distributional shifts that challenge the model’s ability to apply learned reasoning patterns. ➋ Length generalization investigates CoT’s robustness to reasoning chains of varying lengths. Since training data typically contains reasoning sequences within a certain length range, test cases requiring substantially longer or shorter reasoning chains represent a form of distributional shift along the sequence length dimension. This length discrepancy could result from the reasoning step or the text-dependent solution space. ➌ Format generalization explores how sensitive CoT is to variations in prompt formulation and structure. Due to various reasons (e.g., sophistical training data or diverse background of users), it is challenging for LLM practitioners to design a golden prompt to elicit knowledge suitable for the current case. Their detailed definition and implementation are given in subsequent sections.
 134: 
 135: Each dimension provides a unique lens for understanding the boundaries of CoT’s effectiveness and the mechanisms underlying its apparent reasoning capabilities. By systematically varying these dimensions in controlled experimental settings, we can empirically validate our hypothesis that CoT performance degrades predictably as distributional discrepancy increases, thereby revealing its fundamental nature as a pattern-matching rather than reasoning system.
 136: 
 137: 4 DataAlchemy: An Isolated and Controlled Environment
 138: 
 139: To systematically investigate the influence of distributional shifts on CoT reasoning capabilities, we introduce DataAlchemy, a synthetic dataset framework designed for controlled experimentation. This environment enables us to train language models from scratch under precisely defined conditions, allowing for rigorous analysis of CoT behavior across different OOD scenarios. The overview is shown in Figure 2.
 140: 

full_text/2508.01191v3.txt:1395::1409 (0.4007)
1395: 
1396: (4)
1397: 
1398: where Λ>0\Lambda>0 is a Lipschitz constant that depends on the model architecture and task complexity, nn is the training sample size, and the bound holds with probability 1−δ1-\delta, where δ\delta is the failure probability.
1399: 
1400: The proof is provided in Appendix A.1
1401: 
1402: Building on this data distribution perspective, we identify three critical dimensions along which distributional shifts can occur, each revealing different aspects of CoT’s pattern-matching nature: ➊ Task generalization examines how well CoT transfers across different types of reasoning tasks. Novel tasks may have unique elements and underlying logical structure, which introduces distributional shifts that challenge the model’s ability to apply learned reasoning patterns. ➋ Length generalization investigates CoT’s robustness to reasoning chains of varying lengths. Since training data typically contains reasoning sequences within a certain length range, test cases requiring substantially longer or shorter reasoning chains represent a form of distributional shift along the sequence length dimension. This length discrepancy could result from the reasoning step or the text-dependent solution space. ➌ Format generalization explores how sensitive CoT is to variations in prompt formulation and structure. Due to various reasons (e.g., sophistical training data or diverse background of users), it is challenging for LLM practitioners to design a golden prompt to elicit knowledge suitable for the current case. Their detailed definition and implementation are given in subsequent sections.
1403: 
1404: Each dimension provides a unique lens for understanding the boundaries of CoT’s effectiveness and the mechanisms underlying its apparent reasoning capabilities. By systematically varying these dimensions in controlled experimental settings, we can empirically validate our hypothesis that CoT performance degrades predictably as distributional discrepancy increases, thereby revealing its fundamental nature as a pattern-matching rather than reasoning system.
1405: 
1406: 3 THE DATA DISTRIBUTION LENS
1407: 
1408: We propose a fundamental reframing to understand what CoT actually represents. We hypothesize that the underlying mechanism is better understood through the lens of data distribution: rather than executing explicit reasoning procedures, CoT operates as a pattern-matching process that interpolates and extrapolates from the statistical regularities present in its training distribution. Specifically, we posit that CoT’s success stems not from a model’s inherent reasoning capacity, but from its ability to generalize conditionally to out-of-distribution (OOD) test cases that are structurally similar to in-distribution exemplars.
1409: 

full_text/2508.01191v3.txt:1481::1495 (0.4007)
1481: 
1482: where Λ>0\Lambda>0 is a Lipschitz constant that depends on the model architecture and task complexity, nn is the training sample size, and the bound holds with probability 1−δ1-\delta, where δ\delta is the failure probability.
1483: 
1484: The proof is provided in Appendix A.1
1485: 
1486: The proof is provided in Appendix A.1
1487: 
1488: Building on this data distribution perspective, we identify three critical dimensions along which distributional shifts can occur, each revealing different aspects of CoT’s pattern-matching nature: ➊ Task generalization examines how well CoT transfers across different types of reasoning tasks. Novel tasks may have unique elements and underlying logical structure, which introduces distributional shifts that challenge the model’s ability to apply learned reasoning patterns. ➋ Length generalization investigates CoT’s robustness to reasoning chains of varying lengths. Since training data typically contains reasoning sequences within a certain length range, test cases requiring substantially longer or shorter reasoning chains represent a form of distributional shift along the sequence length dimension. This length discrepancy could result from the reasoning step or the text-dependent solution space. ➌ Format generalization explores how sensitive CoT is to variations in prompt formulation and structure. Due to various reasons (e.g., sophistical training data or diverse background of users), it is challenging for LLM practitioners to design a golden prompt to elicit knowledge suitable for the current case. Their detailed definition and implementation are given in subsequent sections.
1489: 
1490: Building on this data distribution perspective, we identify three critical dimensions along which distributional shifts can occur, each revealing different aspects of CoT’s pattern-matching nature: ➊ Task generalization examines how well CoT transfers across different types of reasoning tasks. Novel tasks may have unique elements and underlying logical structure, which introduces distributional shifts that challenge the model’s ability to apply learned reasoning patterns. ➋ Length generalization investigates CoT’s robustness to reasoning chains of varying lengths. Since training data typically contains reasoning sequences within a certain length range, test cases requiring substantially longer or shorter reasoning chains represent a form of distributional shift along the sequence length dimension. This length discrepancy could result from the reasoning step or the text-dependent solution space. ➌ Format generalization explores how sensitive CoT is to variations in prompt formulation and structure. Due to various reasons (e.g., sophistical training data or diverse background of users), it is challenging for LLM practitioners to design a golden prompt to elicit knowledge suitable for the current case. Their detailed definition and implementation are given in subsequent sections.
1491: 
1492: Each dimension provides a unique lens for understanding the boundaries of CoT’s effectiveness and the mechanisms underlying its apparent reasoning capabilities. By systematically varying these dimensions in controlled experimental settings, we can empirically validate our hypothesis that CoT performance degrades predictably as distributional discrepancy increases, thereby revealing its fundamental nature as a pattern-matching rather than reasoning system.
1493: 
1494: Each dimension provides a unique lens for understanding the boundaries of CoT’s effectiveness and the mechanisms underlying its apparent reasoning capabilities. By systematically varying these dimensions in controlled experimental settings, we can empirically validate our hypothesis that CoT performance degrades predictably as distributional discrepancy increases, thereby revealing its fundamental nature as a pattern-matching rather than reasoning system.
1495: 

full_text/2508.01191v3.txt:1483::1497 (0.4007)
1483: 
1484: The proof is provided in Appendix A.1
1485: 
1486: The proof is provided in Appendix A.1
1487: 
1488: Building on this data distribution perspective, we identify three critical dimensions along which distributional shifts can occur, each revealing different aspects of CoT’s pattern-matching nature: ➊ Task generalization examines how well CoT transfers across different types of reasoning tasks. Novel tasks may have unique elements and underlying logical structure, which introduces distributional shifts that challenge the model’s ability to apply learned reasoning patterns. ➋ Length generalization investigates CoT’s robustness to reasoning chains of varying lengths. Since training data typically contains reasoning sequences within a certain length range, test cases requiring substantially longer or shorter reasoning chains represent a form of distributional shift along the sequence length dimension. This length discrepancy could result from the reasoning step or the text-dependent solution space. ➌ Format generalization explores how sensitive CoT is to variations in prompt formulation and structure. Due to various reasons (e.g., sophistical training data or diverse background of users), it is challenging for LLM practitioners to design a golden prompt to elicit knowledge suitable for the current case. Their detailed definition and implementation are given in subsequent sections.
1489: 
1490: Building on this data distribution perspective, we identify three critical dimensions along which distributional shifts can occur, each revealing different aspects of CoT’s pattern-matching nature: ➊ Task generalization examines how well CoT transfers across different types of reasoning tasks. Novel tasks may have unique elements and underlying logical structure, which introduces distributional shifts that challenge the model’s ability to apply learned reasoning patterns. ➋ Length generalization investigates CoT’s robustness to reasoning chains of varying lengths. Since training data typically contains reasoning sequences within a certain length range, test cases requiring substantially longer or shorter reasoning chains represent a form of distributional shift along the sequence length dimension. This length discrepancy could result from the reasoning step or the text-dependent solution space. ➌ Format generalization explores how sensitive CoT is to variations in prompt formulation and structure. Due to various reasons (e.g., sophistical training data or diverse background of users), it is challenging for LLM practitioners to design a golden prompt to elicit knowledge suitable for the current case. Their detailed definition and implementation are given in subsequent sections.
1491: 
1492: Each dimension provides a unique lens for understanding the boundaries of CoT’s effectiveness and the mechanisms underlying its apparent reasoning capabilities. By systematically varying these dimensions in controlled experimental settings, we can empirically validate our hypothesis that CoT performance degrades predictably as distributional discrepancy increases, thereby revealing its fundamental nature as a pattern-matching rather than reasoning system.
1493: 
1494: Each dimension provides a unique lens for understanding the boundaries of CoT’s effectiveness and the mechanisms underlying its apparent reasoning capabilities. By systematically varying these dimensions in controlled experimental settings, we can empirically validate our hypothesis that CoT performance degrades predictably as distributional discrepancy increases, thereby revealing its fundamental nature as a pattern-matching rather than reasoning system.
1495: 
1496: 4 DataAlchemy: An Isolated and Controlled Environment
1497: 

full_text/2507.14200v1.txt:65::79 (0.4039)
  65: Recently, Large Language Models (LLMs) OpenAI (2025); Anthropic (2025a, b) have achieved remarkable success in numerous fields of natural language processing, such as machine translation Hutchins (1995); Poibeau (2017), text summarization Stahlberg (2020) and sentence analysis Verspoor and Sauter (2000).
  66: However, as the amount of training data and parameters increases consistently, optimizing a single LLM brings unbearable computational overhead with marginal performance gains. Meanwhile, with the development of LLM training techniques, a growing number of heterogeneous LLMs, particularly open-source LLMs trained on disparate data, have emerged. Due to the structural diversity and training data bias, these LLMs possess diverse specialized skills and are expert in distinct areas. This diversity in capabilities gives rise to complementarity, while the growing number of LLMs offers the potential for sustained expansion of such complementary strengths. Therefore, a pivotal and valuable question naturally arises: how can we sustainably harness and scale up the vast and diverse ensemble of LLMs to continually push the performance frontier or the intelligence upper bound?
  67: 
  68: To answer this question, a mainstream method is to construct a multi-agent collaborative system (MACS). MACS aims to orchestrate interactions among multiple agents, enable information exchange and integration, and generate high-quality responses.
  69: Emerging works have explored building MACS by employing diverse LLMs as agents, which can be roughly categorized into two classes: (1) MACS via prior LLM selection. These approaches Chen et al. (2025); Lu et al. (2023); Shnitzer et al. (2023); Chen et al. (2024d) select appropriate LLMs before response generation by leveraging prior knowledge corresponding to LLMs, such as their performance on standard benchmarks Shnitzer et al. (2023) or model embeddings Chen et al. (2024d) obtained from training on specific datasets. By selecting the most suitable models for each given question in advance, these methods aim to increase the likelihood of generating high-quality responses and reduce computational overhead by avoiding the inference of unsuitable LLMs.
  70: (2) MACS via posterior response enhancement. These approaches Chen et al. (2024c, 2023a); Gui et al. (2024); Choudhury (2025) assess the quality of responses after each LLM has generated its answer, using inter- or intra-response criteria such as reward model scores Choudhury (2025), perplexity Mavromatis et al. (2024), or majority voting Li et al. (2024). Due to performing reasoning in advance, these methods provide a more accurate evaluation of response quality compared to relying solely on prior information.
  71: 
  72: However, both categories of methods encounter a dilemma when scaling the number of LLMs and tasks. For MACS based on prior LLM selection, they either require end-to-end router training Chen et al. (2024d) for each individual LLM, making it difficult to continuously incorporate new LLMs, or rely on limited and discrete capability labels Chen et al. (2025), which are insufficient for comprehensive analysis on a given question and hard to handle unseen questions. As a result, they exhibit suboptimal performance when facing
  73: unseen questions. For MACS based on posterior response enhancement, these methods typically rely on a single posterior criterion, which can introduce bias and lead to inaccurate quality assessments. Moreover, they mainly focus on selecting from an existing pool of responses, lacking the ability to generate new and diverse high-quality responses, limiting their performance upper bound. Besides the aforementioned limitations, current MACS methods often fail to effectively integrate prior and posterior methods in a coupled manner, which causes unfiltered low-quality responses as bottlenecks, which significantly hinders the overall performance and scalability of the collaboration system.
  74: 
  75: To enhance the
  76: scalability and break through the performance upper bound of MACS, we
  77: propose a novel framework called Scalable Multi-Agent Collaboration System (SMACS).
  78: Specifically, we first construct a question bank comprising diverse questions from multiple domains, along with an LLM pool containing plentiful heterogeneous LLMs. Each LLM in the pool is evaluated on the question bank to record its response to every question, representing its capacity across diverse domains. Further, inspired by Retrieval-Augmented Generation (RAG) Lewis et al. (2020); Chen et al. (2024a), we design a retrieval-based prior selection strategy: given any question, we retrieve similar questions from the question bank. A weighted score is computed for each LLM based on its performance on the retrieved questions, which serves as the prior information for selecting high-scoring LLMs.
  79: After that, we introduce exploration–exploitation-driven posterior enhancement: in the exploration phase, these responses are dropped via prior scores to form multiple answer subsets, which are independently aggregated by an LLM aggregator; in the exploitation phase, the aggregating responses are evaluated using a hybrid posterior scores of mean pairwise similarity and perplexity. The aggregated response with the highest score is selected as the final response.

full_text/2507.14200v1.txt:1927::1941 (0.4039)
1927: Recently, Large Language Models (LLMs) OpenAI (2025); Anthropic (2025a, b) have achieved remarkable success in numerous fields of natural language processing, such as machine translation Hutchins (1995); Poibeau (2017), text summarization Stahlberg (2020) and sentence analysis Verspoor and Sauter (2000).
1928: However, as the amount of training data and parameters increases consistently, optimizing a single LLM brings unbearable computational overhead with marginal performance gains. Meanwhile, with the development of LLM training techniques, a growing number of heterogeneous LLMs, particularly open-source LLMs trained on disparate data, have emerged. Due to the structural diversity and training data bias, these LLMs possess diverse specialized skills and are expert in distinct areas. This diversity in capabilities gives rise to complementarity, while the growing number of LLMs offers the potential for sustained expansion of such complementary strengths. Therefore, a pivotal and valuable question naturally arises: how can we sustainably harness and scale up the vast and diverse ensemble of LLMs to continually push the performance frontier or the intelligence upper bound?
1929: 
1930: To answer this question, a mainstream method is to construct a multi-agent collaborative system (MACS). MACS aims to orchestrate interactions among multiple agents, enable information exchange and integration, and generate high-quality responses.
1931: Emerging works have explored building MACS by employing diverse LLMs as agents, which can be roughly categorized into two classes: (1) MACS via prior LLM selection. These approaches Chen et al. (2025); Lu et al. (2023); Shnitzer et al. (2023); Chen et al. (2024d) select appropriate LLMs before response generation by leveraging prior knowledge corresponding to LLMs, such as their performance on standard benchmarks Shnitzer et al. (2023) or model embeddings Chen et al. (2024d) obtained from training on specific datasets. By selecting the most suitable models for each given question in advance, these methods aim to increase the likelihood of generating high-quality responses and reduce computational overhead by avoiding the inference of unsuitable LLMs.
1932: (2) MACS via posterior response enhancement. These approaches Chen et al. (2024c, 2023a); Gui et al. (2024); Choudhury (2025) assess the quality of responses after each LLM has generated its answer, using inter- or intra-response criteria such as reward model scores Choudhury (2025), perplexity Mavromatis et al. (2024), or majority voting Li et al. (2024). Due to performing reasoning in advance, these methods provide a more accurate evaluation of response quality compared to relying solely on prior information.
1933: 
1934: However, both categories of methods encounter a dilemma when scaling the number of LLMs and tasks. For MACS based on prior LLM selection, they either require end-to-end router training Chen et al. (2024d) for each individual LLM, making it difficult to continuously incorporate new LLMs, or rely on limited and discrete capability labels Chen et al. (2025), which are insufficient for comprehensive analysis on a given question and hard to handle unseen questions. As a result, they exhibit suboptimal performance when facing
1935: unseen questions. For MACS based on posterior response enhancement, these methods typically rely on a single posterior criterion, which can introduce bias and lead to inaccurate quality assessments. Moreover, they mainly focus on selecting from an existing pool of responses, lacking the ability to generate new and diverse high-quality responses, limiting their performance upper bound. Besides the aforementioned limitations, current MACS methods often fail to effectively integrate prior and posterior methods in a coupled manner, which causes unfiltered low-quality responses as bottlenecks, which significantly hinders the overall performance and scalability of the collaboration system.
1936: 
1937: To enhance the
1938: scalability and break through the performance upper bound of MACS, we
1939: propose a novel framework called Scalable Multi-Agent Collaboration System (SMACS).
1940: Specifically, we first construct a question bank comprising diverse questions from multiple domains, along with an LLM pool containing plentiful heterogeneous LLMs. Each LLM in the pool is evaluated on the question bank to record its response to every question, representing its capacity across diverse domains. Further, inspired by Retrieval-Augmented Generation (RAG) Lewis et al. (2020); Chen et al. (2024a), we design a retrieval-based prior selection strategy: given any question, we retrieve similar questions from the question bank. A weighted score is computed for each LLM based on its performance on the retrieved questions, which serves as the prior information for selecting high-scoring LLMs.
1941: After that, we introduce exploration–exploitation-driven posterior enhancement: in the exploration phase, these responses are dropped via prior scores to form multiple answer subsets, which are independently aggregated by an LLM aggregator; in the exploitation phase, the aggregating responses are evaluated using a hybrid posterior scores of mean pairwise similarity and perplexity. The aggregated response with the highest score is selected as the final response.

full_text/2507.14200v1.txt:1976::1990 (0.4039)
1976: Emerging works have explored building MACS by employing diverse LLMs as agents, which can be roughly categorized into two classes: (1) MACS via prior LLM selection. These approaches Chen et al. (2025); Lu et al. (2023); Shnitzer et al. (2023); Chen et al. (2024d) select appropriate LLMs before response generation by leveraging prior knowledge corresponding to LLMs, such as their performance on standard benchmarks Shnitzer et al. (2023) or model embeddings Chen et al. (2024d) obtained from training on specific datasets. By selecting the most suitable models for each given question in advance, these methods aim to increase the likelihood of generating high-quality responses and reduce computational overhead by avoiding the inference of unsuitable LLMs.
1977: (2) MACS via posterior response enhancement. These approaches Chen et al. (2024c, 2023a); Gui et al. (2024); Choudhury (2025) assess the quality of responses after each LLM has generated its answer, using inter- or intra-response criteria such as reward model scores Choudhury (2025), perplexity Mavromatis et al. (2024), or majority voting Li et al. (2024). Due to performing reasoning in advance, these methods provide a more accurate evaluation of response quality compared to relying solely on prior information.
1978: 
1979: To answer this question, a mainstream method is to construct a multi-agent collaborative system (MACS). MACS aims to orchestrate interactions among multiple agents, enable information exchange and integration, and generate high-quality responses.
1980: Emerging works have explored building MACS by employing diverse LLMs as agents, which can be roughly categorized into two classes: (1) MACS via prior LLM selection. These approaches Chen et al. (2025); Lu et al. (2023); Shnitzer et al. (2023); Chen et al. (2024d) select appropriate LLMs before response generation by leveraging prior knowledge corresponding to LLMs, such as their performance on standard benchmarks Shnitzer et al. (2023) or model embeddings Chen et al. (2024d) obtained from training on specific datasets. By selecting the most suitable models for each given question in advance, these methods aim to increase the likelihood of generating high-quality responses and reduce computational overhead by avoiding the inference of unsuitable LLMs.
1981: (2) MACS via posterior response enhancement. These approaches Chen et al. (2024c, 2023a); Gui et al. (2024); Choudhury (2025) assess the quality of responses after each LLM has generated its answer, using inter- or intra-response criteria such as reward model scores Choudhury (2025), perplexity Mavromatis et al. (2024), or majority voting Li et al. (2024). Due to performing reasoning in advance, these methods provide a more accurate evaluation of response quality compared to relying solely on prior information.
1982: 
1983: However, both categories of methods encounter a dilemma when scaling the number of LLMs and tasks. For MACS based on prior LLM selection, they either require end-to-end router training Chen et al. (2024d) for each individual LLM, making it difficult to continuously incorporate new LLMs, or rely on limited and discrete capability labels Chen et al. (2025), which are insufficient for comprehensive analysis on a given question and hard to handle unseen questions. As a result, they exhibit suboptimal performance when facing
1984: unseen questions. For MACS based on posterior response enhancement, these methods typically rely on a single posterior criterion, which can introduce bias and lead to inaccurate quality assessments. Moreover, they mainly focus on selecting from an existing pool of responses, lacking the ability to generate new and diverse high-quality responses, limiting their performance upper bound. Besides the aforementioned limitations, current MACS methods often fail to effectively integrate prior and posterior methods in a coupled manner, which causes unfiltered low-quality responses as bottlenecks, which significantly hinders the overall performance and scalability of the collaboration system.
1985: 
1986: However, both categories of methods encounter a dilemma when scaling the number of LLMs and tasks. For MACS based on prior LLM selection, they either require end-to-end router training Chen et al. (2024d) for each individual LLM, making it difficult to continuously incorporate new LLMs, or rely on limited and discrete capability labels Chen et al. (2025), which are insufficient for comprehensive analysis on a given question and hard to handle unseen questions. As a result, they exhibit suboptimal performance when facing
1987: unseen questions. For MACS based on posterior response enhancement, these methods typically rely on a single posterior criterion, which can introduce bias and lead to inaccurate quality assessments. Moreover, they mainly focus on selecting from an existing pool of responses, lacking the ability to generate new and diverse high-quality responses, limiting their performance upper bound. Besides the aforementioned limitations, current MACS methods often fail to effectively integrate prior and posterior methods in a coupled manner, which causes unfiltered low-quality responses as bottlenecks, which significantly hinders the overall performance and scalability of the collaboration system.
1988: 
1989: To enhance the
1990: scalability and break through the performance upper bound of MACS, we

full_text/2507.14200v1.txt:1979::1993 (0.4039)
1979: To answer this question, a mainstream method is to construct a multi-agent collaborative system (MACS). MACS aims to orchestrate interactions among multiple agents, enable information exchange and integration, and generate high-quality responses.
1980: Emerging works have explored building MACS by employing diverse LLMs as agents, which can be roughly categorized into two classes: (1) MACS via prior LLM selection. These approaches Chen et al. (2025); Lu et al. (2023); Shnitzer et al. (2023); Chen et al. (2024d) select appropriate LLMs before response generation by leveraging prior knowledge corresponding to LLMs, such as their performance on standard benchmarks Shnitzer et al. (2023) or model embeddings Chen et al. (2024d) obtained from training on specific datasets. By selecting the most suitable models for each given question in advance, these methods aim to increase the likelihood of generating high-quality responses and reduce computational overhead by avoiding the inference of unsuitable LLMs.
1981: (2) MACS via posterior response enhancement. These approaches Chen et al. (2024c, 2023a); Gui et al. (2024); Choudhury (2025) assess the quality of responses after each LLM has generated its answer, using inter- or intra-response criteria such as reward model scores Choudhury (2025), perplexity Mavromatis et al. (2024), or majority voting Li et al. (2024). Due to performing reasoning in advance, these methods provide a more accurate evaluation of response quality compared to relying solely on prior information.
1982: 
1983: However, both categories of methods encounter a dilemma when scaling the number of LLMs and tasks. For MACS based on prior LLM selection, they either require end-to-end router training Chen et al. (2024d) for each individual LLM, making it difficult to continuously incorporate new LLMs, or rely on limited and discrete capability labels Chen et al. (2025), which are insufficient for comprehensive analysis on a given question and hard to handle unseen questions. As a result, they exhibit suboptimal performance when facing
1984: unseen questions. For MACS based on posterior response enhancement, these methods typically rely on a single posterior criterion, which can introduce bias and lead to inaccurate quality assessments. Moreover, they mainly focus on selecting from an existing pool of responses, lacking the ability to generate new and diverse high-quality responses, limiting their performance upper bound. Besides the aforementioned limitations, current MACS methods often fail to effectively integrate prior and posterior methods in a coupled manner, which causes unfiltered low-quality responses as bottlenecks, which significantly hinders the overall performance and scalability of the collaboration system.
1985: 
1986: However, both categories of methods encounter a dilemma when scaling the number of LLMs and tasks. For MACS based on prior LLM selection, they either require end-to-end router training Chen et al. (2024d) for each individual LLM, making it difficult to continuously incorporate new LLMs, or rely on limited and discrete capability labels Chen et al. (2025), which are insufficient for comprehensive analysis on a given question and hard to handle unseen questions. As a result, they exhibit suboptimal performance when facing
1987: unseen questions. For MACS based on posterior response enhancement, these methods typically rely on a single posterior criterion, which can introduce bias and lead to inaccurate quality assessments. Moreover, they mainly focus on selecting from an existing pool of responses, lacking the ability to generate new and diverse high-quality responses, limiting their performance upper bound. Besides the aforementioned limitations, current MACS methods often fail to effectively integrate prior and posterior methods in a coupled manner, which causes unfiltered low-quality responses as bottlenecks, which significantly hinders the overall performance and scalability of the collaboration system.
1988: 
1989: To enhance the
1990: scalability and break through the performance upper bound of MACS, we
1991: propose a novel framework called Scalable Multi-Agent Collaboration System (SMACS).
1992: Specifically, we first construct a question bank comprising diverse questions from multiple domains, along with an LLM pool containing plentiful heterogeneous LLMs. Each LLM in the pool is evaluated on the question bank to record its response to every question, representing its capacity across diverse domains. Further, inspired by Retrieval-Augmented Generation (RAG) Lewis et al. (2020); Chen et al. (2024a), we design a retrieval-based prior selection strategy: given any question, we retrieve similar questions from the question bank. A weighted score is computed for each LLM based on its performance on the retrieved questions, which serves as the prior information for selecting high-scoring LLMs.
1993: After that, we introduce exploration–exploitation-driven posterior enhancement: in the exploration phase, these responses are dropped via prior scores to form multiple answer subsets, which are independently aggregated by an LLM aggregator; in the exploitation phase, the aggregating responses are evaluated using a hybrid posterior scores of mean pairwise similarity and perplexity. The aggregated response with the highest score is selected as the final response.

full_text/2505.07796v2.txt:154::168 (0.4073)
 154: Figure 3: Using Eq. 4 to fit all PT and CPT loss curves with different LRS (WSD and Cosine).
 155: For Dp⁢tsubscript𝐷𝑝𝑡D_{pt}italic_D start_POSTSUBSCRIPT italic_p italic_t end_POSTSUBSCRIPT validation sets, all loss curves (b and e) are described by the same equation; similarly, for Dc⁢p⁢tsubscript𝐷𝑐𝑝𝑡D_{cpt}italic_D start_POSTSUBSCRIPT italic_c italic_p italic_t end_POSTSUBSCRIPT validation sets, all loss curves (c and f) follow the same equation.
 156: 
 157: 3.2 Distribution Shift Term
 158: 
 159: The distribution shift term describes the deviations from the hidden PT curve trained on Dp⁢tsubscript𝐷𝑝𝑡D_{pt}italic_D start_POSTSUBSCRIPT italic_p italic_t end_POSTSUBSCRIPT.
 160: This shift reflects the distributional distance between Dp⁢tsubscript𝐷𝑝𝑡D_{pt}italic_D start_POSTSUBSCRIPT italic_p italic_t end_POSTSUBSCRIPT and Dc⁢p⁢tsubscript𝐷𝑐𝑝𝑡D_{cpt}italic_D start_POSTSUBSCRIPT italic_c italic_p italic_t end_POSTSUBSCRIPT. Many studies  (Ibrahim et al., 2024; Wang et al., 2024; Parmar et al., 2024) have highlighted the impact of LRS at the CPT stage, implying that this shift should be also affected by the LRS.
 161: We first analyze the form of the distribution shift term with a constant LR to isolate the effects of LRS, then we incorporate the forward area into the equation to accurately describe the distribution shift term for different LRS.
 162: 
 163: Constant LRS.
 164: 
 165: We first use a constant LR in both PT and CPT phases.
 166: To study the relationship between distribution shift and the PT model state, we continually pre-train the model starting from different transfer points.
 167: As shown in Fig. 2, these distribution shift terms tend to overlap regardless of the transfer starting point.
 168: This overlap suggests that the distribution shift term is independent of transfer starting points or PT model checkpoints.

full_text/2505.07796v2.txt:1802::1816 (0.4073)
1802: Figure 3: Using Eq. 4 to fit all PT and CPT loss curves with different LRS (WSD and Cosine).
1803: For Dp⁢tsubscript𝐷𝑝𝑡D_{pt}italic_D start_POSTSUBSCRIPT italic_p italic_t end_POSTSUBSCRIPT validation sets, all loss curves (b and e) are described by the same equation; similarly, for Dc⁢p⁢tsubscript𝐷𝑐𝑝𝑡D_{cpt}italic_D start_POSTSUBSCRIPT italic_c italic_p italic_t end_POSTSUBSCRIPT validation sets, all loss curves (c and f) follow the same equation.
1804: 
1805: 3.2 Distribution Shift Term
1806: 
1807: The distribution shift term describes the deviations from the hidden PT curve trained on Dp⁢tsubscript𝐷𝑝𝑡D_{pt}italic_D start_POSTSUBSCRIPT italic_p italic_t end_POSTSUBSCRIPT.
1808: This shift reflects the distributional distance between Dp⁢tsubscript𝐷𝑝𝑡D_{pt}italic_D start_POSTSUBSCRIPT italic_p italic_t end_POSTSUBSCRIPT and Dc⁢p⁢tsubscript𝐷𝑐𝑝𝑡D_{cpt}italic_D start_POSTSUBSCRIPT italic_c italic_p italic_t end_POSTSUBSCRIPT. Many studies  (Ibrahim et al., 2024; Wang et al., 2024; Parmar et al., 2024) have highlighted the impact of LRS at the CPT stage, implying that this shift should be also affected by the LRS.
1809: We first analyze the form of the distribution shift term with a constant LR to isolate the effects of LRS, then we incorporate the forward area into the equation to accurately describe the distribution shift term for different LRS.
1810: 
1811: Constant LRS.
1812: 
1813: We first use a constant LR in both PT and CPT phases.
1814: To study the relationship between distribution shift and the PT model state, we continually pre-train the model starting from different transfer points.
1815: As shown in Fig. 2, these distribution shift terms tend to overlap regardless of the transfer starting point.
1816: This overlap suggests that the distribution shift term is independent of transfer starting points or PT model checkpoints.


```

</details>


---

### 5. Query: How does the performance of GPT-4o in long-context multimodal document understanding, as measured in WikiMixQA, compare with its performance in extracting statistical results for meta-analysis using customized prompts, as reported by Li et al.?

- **Query ID:** `synthesis_2`
- **Query Type:** Synthesis
- **Curated Source Files:** `full_text/2505.07796v2.txt, full_text/2506.15594v1.txt, full_text/2506.22309v1.txt, full_text/2507.15152v1.txt, full_text/2508.14302v1.txt, full_text/2508.15370v1.txt`

#### LLM Ground Truth Answer

> In the WikiMixQA benchmark, GPT-4o achieved 55.24% accuracy in the 'wikidoc' setting, which involves retrieving and reasoning over information from long Wikipedia document snapshots (averaging 24.18 pages and ~1815 textual tokens). This was the only model in that benchmark to exceed 50% accuracy in this long-context multimodal reasoning task. Conversely, for meta-analysis data extraction, Li et al. found that GPT-4o-mini (referred to as GPT) demonstrated a recall of 0.792 (79.2%) and precision of 0.840 (84.0%) for statistical results in MA1 when using customized prompts. However, its overall average recall for statistical results across all meta-analyses, even with customized prompts, was lower at 0.381, ranking third (lowest) among the models tested (Grok, Gemini). This indicates that while GPT-4o can achieve strong performance in specific long-context, structured extraction tasks when precisely guided by customized prompts, its general capability in statistical extraction can be inconsistent, and it tends to lag behind more advanced models like Gemini and Grok in broader data capture for this category.

**Source Document(s):** `full_text/2506.15594v1.txt, full_text/2507.15152v1.txt`

#### `search` Tool Performance

**Command Executed:**

```bash
search "How does the performance of GPT-4o in long-context multimodal document understanding, as measured in WikiMixQA, compare with its performance in extracting statistical results for meta-analysis using customized prompts, as reported by Li et al.?" full_text/*.txt --top-k 10 --n-lines 7
```

**Retrieval Precision:** `0.50`
**Retrieval Recall:** `0.50`

**Documents Returned by `search`:** `full_text/2507.15152v1.txt, full_text/2507.15882v2.txt`

#### LLM Search-Augmented Answer

> Based on the provided search results, a direct comparison of GPT-4o's performance in long-context multimodal document understanding using WikiMixQA with its performance in extracting statistical results for meta-analysis using customized prompts, as reported by Li et al., cannot be fully made due to insufficient information for the WikiMixQA scenario.
> 
> Regarding the extraction of statistical results for meta-analysis using customized prompts, the study by Li et al. (identified by the corresponding author L.Li5) evaluated GPT-4o-mini, along with other LLMs, for this task. The study found that all models, including GPT-4o-mini, demonstrated "high precision" but consistently suffered from "poor recall by omitting key information." However, they discovered that "customised prompts were the most effective, boosting recall by up to 15%" for these models.
> 
> For long-context multimodal document understanding, while the search results mention a benchmark dataset for "long context multimodal retrieval challenges" and discuss "significant disparity in VLMs’ performance between textual and visual information processing over extended contexts," noting that "accuracy of extracting multimodal information is notably lower compared to extracting pure textual information from document images," these observations are general for VLMs and do not provide specific performance metrics or results for GPT-4o (or GPT-4o-mini) on WikiMixQA. Therefore, there is no specific data in the provided snippets to directly compare GPT-4o's performance in this context against its performance in meta-analysis data extraction.

<details><summary>View Original `search` Tool Output</summary>

```
full_text/2507.15152v1.txt:26::40 (0.2628)
  26: 
  27: Meta-analysis is a gold standard in evidence-based medicine, combining quantitative findings from clinical trials to guide healthcare decisions [1, 2]. Accurate data extraction is a foundational component in meta-analyses, as it directly affects the quality of findings and validity of the conclusions. Traditionally, this step has been highly manual and resource-intensive [3], requiring multiple reviewers to identify and double-check key details from each study [4]. Errors at this stage are common and can compromise the accuracy of meta-analytic conclusions [5]. Furthermore, with the growing volume of the published research, the need for efficient, accurate and reliable automation methods capable of scalability, has become more critical [6].
  28: 
  29: Over the years, researchers have explored a range of automated data extraction approaches to alleviate the manual burden. Early efforts used rule-based systems with manually designed patterns to extract trial elements such as sample sizes and interventions [7, 8]. While these showed that automated extraction was possible, they were constrained by the variability of reports, making them challenging to maintain or expand. To overcome such drawbacks, classical machine learning and specialised natural language processing techniques [9, 10, 7, 11, 12] such as named entity recognition and supervised classification to extract PICO (Population, Intervention, Comparator, Outcome) elements are being employed. For example, BERT-based models, like those described by Mutinda et al. [13], offered better adaptability compared to rule-based systems. However, these earlier approaches needed annotated datasets [7, 12, 9], were often designed for narrow or specific objectives [9, 10], and struggled with complex full-text documents [7, 11, 12]. A recent literature review has noted that 84% of extraction methods focused on abstracts, with only 25% attempting to process full-text trial reports [14]. Furthermore, only a small proportion of projects produced widely accessible tools (approximately 8% of methods had publicly available implementations) [14], highlighting the difficulty of creating broadly applicable solutions. Despite these challenges, semi-automated tools like RobotReviewer [15] and AutoLit (https://about.nested-knowledge.com/) have emerged. RobotReviewer was among the first systems to address full-text data extraction and risk-of-bias assessment simultaneously. Though it aids reviewers by summarising participant details and methodological quality, it does not fully capture numerical outcomes essential for meta-analysis. AutoLit incorporates AI into the entire systematic review process, providing tools such as inclusion prediction and NLP-assisted data extraction. The platform’s value lies in its ability to streamline workflows, ensuring that extracted data flow directly into meta-analysis and visualisation components (the “Synthesis” module of the platform). Although AutoLit streamlines many aspects of the systematic review process, its outputs still require substantial human oversight [16]. This is evident when extracting complex or numerical data from tables [17].
  30: 
  31: More recently, large language models (LLMs) powered systems offer greater adaptability. Tools like MetaMate [18] employ LLMs in a structured extraction pipeline with verification steps, achieving strong accuracy for participant and intervention data. In controlled settings, MetaMate attained F1 scores similar to those of human coders, including accurately parsing numerical expressions. However, it has not yet addressed full outcome extraction and has primarily been evaluated in the educational domain. The advent of general LLMs (such as ChatGPT [19], Claude [20], and others) has introduced powerful new ways to automate data extraction. With LLMs’ ability to understand context and perform tasks without extensive training from scientific texts, researchers are currently evaluating LLMs both as independent extractors and within human-in-the-loop workflows [21, 18, 22, 23]. Studies show promising results: GPT-4 achieved 82% accuracy extracting trial characteristics in biomedical RCTs [24], and Claude successfully extracted binary outcome data with around 70–75% accuracy [23]. Konet et.al showed Claude 2 can achieve 96.2% data elements correctness in 10 PDF articles [22]. However, their application to structured data extraction for meta-analysis has yet to be widely tested at the scale and complexity required for real-world use involving heterogeneous document types, especially when extracting detailed statistical information needed for meta-analyses.
  32: 
  33: This study investigates the extent to which current LLMs can reliably extract the structured data from raw scientific papers required for automated meta-analysis (AMA), and further examines how extraction demands differ across statistical results, risk-of-bias assessments, and study-level categories of data, as well as how these data types impact extraction performance. We sought answers to these goals across three heterogeneous medical fields, namely, hypertension, diabetes, and orthopaedics, maximising the generalisability of our research. In our work, we evaluated the data extraction performance of three advanced models (Gemini-2.0-Flash, Grok-3, and GPT-4o-mini) against a human-annotated ground truth data, while exploring a variety of prompting and model-output aggregation strategies. Given the research momentum towards automating all parts of the meta-analysis process, our findings shed important light on the performance profile and the existing capabilities and limitations of current LLMs in real-world data extraction tasks for evidence synthesis purposes. Therefore, the contributions of this study are as follows:
  34: 
  35: •
  36: 
  37: Comprehensive feasibility assessment: We provide the first in-depth benchmark of LLMs for full-text data extraction in meta-analysis across multiple clinical domains, information types, and task structures.
  38: 
  39: •
  40: 

full_text/2507.15152v1.txt:2503::2517 (0.2628)
2503: 
2504: Meta-analysis is a gold standard in evidence-based medicine, combining quantitative findings from clinical trials to guide healthcare decisions [1, 2]. Accurate data extraction is a foundational component in meta-analyses, as it directly affects the quality of findings and validity of the conclusions. Traditionally, this step has been highly manual and resource-intensive [3], requiring multiple reviewers to identify and double-check key details from each study [4]. Errors at this stage are common and can compromise the accuracy of meta-analytic conclusions [5]. Furthermore, with the growing volume of the published research, the need for efficient, accurate and reliable automation methods capable of scalability, has become more critical [6].
2505: 
2506: Over the years, researchers have explored a range of automated data extraction approaches to alleviate the manual burden. Early efforts used rule-based systems with manually designed patterns to extract trial elements such as sample sizes and interventions [7, 8]. While these showed that automated extraction was possible, they were constrained by the variability of reports, making them challenging to maintain or expand. To overcome such drawbacks, classical machine learning and specialised natural language processing techniques [9, 10, 7, 11, 12] such as named entity recognition and supervised classification to extract PICO (Population, Intervention, Comparator, Outcome) elements are being employed. For example, BERT-based models, like those described by Mutinda et al. [13], offered better adaptability compared to rule-based systems. However, these earlier approaches needed annotated datasets [7, 12, 9], were often designed for narrow or specific objectives [9, 10], and struggled with complex full-text documents [7, 11, 12]. A recent literature review has noted that 84% of extraction methods focused on abstracts, with only 25% attempting to process full-text trial reports [14]. Furthermore, only a small proportion of projects produced widely accessible tools (approximately 8% of methods had publicly available implementations) [14], highlighting the difficulty of creating broadly applicable solutions. Despite these challenges, semi-automated tools like RobotReviewer [15] and AutoLit (https://about.nested-knowledge.com/) have emerged. RobotReviewer was among the first systems to address full-text data extraction and risk-of-bias assessment simultaneously. Though it aids reviewers by summarising participant details and methodological quality, it does not fully capture numerical outcomes essential for meta-analysis. AutoLit incorporates AI into the entire systematic review process, providing tools such as inclusion prediction and NLP-assisted data extraction. The platform’s value lies in its ability to streamline workflows, ensuring that extracted data flow directly into meta-analysis and visualisation components (the “Synthesis” module of the platform). Although AutoLit streamlines many aspects of the systematic review process, its outputs still require substantial human oversight [16]. This is evident when extracting complex or numerical data from tables [17].
2507: 
2508: More recently, large language models (LLMs) powered systems offer greater adaptability. Tools like MetaMate [18] employ LLMs in a structured extraction pipeline with verification steps, achieving strong accuracy for participant and intervention data. In controlled settings, MetaMate attained F1 scores similar to those of human coders, including accurately parsing numerical expressions. However, it has not yet addressed full outcome extraction and has primarily been evaluated in the educational domain. The advent of general LLMs (such as ChatGPT [19], Claude [20], and others) has introduced powerful new ways to automate data extraction. With LLMs’ ability to understand context and perform tasks without extensive training from scientific texts, researchers are currently evaluating LLMs both as independent extractors and within human-in-the-loop workflows [21, 18, 22, 23]. Studies show promising results: GPT-4 achieved 82% accuracy extracting trial characteristics in biomedical RCTs [24], and Claude successfully extracted binary outcome data with around 70–75% accuracy [23]. Konet et.al showed Claude 2 can achieve 96.2% data elements correctness in 10 PDF articles [22]. However, their application to structured data extraction for meta-analysis has yet to be widely tested at the scale and complexity required for real-world use involving heterogeneous document types, especially when extracting detailed statistical information needed for meta-analyses.
2509: 
2510: This study investigates the extent to which current LLMs can reliably extract the structured data from raw scientific papers required for automated meta-analysis (AMA), and further examines how extraction demands differ across statistical results, risk-of-bias assessments, and study-level categories of data, as well as how these data types impact extraction performance. We sought answers to these goals across three heterogeneous medical fields, namely, hypertension, diabetes, and orthopaedics, maximising the generalisability of our research. In our work, we evaluated the data extraction performance of three advanced models (Gemini-2.0-Flash, Grok-3, and GPT-4o-mini) against a human-annotated ground truth data, while exploring a variety of prompting and model-output aggregation strategies. Given the research momentum towards automating all parts of the meta-analysis process, our findings shed important light on the performance profile and the existing capabilities and limitations of current LLMs in real-world data extraction tasks for evidence synthesis purposes. Therefore, the contributions of this study are as follows:
2511: 
2512: •
2513: 
2514: Comprehensive feasibility assessment: We provide the first in-depth benchmark of LLMs for full-text data extraction in meta-analysis across multiple clinical domains, information types, and task structures.
2515: 
2516: •
2517: 

full_text/2507.15152v1.txt:2535::2549 (0.2628)
2535: 
2536: Over the years, researchers have explored a range of automated data extraction approaches to alleviate the manual burden. Early efforts used rule-based systems with manually designed patterns to extract trial elements such as sample sizes and interventions [7, 8]. While these showed that automated extraction was possible, they were constrained by the variability of reports, making them challenging to maintain or expand. To overcome such drawbacks, classical machine learning and specialised natural language processing techniques [9, 10, 7, 11, 12] such as named entity recognition and supervised classification to extract PICO (Population, Intervention, Comparator, Outcome) elements are being employed. For example, BERT-based models, like those described by Mutinda et al. [13], offered better adaptability compared to rule-based systems. However, these earlier approaches needed annotated datasets [7, 12, 9], were often designed for narrow or specific objectives [9, 10], and struggled with complex full-text documents [7, 11, 12]. A recent literature review has noted that 84% of extraction methods focused on abstracts, with only 25% attempting to process full-text trial reports [14]. Furthermore, only a small proportion of projects produced widely accessible tools (approximately 8% of methods had publicly available implementations) [14], highlighting the difficulty of creating broadly applicable solutions. Despite these challenges, semi-automated tools like RobotReviewer [15] and AutoLit (https://about.nested-knowledge.com/) have emerged. RobotReviewer was among the first systems to address full-text data extraction and risk-of-bias assessment simultaneously. Though it aids reviewers by summarising participant details and methodological quality, it does not fully capture numerical outcomes essential for meta-analysis. AutoLit incorporates AI into the entire systematic review process, providing tools such as inclusion prediction and NLP-assisted data extraction. The platform’s value lies in its ability to streamline workflows, ensuring that extracted data flow directly into meta-analysis and visualisation components (the “Synthesis” module of the platform). Although AutoLit streamlines many aspects of the systematic review process, its outputs still require substantial human oversight [16]. This is evident when extracting complex or numerical data from tables [17].
2537: 
2538: More recently, large language models (LLMs) powered systems offer greater adaptability. Tools like MetaMate [18] employ LLMs in a structured extraction pipeline with verification steps, achieving strong accuracy for participant and intervention data. In controlled settings, MetaMate attained F1 scores similar to those of human coders, including accurately parsing numerical expressions. However, it has not yet addressed full outcome extraction and has primarily been evaluated in the educational domain. The advent of general LLMs (such as ChatGPT [19], Claude [20], and others) has introduced powerful new ways to automate data extraction. With LLMs’ ability to understand context and perform tasks without extensive training from scientific texts, researchers are currently evaluating LLMs both as independent extractors and within human-in-the-loop workflows [21, 18, 22, 23]. Studies show promising results: GPT-4 achieved 82% accuracy extracting trial characteristics in biomedical RCTs [24], and Claude successfully extracted binary outcome data with around 70–75% accuracy [23]. Konet et.al showed Claude 2 can achieve 96.2% data elements correctness in 10 PDF articles [22]. However, their application to structured data extraction for meta-analysis has yet to be widely tested at the scale and complexity required for real-world use involving heterogeneous document types, especially when extracting detailed statistical information needed for meta-analyses.
2539: 
2540: More recently, large language models (LLMs) powered systems offer greater adaptability. Tools like MetaMate [18] employ LLMs in a structured extraction pipeline with verification steps, achieving strong accuracy for participant and intervention data. In controlled settings, MetaMate attained F1 scores similar to those of human coders, including accurately parsing numerical expressions. However, it has not yet addressed full outcome extraction and has primarily been evaluated in the educational domain. The advent of general LLMs (such as ChatGPT [19], Claude [20], and others) has introduced powerful new ways to automate data extraction. With LLMs’ ability to understand context and perform tasks without extensive training from scientific texts, researchers are currently evaluating LLMs both as independent extractors and within human-in-the-loop workflows [21, 18, 22, 23]. Studies show promising results: GPT-4 achieved 82% accuracy extracting trial characteristics in biomedical RCTs [24], and Claude successfully extracted binary outcome data with around 70–75% accuracy [23]. Konet et.al showed Claude 2 can achieve 96.2% data elements correctness in 10 PDF articles [22]. However, their application to structured data extraction for meta-analysis has yet to be widely tested at the scale and complexity required for real-world use involving heterogeneous document types, especially when extracting detailed statistical information needed for meta-analyses.
2541: 
2542: This study investigates the extent to which current LLMs can reliably extract the structured data from raw scientific papers required for automated meta-analysis (AMA), and further examines how extraction demands differ across statistical results, risk-of-bias assessments, and study-level categories of data, as well as how these data types impact extraction performance. We sought answers to these goals across three heterogeneous medical fields, namely, hypertension, diabetes, and orthopaedics, maximising the generalisability of our research. In our work, we evaluated the data extraction performance of three advanced models (Gemini-2.0-Flash, Grok-3, and GPT-4o-mini) against a human-annotated ground truth data, while exploring a variety of prompting and model-output aggregation strategies. Given the research momentum towards automating all parts of the meta-analysis process, our findings shed important light on the performance profile and the existing capabilities and limitations of current LLMs in real-world data extraction tasks for evidence synthesis purposes. Therefore, the contributions of this study are as follows:
2543: 
2544: •
2545: 
2546: Comprehensive feasibility assessment: We provide the first in-depth benchmark of LLMs for full-text data extraction in meta-analysis across multiple clinical domains, information types, and task structures.
2547: 
2548: •
2549: 

full_text/2507.15152v1.txt:2553::2567 (0.2628)
2553: 
2554: Methodologically robust evaluation protocol: We design a role-separated evaluation process that prevents LLMs from scoring their own outputs, using blinded, model-agnostic comparisons to ensure reliable and unbiased assessment of extraction quality.
2555: 
2556: •
2557: 
2558: Task-specific automation guideline: Drawing on empirical performance patterns, we propose a three-tier classification of meta-analysis information types based on their suitability for automation and tolerance for error, offering practical guidelines on when to automate, when to review, and when human judgment remains essential.
2559: 
2560: This study investigates the extent to which current LLMs can reliably extract the structured data from raw scientific papers required for automated meta-analysis (AMA), and further examines how extraction demands differ across statistical results, risk-of-bias assessments, and study-level categories of data, as well as how these data types impact extraction performance. We sought answers to these goals across three heterogeneous medical fields, namely, hypertension, diabetes, and orthopaedics, maximising the generalisability of our research. In our work, we evaluated the data extraction performance of three advanced models (Gemini-2.0-Flash, Grok-3, and GPT-4o-mini) against a human-annotated ground truth data, while exploring a variety of prompting and model-output aggregation strategies. Given the research momentum towards automating all parts of the meta-analysis process, our findings shed important light on the performance profile and the existing capabilities and limitations of current LLMs in real-world data extraction tasks for evidence synthesis purposes. Therefore, the contributions of this study are as follows:
2561: 
2562: Comprehensive feasibility assessment: We provide the first in-depth benchmark of LLMs for full-text data extraction in meta-analysis across multiple clinical domains, information types, and task structures.
2563: 
2564: Comprehensive feasibility assessment: We provide the first in-depth benchmark of LLMs for full-text data extraction in meta-analysis across multiple clinical domains, information types, and task structures.
2565: 
2566: Modular performance optimisation: We demonstrate that prompt specialisation and model output aggregation can yield distinct and complementary gains, establishing a modular strategy for improving extraction quality across heterogeneous AMA tasks.
2567: 

full_text/2507.15882v2.txt:539::553 (0.2758)
 539: 
 540: 5.1 Document Haystack Latency
 541: 
 542: While our study emphasizes accuracy measurements, researchers could utilize our dataset to evaluate the latency characteristics of different VLMs in processing long documents. Such analysis would provide valuable insights into the computational efficiency and practical deployability of these models, particularly important for real-world applications where response time is crucial. This analysis could also reveal important trade-offs between model accuracy and response time, helping practitioners make informed decisions based on their specific application requirements.
 543: 
 544: 5.2 Advancing VLMs’ Long Context Processing
 545: 
 546: Our benchmark results reveal a significant disparity in VLMs’ performance between textual and visual information processing over extended contexts. While models demonstrate robust capabilities in handling long context textual information, their performance in identifying and extracting image-based information deteriorates as document length increases. Additionally, the accuracy of extracting multimodal information is notably lower compared to extracting pure textual information from document images. These performance gaps highlight a critical area for improvement in next-generation VLMs.
 547: 
 548: The challenge likely stems from the increased complexity of maintaining and processing rich visual information over longer sequences, as opposed to textual information. Future research should focus on developing more efficient architectures, training approaches, and inference algorithms specifically designed to maintain visual context over extended sequences. This might include novel attention mechanisms, better visual tokenization strategies, or more sophisticated methods for managing the interaction between textual and visual modalities in long documents. Addressing these limitations is crucial as real-world applications often require processing lengthy documents containing both text and images, from technical manuals to medical records.
 549: 
 550: 5.3 Extended Analysis Framework
 551: 
 552: While our primary contribution is a benchmark dataset for long context multimodal retrieval challenges, we recognize the importance of enabling more fine-grained analysis tasks. To facilitate this, our dataset release includes comprehensive metadata for each needle, comprising: (1) page location within the document, (2) precise X-Y coordinates on the page, (3) image size, (4) color specifications, and (5) font type and size.
 553: 

full_text/2507.15882v2.txt:1896::1910 (0.2758)
1896: 
1897: 5.1 Document Haystack Latency
1898: 
1899: While our study emphasizes accuracy measurements, researchers could utilize our dataset to evaluate the latency characteristics of different VLMs in processing long documents. Such analysis would provide valuable insights into the computational efficiency and practical deployability of these models, particularly important for real-world applications where response time is crucial. This analysis could also reveal important trade-offs between model accuracy and response time, helping practitioners make informed decisions based on their specific application requirements.
1900: 
1901: 5.2 Advancing VLMs’ Long Context Processing
1902: 
1903: Our benchmark results reveal a significant disparity in VLMs’ performance between textual and visual information processing over extended contexts. While models demonstrate robust capabilities in handling long context textual information, their performance in identifying and extracting image-based information deteriorates as document length increases. Additionally, the accuracy of extracting multimodal information is notably lower compared to extracting pure textual information from document images. These performance gaps highlight a critical area for improvement in next-generation VLMs.
1904: 
1905: The challenge likely stems from the increased complexity of maintaining and processing rich visual information over longer sequences, as opposed to textual information. Future research should focus on developing more efficient architectures, training approaches, and inference algorithms specifically designed to maintain visual context over extended sequences. This might include novel attention mechanisms, better visual tokenization strategies, or more sophisticated methods for managing the interaction between textual and visual modalities in long documents. Addressing these limitations is crucial as real-world applications often require processing lengthy documents containing both text and images, from technical manuals to medical records.
1906: 
1907: 5.3 Extended Analysis Framework
1908: 
1909: While our primary contribution is a benchmark dataset for long context multimodal retrieval challenges, we recognize the importance of enabling more fine-grained analysis tasks. To facilitate this, our dataset release includes comprehensive metadata for each needle, comprising: (1) page location within the document, (2) precise X-Y coordinates on the page, (3) image size, (4) color specifications, and (5) font type and size.
1910: 

full_text/2507.15882v2.txt:1920::1934 (0.2758)
1920: 
1921: While our study emphasizes accuracy measurements, researchers could utilize our dataset to evaluate the latency characteristics of different VLMs in processing long documents. Such analysis would provide valuable insights into the computational efficiency and practical deployability of these models, particularly important for real-world applications where response time is crucial. This analysis could also reveal important trade-offs between model accuracy and response time, helping practitioners make informed decisions based on their specific application requirements.
1922: 
1923: While our study emphasizes accuracy measurements, researchers could utilize our dataset to evaluate the latency characteristics of different VLMs in processing long documents. Such analysis would provide valuable insights into the computational efficiency and practical deployability of these models, particularly important for real-world applications where response time is crucial. This analysis could also reveal important trade-offs between model accuracy and response time, helping practitioners make informed decisions based on their specific application requirements.
1924: 
1925: 5.2 Advancing VLMs’ Long Context Processing
1926: 
1927: Our benchmark results reveal a significant disparity in VLMs’ performance between textual and visual information processing over extended contexts. While models demonstrate robust capabilities in handling long context textual information, their performance in identifying and extracting image-based information deteriorates as document length increases. Additionally, the accuracy of extracting multimodal information is notably lower compared to extracting pure textual information from document images. These performance gaps highlight a critical area for improvement in next-generation VLMs.
1928: 
1929: The challenge likely stems from the increased complexity of maintaining and processing rich visual information over longer sequences, as opposed to textual information. Future research should focus on developing more efficient architectures, training approaches, and inference algorithms specifically designed to maintain visual context over extended sequences. This might include novel attention mechanisms, better visual tokenization strategies, or more sophisticated methods for managing the interaction between textual and visual modalities in long documents. Addressing these limitations is crucial as real-world applications often require processing lengthy documents containing both text and images, from technical manuals to medical records.
1930: 
1931: 5.2 ADVANCING VLMS’ LONG CONTEXT PROCESSING
1932: 
1933: Our benchmark results reveal a significant disparity in VLMs’ performance between textual and visual information processing over extended contexts. While models demonstrate robust capabilities in handling long context textual information, their performance in identifying and extracting image-based information deteriorates as document length increases. Additionally, the accuracy of extracting multimodal information is notably lower compared to extracting pure textual information from document images. These performance gaps highlight a critical area for improvement in next-generation VLMs.
1934: 

full_text/2507.15882v2.txt:1926::1940 (0.2758)
1926: 
1927: Our benchmark results reveal a significant disparity in VLMs’ performance between textual and visual information processing over extended contexts. While models demonstrate robust capabilities in handling long context textual information, their performance in identifying and extracting image-based information deteriorates as document length increases. Additionally, the accuracy of extracting multimodal information is notably lower compared to extracting pure textual information from document images. These performance gaps highlight a critical area for improvement in next-generation VLMs.
1928: 
1929: The challenge likely stems from the increased complexity of maintaining and processing rich visual information over longer sequences, as opposed to textual information. Future research should focus on developing more efficient architectures, training approaches, and inference algorithms specifically designed to maintain visual context over extended sequences. This might include novel attention mechanisms, better visual tokenization strategies, or more sophisticated methods for managing the interaction between textual and visual modalities in long documents. Addressing these limitations is crucial as real-world applications often require processing lengthy documents containing both text and images, from technical manuals to medical records.
1930: 
1931: 5.2 ADVANCING VLMS’ LONG CONTEXT PROCESSING
1932: 
1933: Our benchmark results reveal a significant disparity in VLMs’ performance between textual and visual information processing over extended contexts. While models demonstrate robust capabilities in handling long context textual information, their performance in identifying and extracting image-based information deteriorates as document length increases. Additionally, the accuracy of extracting multimodal information is notably lower compared to extracting pure textual information from document images. These performance gaps highlight a critical area for improvement in next-generation VLMs.
1934: 
1935: Our benchmark results reveal a significant disparity in VLMs’ performance between textual and visual information processing over extended contexts. While models demonstrate robust capabilities in handling long context textual information, their performance in identifying and extracting image-based information deteriorates as document length increases. Additionally, the accuracy of extracting multimodal information is notably lower compared to extracting pure textual information from document images. These performance gaps highlight a critical area for improvement in next-generation VLMs.
1936: 
1937: The challenge likely stems from the increased complexity of maintaining and processing rich visual information over longer sequences, as opposed to textual information. Future research should focus on developing more efficient architectures, training approaches, and inference algorithms specifically designed to maintain visual context over extended sequences. This might include novel attention mechanisms, better visual tokenization strategies, or more sophisticated methods for managing the interaction between textual and visual modalities in long documents. Addressing these limitations is crucial as real-world applications often require processing lengthy documents containing both text and images, from technical manuals to medical records.
1938: 
1939: The challenge likely stems from the increased complexity of maintaining and processing rich visual information over longer sequences, as opposed to textual information. Future research should focus on developing more efficient architectures, training approaches, and inference algorithms specifically designed to maintain visual context over extended sequences. This might include novel attention mechanisms, better visual tokenization strategies, or more sophisticated methods for managing the interaction between textual and visual modalities in long documents. Addressing these limitations is crucial as real-world applications often require processing lengthy documents containing both text and images, from technical manuals to medical records.
1940: 

full_text/2507.15882v2.txt:1928::1942 (0.2758)
1928: 
1929: The challenge likely stems from the increased complexity of maintaining and processing rich visual information over longer sequences, as opposed to textual information. Future research should focus on developing more efficient architectures, training approaches, and inference algorithms specifically designed to maintain visual context over extended sequences. This might include novel attention mechanisms, better visual tokenization strategies, or more sophisticated methods for managing the interaction between textual and visual modalities in long documents. Addressing these limitations is crucial as real-world applications often require processing lengthy documents containing both text and images, from technical manuals to medical records.
1930: 
1931: 5.2 ADVANCING VLMS’ LONG CONTEXT PROCESSING
1932: 
1933: Our benchmark results reveal a significant disparity in VLMs’ performance between textual and visual information processing over extended contexts. While models demonstrate robust capabilities in handling long context textual information, their performance in identifying and extracting image-based information deteriorates as document length increases. Additionally, the accuracy of extracting multimodal information is notably lower compared to extracting pure textual information from document images. These performance gaps highlight a critical area for improvement in next-generation VLMs.
1934: 
1935: Our benchmark results reveal a significant disparity in VLMs’ performance between textual and visual information processing over extended contexts. While models demonstrate robust capabilities in handling long context textual information, their performance in identifying and extracting image-based information deteriorates as document length increases. Additionally, the accuracy of extracting multimodal information is notably lower compared to extracting pure textual information from document images. These performance gaps highlight a critical area for improvement in next-generation VLMs.
1936: 
1937: The challenge likely stems from the increased complexity of maintaining and processing rich visual information over longer sequences, as opposed to textual information. Future research should focus on developing more efficient architectures, training approaches, and inference algorithms specifically designed to maintain visual context over extended sequences. This might include novel attention mechanisms, better visual tokenization strategies, or more sophisticated methods for managing the interaction between textual and visual modalities in long documents. Addressing these limitations is crucial as real-world applications often require processing lengthy documents containing both text and images, from technical manuals to medical records.
1938: 
1939: The challenge likely stems from the increased complexity of maintaining and processing rich visual information over longer sequences, as opposed to textual information. Future research should focus on developing more efficient architectures, training approaches, and inference algorithms specifically designed to maintain visual context over extended sequences. This might include novel attention mechanisms, better visual tokenization strategies, or more sophisticated methods for managing the interaction between textual and visual modalities in long documents. Addressing these limitations is crucial as real-world applications often require processing lengthy documents containing both text and images, from technical manuals to medical records.
1940: 
1941: 5.3 Extended Analysis Framework
1942: 

full_text/2507.15152v1.txt:14::28 (0.2817)
  14: School of Mathematical and Computational Sciences
  15: Massey University
  16: Auckland, New Zealand 
  17: 
  18: Corresponding author: L.Li5@massey.ac.nz
  19: 
  20: Abstract
  21: Automating data extraction from full-text randomised controlled trials (RCTs) for meta-analysis remains a significant challenge. This study evaluates the practical performance of three LLMs (Gemini-2.0-flash, Grok-3, GPT-4o-mini) across tasks involving statistical results, risk-of-bias assessments, and study-level characteristics in three medical domains: hypertension, diabetes, and orthopaedics. We tested four distinct prompting strategies (basic prompting, self-reflective prompting, model ensemble, and customised prompts) to determine how to improve extraction quality. All models demonstrate high precision but consistently suffer from poor recall by omitting key information. We found that customised prompts were the most effective, boosting recall by up to 15%. Based on this analysis, we propose a three-tiered set of guidelines for using LLMs in data extraction, matching data types to appropriate levels of automation based on task complexity and risk. Our study offers practical advice for automating data extraction in real-world meta-analyses, balancing LLM efficiency with expert oversight through targeted, task-specific automation.
  22: 
  23: Keywords Automated Meta-analysis, Large Language Models (LLMs), Data Extraction, Prompt Engineering, LLM Performance Evaluation, Human-in-the-loop, Evidence Synthesis
  24: 
  25: 1 Introduction
  26: 
  27: Meta-analysis is a gold standard in evidence-based medicine, combining quantitative findings from clinical trials to guide healthcare decisions [1, 2]. Accurate data extraction is a foundational component in meta-analyses, as it directly affects the quality of findings and validity of the conclusions. Traditionally, this step has been highly manual and resource-intensive [3], requiring multiple reviewers to identify and double-check key details from each study [4]. Errors at this stage are common and can compromise the accuracy of meta-analytic conclusions [5]. Furthermore, with the growing volume of the published research, the need for efficient, accurate and reliable automation methods capable of scalability, has become more critical [6].
  28: 


```

</details>


---

### 6. Query: How do Wang et al.'s proposed solutions for addressing unknown pre-training dataset distributions for open-source LLMs relate to the methods employed by Foroutan et al. for generating table and image descriptions in the WikiMixQA benchmark?

- **Query ID:** `synthesis_3`
- **Query Type:** Synthesis
- **Curated Source Files:** `full_text/2505.07796v2.txt, full_text/2506.15594v1.txt, full_text/2506.22309v1.txt, full_text/2507.15152v1.txt, full_text/2508.14302v1.txt, full_text/2508.15370v1.txt`

#### LLM Ground Truth Answer

> Wang et al. address unknown pre-training dataset distributions for open-source LLMs by using an open-source Common Crawl dataset as a *proxy* distribution. They also treat parameters like the PT forward area (S1pt) as unknowns to be fitted from observed loss values, and assume a zero final LR for open-source models to compute CPT annealing area (S2cpt). Foroutan et al., in creating WikiMixQA, employ existing LLMs (specifically Llama-3-8B-Instruct and GPT-4-turbo) to *generate textual descriptions* for tables (from raw HTML) and to *confirm and extract key information* from images identified as charts. The commonality is the reliance on existing LLMs to infer, approximate, or generate structured information when explicit data or metadata about the source content is unavailable. Wang et al. use LLMs to fill gaps in system-level parameters for learning dynamics, while Foroutan et al. use them to create semantic metadata (descriptions) for multimodal content to facilitate question generation and similarity matching.

**Source Document(s):** `full_text/2505.07796v2.txt, full_text/2506.15594v1.txt`

#### `search` Tool Performance

**Command Executed:**

```bash
search "How do Wang et al.'s proposed solutions for addressing unknown pre-training dataset distributions for open-source LLMs relate to the methods employed by Foroutan et al. for generating table and image descriptions in the WikiMixQA benchmark?" full_text/*.txt --top-k 10 --n-lines 7
```

**Retrieval Precision:** `0.00`
**Retrieval Recall:** `0.00`

**Documents Returned by `search`:** `full_text/2506.08771v1.txt, full_text/2507.09531v1.txt, full_text/2507.19526v1.txt`

#### LLM Search-Augmented Answer

> The provided search tool output does not contain sufficient information to answer the research question. Specifically, the snippets do not mention "Wang et al.'s proposed solutions for addressing unknown pre-training dataset distributions for open-source LLMs" or any specific solutions by them regarding this problem. Furthermore, there is no mention of "Foroutan et al." or their methods for generating table and image descriptions in the "WikiMixQA benchmark." Therefore, a comparison or relation between these two topics cannot be established from the given text.

<details><summary>View Original `search` Tool Output</summary>

```
full_text/2507.19526v1.txt:24::38 (0.2777)
  24: Singapore Management UniversitySingaporeSingapore
  25: 
  26: yfang@smu.edu.sg
  27: 
  28: (2025)
  29: 
  30: Abstract.
  31: Text-attributed graphs (TAGs) have emerged as a powerful representation for modeling complex relationships across diverse domains. With the rise of large language models (LLMs), there is growing interest in leveraging their capabilities for graph learning. However, current approaches face significant challenges in embedding structural information into LLM-compatible formats, requiring either computationally expensive alignment mechanisms or manual graph verbalization techniques that often lose critical structural details. Moreover, these methods typically require labeled data from source domains for effective transfer learning, significantly constraining their adaptability. We propose STAG, a novel self-supervised framework that directly quantizes graph structural information into discrete tokens using a frozen codebook. Unlike traditional quantization approaches, our method employs soft assignment and KL divergence guided quantization to address the unique challenges of graph data, which lacks natural tokenization structures. Our framework enables both LLM-based and traditional learning approaches, supporting true zero-shot transfer learning without requiring labeled data even in the source domain. Extensive experiments demonstrate state-of-the-art performance across multiple node classification benchmarks while maintaining compatibility with different LLM architectures, offering an elegant solution to bridging graph learning with LLMs.
  32: 
  33: text-attributed graphs, large language models, few-shot, zero-shot, graph transfer learning
  34: 
  35: ††journalyear: 2025††copyright: cc††conference: Proceedings of the 31st ACM SIGKDD Conference on
  36: Knowledge Discovery and Data Mining V.2; August 3–7, 2025; Toronto, ON,
  37: Canada††booktitle: Proceedings of the 31st ACM SIGKDD Conference on Knowledge
  38: Discovery and Data Mining V.2 (KDD ’25), August 3–7, 2025, Toronto, ON,

full_text/2507.19526v1.txt:2023::2037 (0.2777)
2023: Singapore Management UniversitySingaporeSingapore
2024: 
2025: yfang@smu.edu.sg
2026: 
2027: (2025)
2028: 
2029: Abstract.
2030: Text-attributed graphs (TAGs) have emerged as a powerful representation for modeling complex relationships across diverse domains. With the rise of large language models (LLMs), there is growing interest in leveraging their capabilities for graph learning. However, current approaches face significant challenges in embedding structural information into LLM-compatible formats, requiring either computationally expensive alignment mechanisms or manual graph verbalization techniques that often lose critical structural details. Moreover, these methods typically require labeled data from source domains for effective transfer learning, significantly constraining their adaptability. We propose STAG, a novel self-supervised framework that directly quantizes graph structural information into discrete tokens using a frozen codebook. Unlike traditional quantization approaches, our method employs soft assignment and KL divergence guided quantization to address the unique challenges of graph data, which lacks natural tokenization structures. Our framework enables both LLM-based and traditional learning approaches, supporting true zero-shot transfer learning without requiring labeled data even in the source domain. Extensive experiments demonstrate state-of-the-art performance across multiple node classification benchmarks while maintaining compatibility with different LLM architectures, offering an elegant solution to bridging graph learning with LLMs.
2031: 
2032: ABSTRACT.
2033: 
2034: Text-attributed graphs (TAGs) have emerged as a powerful representation for modeling complex relationships across diverse domains. With the rise of large language models (LLMs), there is growing interest in leveraging their capabilities for graph learning. However, current approaches face significant challenges in embedding structural information into LLM-compatible formats, requiring either computationally expensive alignment mechanisms or manual graph verbalization techniques that often lose critical structural details. Moreover, these methods typically require labeled data from source domains for effective transfer learning, significantly constraining their adaptability. We propose STAG, a novel self-supervised framework that directly quantizes graph structural information into discrete tokens using a frozen codebook. Unlike traditional quantization approaches, our method employs soft assignment and KL divergence guided quantization to address the unique challenges of graph data, which lacks natural tokenization structures. Our framework enables both LLM-based and traditional learning approaches, supporting true zero-shot transfer learning without requiring labeled data even in the source domain. Extensive experiments demonstrate state-of-the-art performance across multiple node classification benchmarks while maintaining compatibility with different LLM architectures, offering an elegant solution to bridging graph learning with LLMs.
2035: 
2036: text-attributed graphs, large language models, few-shot, zero-shot, graph transfer learning
2037: 

full_text/2507.19526v1.txt:2027::2041 (0.2777)
2027: (2025)
2028: 
2029: Abstract.
2030: Text-attributed graphs (TAGs) have emerged as a powerful representation for modeling complex relationships across diverse domains. With the rise of large language models (LLMs), there is growing interest in leveraging their capabilities for graph learning. However, current approaches face significant challenges in embedding structural information into LLM-compatible formats, requiring either computationally expensive alignment mechanisms or manual graph verbalization techniques that often lose critical structural details. Moreover, these methods typically require labeled data from source domains for effective transfer learning, significantly constraining their adaptability. We propose STAG, a novel self-supervised framework that directly quantizes graph structural information into discrete tokens using a frozen codebook. Unlike traditional quantization approaches, our method employs soft assignment and KL divergence guided quantization to address the unique challenges of graph data, which lacks natural tokenization structures. Our framework enables both LLM-based and traditional learning approaches, supporting true zero-shot transfer learning without requiring labeled data even in the source domain. Extensive experiments demonstrate state-of-the-art performance across multiple node classification benchmarks while maintaining compatibility with different LLM architectures, offering an elegant solution to bridging graph learning with LLMs.
2031: 
2032: ABSTRACT.
2033: 
2034: Text-attributed graphs (TAGs) have emerged as a powerful representation for modeling complex relationships across diverse domains. With the rise of large language models (LLMs), there is growing interest in leveraging their capabilities for graph learning. However, current approaches face significant challenges in embedding structural information into LLM-compatible formats, requiring either computationally expensive alignment mechanisms or manual graph verbalization techniques that often lose critical structural details. Moreover, these methods typically require labeled data from source domains for effective transfer learning, significantly constraining their adaptability. We propose STAG, a novel self-supervised framework that directly quantizes graph structural information into discrete tokens using a frozen codebook. Unlike traditional quantization approaches, our method employs soft assignment and KL divergence guided quantization to address the unique challenges of graph data, which lacks natural tokenization structures. Our framework enables both LLM-based and traditional learning approaches, supporting true zero-shot transfer learning without requiring labeled data even in the source domain. Extensive experiments demonstrate state-of-the-art performance across multiple node classification benchmarks while maintaining compatibility with different LLM architectures, offering an elegant solution to bridging graph learning with LLMs.
2035: 
2036: text-attributed graphs, large language models, few-shot, zero-shot, graph transfer learning
2037: 
2038: 1. Introduction
2039: 
2040: Graphs serve as a cornerstone for modeling and understanding complex relationships across diverse domains, from social media (Perozzi et al., 2014; Grover and Leskovec, 2016; Kipf and Welling, 2017a) and knowledge graphs (Bordes et al., 2013; Wang et al., 2014; Trouillon et al., 2016) to recommendation systems (Fan et al., 2019; He et al., 2020; Wang et al., 2019). The structural information inherent in graphs is critical for effective graph learning, driving the development of graph neural networks (GNNs) (Veličković et al., 2018). Meanwhile, many real-world graphs contain textual descriptions, such as paper abstracts in citation networks (Yang et al., 2016), and product descriptions in co-purchase networks (McAuley et al., 2015).
2041: Such graphs are known as text-attributed graphs (TAGs) (Wen and Fang, 2024; Yan et al., 2023), in which nodes or edges are associated with rich textual content. However, conventional GNNs struggle to effectively utilize raw text in TAGs. With the rise of pre-trained language models (PLMs) (Kenton and Toutanova, 2019; He et al., 2021) and large language models (LLMs) (Brown et al., 2020; Touvron et al., 2023; Achiam et al., 2023; Hoffmann et al., 2022; Yang et al., 2024; Guo et al., 2025), there is growing interest in combining LLMs with graph learning, termed as GraphLLM (Chen et al., 2024a). Among existing GraphLLM studies, processing TAGs represents an important direction due to the abundance of both semantic and structural information in TAGs.

full_text/2507.09531v1.txt:1138::1152 (0.2794)
1138: Additionally, each detected ROI is pooled into a different size (based on its modality) and flattened to a set of feature vectors rather than one fixed vector per region.
1139: The resulting semantic tokens are concatenated to form rich, context-enriched region representations that preserve fine-grained cues (e.g., fonts, textures) and holistic layout information often lost by static RoI-pooled vectors.
1140: 
1141: These design choices—OCR-free end‐to‐end trainable region proposals and multi‐scale semantic alignment—distinguish VDInstruct ’s dual‐vision encoder from existing region‐based document models and underpin its superior performance on both in‐domain and zero‐shot tasks.
1142: 
1143: Appendix B VDInstruct-Parsing statistics
1144: 
1145: From each dataset, we randomly sample up to 50,000 images from the training split to construct a balanced and diverse training set. To maintain data quality and reduce noise, we exclude images that contain more than 1,000 bounding boxes. A similar sampling strategy is applied to create the test set using the original test or validation splits (with a maximum 1,000 samples per dataset). For vision annotations, we follow dataset-specific rules: AI2D uses the blob attribute, DocBank uses the figure class, and DocLayNet uses the picture class. For datasets such as SciCap and ScienceQA, where graphical content is often embedded as standalone images, we place these figures on a white background to synthesize a consistent visual region. In cases like KLC and PWC, where predefined visual annotations are lacking, we apply a pretrained document layout analysis model [15] to infer vision regions, taking advantage of the visual similarity between these datasets and the model’s original training data.  Tab. 6 and Tab. 7 summarize the sample and bounding box distributions across the seven datasets.
1146: 
1147: Table 6: Sample distribution in the VDInstruct-Parsing dataset across training and test sets.
1148: 
1149: AI2D
1150: DocLayNet
1151: DocBank
1152: SciCap

full_text/2507.09531v1.txt:3917::3931 (0.2794)
3917: 
3918: These design choices—OCR-free end‐to‐end trainable region proposals and multi‐scale semantic alignment—distinguish VDInstruct ’s dual‐vision encoder from existing region‐based document models and underpin its superior performance on both in‐domain and zero‐shot tasks.
3919: 
3920: These design choices—OCR-free end‐to‐end trainable region proposals and multi‐scale semantic alignment—distinguish VDInstruct ’s dual‐vision encoder from existing region‐based document models and underpin its superior performance on both in‐domain and zero‐shot tasks.
3921: 
3922: Appendix B VDInstruct-Parsing statistics
3923: 
3924: From each dataset, we randomly sample up to 50,000 images from the training split to construct a balanced and diverse training set. To maintain data quality and reduce noise, we exclude images that contain more than 1,000 bounding boxes. A similar sampling strategy is applied to create the test set using the original test or validation splits (with a maximum 1,000 samples per dataset). For vision annotations, we follow dataset-specific rules: AI2D uses the blob attribute, DocBank uses the figure class, and DocLayNet uses the picture class. For datasets such as SciCap and ScienceQA, where graphical content is often embedded as standalone images, we place these figures on a white background to synthesize a consistent visual region. In cases like KLC and PWC, where predefined visual annotations are lacking, we apply a pretrained document layout analysis model [15] to infer vision regions, taking advantage of the visual similarity between these datasets and the model’s original training data.  Tab. 6 and Tab. 7 summarize the sample and bounding box distributions across the seven datasets.
3925: 
3926: Table 6: Sample distribution in the VDInstruct-Parsing dataset across training and test sets.
3927: 
3928: AI2D
3929: DocLayNet
3930: DocBank
3931: SciCap

full_text/2507.09531v1.txt:3968::3982 (0.2794)
3968: Test
3969: 983.0K
3970: 7.6K
3971: 990.6K
3972: 
3973: APPENDIX B VDINSTRUCT-PARSING STATISTICS
3974: 
3975: From each dataset, we randomly sample up to 50,000 images from the training split to construct a balanced and diverse training set. To maintain data quality and reduce noise, we exclude images that contain more than 1,000 bounding boxes. A similar sampling strategy is applied to create the test set using the original test or validation splits (with a maximum 1,000 samples per dataset). For vision annotations, we follow dataset-specific rules: AI2D uses the blob attribute, DocBank uses the figure class, and DocLayNet uses the picture class. For datasets such as SciCap and ScienceQA, where graphical content is often embedded as standalone images, we place these figures on a white background to synthesize a consistent visual region. In cases like KLC and PWC, where predefined visual annotations are lacking, we apply a pretrained document layout analysis model [15] to infer vision regions, taking advantage of the visual similarity between these datasets and the model’s original training data.  Tab. 6 and Tab. 7 summarize the sample and bounding box distributions across the seven datasets.
3976: 
3977: From each dataset, we randomly sample up to 50,000 images from the training split to construct a balanced and diverse training set. To maintain data quality and reduce noise, we exclude images that contain more than 1,000 bounding boxes. A similar sampling strategy is applied to create the test set using the original test or validation splits (with a maximum 1,000 samples per dataset). For vision annotations, we follow dataset-specific rules: AI2D uses the blob attribute, DocBank uses the figure class, and DocLayNet uses the picture class. For datasets such as SciCap and ScienceQA, where graphical content is often embedded as standalone images, we place these figures on a white background to synthesize a consistent visual region. In cases like KLC and PWC, where predefined visual annotations are lacking, we apply a pretrained document layout analysis model [15] to infer vision regions, taking advantage of the visual similarity between these datasets and the model’s original training data.  Tab. 6 and Tab. 7 summarize the sample and bounding box distributions across the seven datasets.
3978: 
3979: Appendix C Training details of VDInstruct
3980: 
3981: C.1 The number of image tokens
3982: 

full_text/2507.09531v1.txt:3970::3984 (0.2794)
3970: 7.6K
3971: 990.6K
3972: 
3973: APPENDIX B VDINSTRUCT-PARSING STATISTICS
3974: 
3975: From each dataset, we randomly sample up to 50,000 images from the training split to construct a balanced and diverse training set. To maintain data quality and reduce noise, we exclude images that contain more than 1,000 bounding boxes. A similar sampling strategy is applied to create the test set using the original test or validation splits (with a maximum 1,000 samples per dataset). For vision annotations, we follow dataset-specific rules: AI2D uses the blob attribute, DocBank uses the figure class, and DocLayNet uses the picture class. For datasets such as SciCap and ScienceQA, where graphical content is often embedded as standalone images, we place these figures on a white background to synthesize a consistent visual region. In cases like KLC and PWC, where predefined visual annotations are lacking, we apply a pretrained document layout analysis model [15] to infer vision regions, taking advantage of the visual similarity between these datasets and the model’s original training data.  Tab. 6 and Tab. 7 summarize the sample and bounding box distributions across the seven datasets.
3976: 
3977: From each dataset, we randomly sample up to 50,000 images from the training split to construct a balanced and diverse training set. To maintain data quality and reduce noise, we exclude images that contain more than 1,000 bounding boxes. A similar sampling strategy is applied to create the test set using the original test or validation splits (with a maximum 1,000 samples per dataset). For vision annotations, we follow dataset-specific rules: AI2D uses the blob attribute, DocBank uses the figure class, and DocLayNet uses the picture class. For datasets such as SciCap and ScienceQA, where graphical content is often embedded as standalone images, we place these figures on a white background to synthesize a consistent visual region. In cases like KLC and PWC, where predefined visual annotations are lacking, we apply a pretrained document layout analysis model [15] to infer vision regions, taking advantage of the visual similarity between these datasets and the model’s original training data.  Tab. 6 and Tab. 7 summarize the sample and bounding box distributions across the seven datasets.
3978: 
3979: Appendix C Training details of VDInstruct
3980: 
3981: C.1 The number of image tokens
3982: 
3983: Figure 5: The number of image tokens encoded by VDInstruct and its counterparts. The red and blue boxes cover the detected text and vision ROIs, respectively. Our dual vision encoder scales the number of image tokens with the detected contents, minimizing token redundancy and information loss.
3984: 

full_text/2506.08771v1.txt:880::894 (0.2829)
 880:  4.
 881: 
 882: Cross Encoder vs. Gradient Boosting: Neural or Classical Subgraph Ranker? Our cross encoder-based Subgraph Ranker uses neural networks to rank the subgraphs, relying on contextual embeddings generated by the encoder model. In contrast, our gradient boosting-based Subgraph Ranker ranks subgraphs using decision trees that learn from manually defined features, such as n-grams. Overall, while cross encoder-based subgraphs rankers generally deliver superior performance (9 out of 12 cases), the gradient boosting-based ranker performs relatively well in our task, emerging as the top model in 2 out of 12 cases (SEMEVAL with gemma-7b and ADE with llama-3-8b). According to (Gavito et al., 2023), gradient-boosting excels on structured data, and although the subgraphs are represented as token sequences, they retain their structured nature from KGs, ensuring effective ranking. Meanwhile, within the variation of the LTR-based cross encoders, the pairwise approach (ranknet) consistently performs best, followed by pointwise (rmse) and listwise (listnet). The pairwise approach allows the model to learn subtle differences between subgraphs, leading to better ranking prediction.
 883: 
 884:  5.
 885: 
 886: Wikidata vs. Hetionet.
 887: For the biomedical datasets, using subgraphs from the Hetionet KG improved F1 scores by up to 44.4 points over the no-subgraph baseline. For open-domain dataset using Wikidata, the improvement was as high as 22.37 points, indicating its flexibility regarding the choice of KGs. The smaller improvement with Wikidata suggests that the LLMs already possess partial knowledge of certain relationships, likely learned from similar sources such as Wikipedia. However, our approach enhances this by guiding the model to focus on relevant causal paths, resulting in improved performance.
 888: 
 889: 6.1. Comparison to Statistical-Based Causal Discovery
 890: 
 891: Conventional causal discovery uses statistical methods on observational data, while our approach leverages LLMs and knowledge graphs to infer causal relationships from metadata.
 892: Thus, to comprehensively evaluate our approach, we conducted additional experiments comparing it to conventional statistical-based methods. Specifically, we evaluated on the causal benchmark SACHS (Sachs et al., 2005) protein causality dataset, comparing our method against conventional statistical-based causal discovery methods: PC Algorithm (Spirtes et al., 2001b), Exact Search/A* (Yuan and Malone, 2013), and DirectLingam (Shimizu et al., 2011).
 893: The dataset was selected for its suitability in this evaluation scenario, as it contains real-world observational data needed for statistical-based analysis and a ground truth causal graph created by human experts, allowing empirical evaluation. The results are summarized in Table 3. Some of the statistical-based scores are obtained from (Takayama et al., 2024).
 894: 

full_text/2506.08771v1.txt:3882::3896 (0.2829)
3882:  4.
3883: 
3884: Cross Encoder vs. Gradient Boosting: Neural or Classical Subgraph Ranker? Our cross encoder-based Subgraph Ranker uses neural networks to rank the subgraphs, relying on contextual embeddings generated by the encoder model. In contrast, our gradient boosting-based Subgraph Ranker ranks subgraphs using decision trees that learn from manually defined features, such as n-grams. Overall, while cross encoder-based subgraphs rankers generally deliver superior performance (9 out of 12 cases), the gradient boosting-based ranker performs relatively well in our task, emerging as the top model in 2 out of 12 cases (SEMEVAL with gemma-7b and ADE with llama-3-8b). According to (Gavito et al., 2023), gradient-boosting excels on structured data, and although the subgraphs are represented as token sequences, they retain their structured nature from KGs, ensuring effective ranking. Meanwhile, within the variation of the LTR-based cross encoders, the pairwise approach (ranknet) consistently performs best, followed by pointwise (rmse) and listwise (listnet). The pairwise approach allows the model to learn subtle differences between subgraphs, leading to better ranking prediction.
3885: 
3886:  5.
3887: 
3888: Wikidata vs. Hetionet.
3889: For the biomedical datasets, using subgraphs from the Hetionet KG improved F1 scores by up to 44.4 points over the no-subgraph baseline. For open-domain dataset using Wikidata, the improvement was as high as 22.37 points, indicating its flexibility regarding the choice of KGs. The smaller improvement with Wikidata suggests that the LLMs already possess partial knowledge of certain relationships, likely learned from similar sources such as Wikipedia. However, our approach enhances this by guiding the model to focus on relevant causal paths, resulting in improved performance.
3890: 
3891: 6.1. Comparison to Statistical-Based Causal Discovery
3892: 
3893: Conventional causal discovery uses statistical methods on observational data, while our approach leverages LLMs and knowledge graphs to infer causal relationships from metadata.
3894: Thus, to comprehensively evaluate our approach, we conducted additional experiments comparing it to conventional statistical-based methods. Specifically, we evaluated on the causal benchmark SACHS (Sachs et al., 2005) protein causality dataset, comparing our method against conventional statistical-based causal discovery methods: PC Algorithm (Spirtes et al., 2001b), Exact Search/A* (Yuan and Malone, 2013), and DirectLingam (Shimizu et al., 2011).
3895: The dataset was selected for its suitability in this evaluation scenario, as it contains real-world observational data needed for statistical-based analysis and a ground truth causal graph created by human experts, allowing empirical evaluation. The results are summarized in Table 3. Some of the statistical-based scores are obtained from (Takayama et al., 2024).
3896: 

full_text/2506.08771v1.txt:3975::3989 (0.2829)
3975: Cross Encoder vs. Gradient Boosting: Neural or Classical Subgraph Ranker? Our cross encoder-based Subgraph Ranker uses neural networks to rank the subgraphs, relying on contextual embeddings generated by the encoder model. In contrast, our gradient boosting-based Subgraph Ranker ranks subgraphs using decision trees that learn from manually defined features, such as n-grams. Overall, while cross encoder-based subgraphs rankers generally deliver superior performance (9 out of 12 cases), the gradient boosting-based ranker performs relatively well in our task, emerging as the top model in 2 out of 12 cases (SEMEVAL with gemma-7b and ADE with llama-3-8b). According to (Gavito et al., 2023), gradient-boosting excels on structured data, and although the subgraphs are represented as token sequences, they retain their structured nature from KGs, ensuring effective ranking. Meanwhile, within the variation of the LTR-based cross encoders, the pairwise approach (ranknet) consistently performs best, followed by pointwise (rmse) and listwise (listnet). The pairwise approach allows the model to learn subtle differences between subgraphs, leading to better ranking prediction.
3976: 
3977: Cross Encoder vs. Gradient Boosting: Neural or Classical Subgraph Ranker? Our cross encoder-based Subgraph Ranker uses neural networks to rank the subgraphs, relying on contextual embeddings generated by the encoder model. In contrast, our gradient boosting-based Subgraph Ranker ranks subgraphs using decision trees that learn from manually defined features, such as n-grams. Overall, while cross encoder-based subgraphs rankers generally deliver superior performance (9 out of 12 cases), the gradient boosting-based ranker performs relatively well in our task, emerging as the top model in 2 out of 12 cases (SEMEVAL with gemma-7b and ADE with llama-3-8b). According to (Gavito et al., 2023), gradient-boosting excels on structured data, and although the subgraphs are represented as token sequences, they retain their structured nature from KGs, ensuring effective ranking. Meanwhile, within the variation of the LTR-based cross encoders, the pairwise approach (ranknet) consistently performs best, followed by pointwise (rmse) and listwise (listnet). The pairwise approach allows the model to learn subtle differences between subgraphs, leading to better ranking prediction.
3978: 
3979: 5.
3980: 
3981: Wikidata vs. Hetionet.
3982: For the biomedical datasets, using subgraphs from the Hetionet KG improved F1 scores by up to 44.4 points over the no-subgraph baseline. For open-domain dataset using Wikidata, the improvement was as high as 22.37 points, indicating its flexibility regarding the choice of KGs. The smaller improvement with Wikidata suggests that the LLMs already possess partial knowledge of certain relationships, likely learned from similar sources such as Wikipedia. However, our approach enhances this by guiding the model to focus on relevant causal paths, resulting in improved performance.
3983: 
3984: 5.
3985: 
3986: Wikidata vs. Hetionet.
3987: For the biomedical datasets, using subgraphs from the Hetionet KG improved F1 scores by up to 44.4 points over the no-subgraph baseline. For open-domain dataset using Wikidata, the improvement was as high as 22.37 points, indicating its flexibility regarding the choice of KGs. The smaller improvement with Wikidata suggests that the LLMs already possess partial knowledge of certain relationships, likely learned from similar sources such as Wikipedia. However, our approach enhances this by guiding the model to focus on relevant causal paths, resulting in improved performance.
3988: 
3989: Wikidata vs. Hetionet.


```

</details>


---

### 7. Query: Outline the chronological progression of structured pruning and sparsification techniques for LLMs, from early methods to the training-free approaches introduced by Sattarifard et al.

- **Query ID:** `temporal_1`
- **Query Type:** Temporal
- **Curated Source Files:** `full_text/2505.07796v2.txt, full_text/2506.15594v1.txt, full_text/2506.22309v1.txt, full_text/2507.15152v1.txt, full_text/2508.14302v1.txt, full_text/2508.15370v1.txt`

#### LLM Ground Truth Answer

> The evolution of structured pruning and sparsification techniques for LLMs began with early approaches like Optimal Brain Damage (OBD) (1989) and Optimal Brain Surgeon (OBS) (1993), which used Taylor expansions to estimate parameter impact on training loss. PerforatedCNNs (2016) later applied first-order Taylor expansion for structured pruning in convolutional neural networks. More recently, Transformer sparsification methods emerged, categorized into training-based methods (e.g., DejaVu (2023), ShadowLLM (2024), PowerInfer (2024)) that incur inference overhead, and training-free methods. Training-free methods, designed for latency-sensitive deployments, initially derived a static sparsity mask from the prompt for use throughout generation (e.g., GRIFFIN (2024), TDA (2025), TEAL (2024)). Newer works have proposed dynamic masks for *each* generated token (e.g., Zhang et al. (2025), You et al. (2025), Yin et al. (2025), Storaï et al. (2025), Qi et al. (2025), Shin et al. (2025), Lee et al. (2025), Yang et al. (2025)). Sattarifard et al.'s A/I-GLASS (2024) introduces training-free methods that combine local (prompt-specific) activations with global (model-intrinsic) neural importance for dynamic FFN unit selection, aiming to improve upon prior training-free methods, especially in long-form generation scenarios, without adding inference overhead.

**Source Document(s):** `full_text/2508.14302v1.txt`

#### `search` Tool Performance

**Command Executed:**

```bash
search "Outline the chronological progression of structured pruning and sparsification techniques for LLMs, from early methods to the training-free approaches introduced by Sattarifard et al." full_text/*.txt --top-k 10 --n-lines 7
```

**Retrieval Precision:** `0.33`
**Retrieval Recall:** `1.00`

**Documents Returned by `search`:** `full_text/2506.12953v1.txt, full_text/2507.19477v1.txt, full_text/2508.14302v1.txt`

#### LLM Search-Augmented Answer

> The chronological progression of structured pruning and sparsification techniques for LLMs, as described in the provided texts, begins with methods focusing on convolutional neural networks before transitioning to Transformers. Early work involved utilizing first-order saliency to reduce spatial redundancy in convolutional neural networks, which laid the groundwork for subsequent neuron- and kernel-level pruning. This was followed by Molchanov et al. (2017) applying the first-order Taylor criterion for pruning convolutional channels, a method that Molchanov et al. (2019) later generalized to second-order expansions.
> 
> For Transformers, Kwon et al. (2022) introduced a significant development: a Fisher information-based, training-free pruning framework designed to enhance inference efficiency. This marks a shift towards training-free methods specifically for Transformers.
> 
> Generally, Transformer sparsification techniques are categorized into two broad types:
> 
> 1.  **Training-based methods:** These methods, such as DejaVu (Liu et al. 2023), ShadowLLM (Akhauri et al. 2024), and PowerInfer (Song et al. 2024; Xue et al. 2024), rely on auxiliary predictors or routing mechanisms to achieve sparsity. While effective, they introduce inference-time overhead due to runtime decisions or additional computations.
> 
> 2.  **Training-free methods:** In contrast, training-free methods operate post-hoc on pre-trained models. These approaches, exemplified by the framework introduced by Kwon et al. (2022), are considered better suited for latency-sensitive deployments as they avoid the overhead associated with training-based decisions.
> 
> The provided search output does not contain any information regarding specific training-free approaches introduced by "Sattarifard et al." Therefore, the final part of the research question cannot be addressed with the given text.

<details><summary>View Original `search` Tool Output</summary>

```
full_text/2506.12953v1.txt:191::205 (0.3278)
 191: 
 192: Table 1: Summary of datasets used in our experiments.
 193: 
 194: 4.2 Main Results
 195: 
 196: For our experiments, we adopt S2IP-LLM as the primary baseline, a method that aligns time series embeddings with the semantic space of a pre-trained LLM through a tokenization framework. While effective, S2IP-LLM suffers from significant computational overhead, requiring extensive training and inference time due to its fine-tuning of LLM components. All methods are evaluated in a consistent zero-shot setting without model retraining to isolate the impact of prompting strategies.
 197: 
 198: Using various prompting strategies, we instructed a pre-trained LLM to consider time-series patches and utilize them for forecasting without any additional fine-tuning or retraining. Our experiments demonstrate that such patch-based prompting methods can significantly improve forecasting performance across multiple datasets and over shorter horizons. In contrast to models like S2IP-LLM, which rely on explicit decomposition, semantic alignment, and parameter tuning, our approach leverages instruction-tuned LLMs. Among all the strategies evaluated the PatchInstruct technique consistently delivered the best results. This suggests that prompting pre-trained LLMs with thoughtfully structured temporal context can match or even surpass models trained from scratch, offering a lightweight yet effective alternative for time-series forecasting.
 199: 
 200: Table 3 presents a performance comparison between S2IPLLM (the baseline) and our best-performing Patch Instruct method across multiple time series datasets and forecast horizons. The results clearly indicate that Patch Instruct consistently outperforms the baseline in terms of both MSE and MAE. Finally, Table 3 compares the two methods in terms of input/output token counts and computation time. The analysis reveals that Patch Instruct not only improves forecasting accuracy but also significantly reduces computational overhead. Overall, this comparison highlights the efficiency and effectiveness of the Patch Instruct method.
 201: 
 202: Dataset
 203: Horizon
 204: S2IP-LLM
 205: Zeroshot

full_text/2506.12953v1.txt:1581::1595 (0.3278)
1581: 
1582: Table 1: Summary of datasets used in our experiments.
1583: 
1584: 4.2 Main Results
1585: 
1586: For our experiments, we adopt S2IP-LLM as the primary baseline, a method that aligns time series embeddings with the semantic space of a pre-trained LLM through a tokenization framework. While effective, S2IP-LLM suffers from significant computational overhead, requiring extensive training and inference time due to its fine-tuning of LLM components. All methods are evaluated in a consistent zero-shot setting without model retraining to isolate the impact of prompting strategies.
1587: 
1588: Using various prompting strategies, we instructed a pre-trained LLM to consider time-series patches and utilize them for forecasting without any additional fine-tuning or retraining. Our experiments demonstrate that such patch-based prompting methods can significantly improve forecasting performance across multiple datasets and over shorter horizons. In contrast to models like S2IP-LLM, which rely on explicit decomposition, semantic alignment, and parameter tuning, our approach leverages instruction-tuned LLMs. Among all the strategies evaluated the PatchInstruct technique consistently delivered the best results. This suggests that prompting pre-trained LLMs with thoughtfully structured temporal context can match or even surpass models trained from scratch, offering a lightweight yet effective alternative for time-series forecasting.
1589: 
1590: Table 3 presents a performance comparison between S2IPLLM (the baseline) and our best-performing Patch Instruct method across multiple time series datasets and forecast horizons. The results clearly indicate that Patch Instruct consistently outperforms the baseline in terms of both MSE and MAE. Finally, Table 3 compares the two methods in terms of input/output token counts and computation time. The analysis reveals that Patch Instruct not only improves forecasting accuracy but also significantly reduces computational overhead. Overall, this comparison highlights the efficiency and effectiveness of the Patch Instruct method.
1591: 
1592: Dataset
1593: Horizon
1594: S2IP-LLM
1595: Zeroshot

full_text/2506.12953v1.txt:2125::2139 (0.3278)
2125: 34,172
2126: 2.5–70
2127: 
2128: 4.2 Main Results
2129: 
2130: For our experiments, we adopt S2IP-LLM as the primary baseline, a method that aligns time series embeddings with the semantic space of a pre-trained LLM through a tokenization framework. While effective, S2IP-LLM suffers from significant computational overhead, requiring extensive training and inference time due to its fine-tuning of LLM components. All methods are evaluated in a consistent zero-shot setting without model retraining to isolate the impact of prompting strategies.
2131: 
2132: Using various prompting strategies, we instructed a pre-trained LLM to consider time-series patches and utilize them for forecasting without any additional fine-tuning or retraining. Our experiments demonstrate that such patch-based prompting methods can significantly improve forecasting performance across multiple datasets and over shorter horizons. In contrast to models like S2IP-LLM, which rely on explicit decomposition, semantic alignment, and parameter tuning, our approach leverages instruction-tuned LLMs. Among all the strategies evaluated the PatchInstruct technique consistently delivered the best results. This suggests that prompting pre-trained LLMs with thoughtfully structured temporal context can match or even surpass models trained from scratch, offering a lightweight yet effective alternative for time-series forecasting.
2133: 
2134: Table 3 presents a performance comparison between S2IPLLM (the baseline) and our best-performing Patch Instruct method across multiple time series datasets and forecast horizons. The results clearly indicate that Patch Instruct consistently outperforms the baseline in terms of both MSE and MAE. Finally, Table 3 compares the two methods in terms of input/output token counts and computation time. The analysis reveals that Patch Instruct not only improves forecasting accuracy but also significantly reduces computational overhead. Overall, this comparison highlights the efficiency and effectiveness of the Patch Instruct method.
2135: 
2136: Dataset
2137: Horizon
2138: S2IP-LLM
2139: Zeroshot

full_text/2506.12953v1.txt:2438::2452 (0.3278)
2438: 
2439: 4.2 MAIN RESULTS
2440: 
2441: For our experiments, we adopt S2IP-LLM as the primary baseline, a method that aligns time series embeddings with the semantic space of a pre-trained LLM through a tokenization framework. While effective, S2IP-LLM suffers from significant computational overhead, requiring extensive training and inference time due to its fine-tuning of LLM components. All methods are evaluated in a consistent zero-shot setting without model retraining to isolate the impact of prompting strategies.
2442: 
2443: For our experiments, we adopt S2IP-LLM as the primary baseline, a method that aligns time series embeddings with the semantic space of a pre-trained LLM through a tokenization framework. While effective, S2IP-LLM suffers from significant computational overhead, requiring extensive training and inference time due to its fine-tuning of LLM components. All methods are evaluated in a consistent zero-shot setting without model retraining to isolate the impact of prompting strategies.
2444: 
2445: Using various prompting strategies, we instructed a pre-trained LLM to consider time-series patches and utilize them for forecasting without any additional fine-tuning or retraining. Our experiments demonstrate that such patch-based prompting methods can significantly improve forecasting performance across multiple datasets and over shorter horizons. In contrast to models like S2IP-LLM, which rely on explicit decomposition, semantic alignment, and parameter tuning, our approach leverages instruction-tuned LLMs. Among all the strategies evaluated the PatchInstruct technique consistently delivered the best results. This suggests that prompting pre-trained LLMs with thoughtfully structured temporal context can match or even surpass models trained from scratch, offering a lightweight yet effective alternative for time-series forecasting.
2446: 
2447: Using various prompting strategies, we instructed a pre-trained LLM to consider time-series patches and utilize them for forecasting without any additional fine-tuning or retraining. Our experiments demonstrate that such patch-based prompting methods can significantly improve forecasting performance across multiple datasets and over shorter horizons. In contrast to models like S2IP-LLM, which rely on explicit decomposition, semantic alignment, and parameter tuning, our approach leverages instruction-tuned LLMs. Among all the strategies evaluated the PatchInstruct technique consistently delivered the best results. This suggests that prompting pre-trained LLMs with thoughtfully structured temporal context can match or even surpass models trained from scratch, offering a lightweight yet effective alternative for time-series forecasting.
2448: 
2449: Table 3 presents a performance comparison between S2IPLLM (the baseline) and our best-performing Patch Instruct method across multiple time series datasets and forecast horizons. The results clearly indicate that Patch Instruct consistently outperforms the baseline in terms of both MSE and MAE. Finally, Table 3 compares the two methods in terms of input/output token counts and computation time. The analysis reveals that Patch Instruct not only improves forecasting accuracy but also significantly reduces computational overhead. Overall, this comparison highlights the efficiency and effectiveness of the Patch Instruct method.
2450: 
2451: Table 3 presents a performance comparison between S2IPLLM (the baseline) and our best-performing Patch Instruct method across multiple time series datasets and forecast horizons. The results clearly indicate that Patch Instruct consistently outperforms the baseline in terms of both MSE and MAE. Finally, Table 3 compares the two methods in terms of input/output token counts and computation time. The analysis reveals that Patch Instruct not only improves forecasting accuracy but also significantly reduces computational overhead. Overall, this comparison highlights the efficiency and effectiveness of the Patch Instruct method.
2452: 

full_text/2506.12953v1.txt:2440::2454 (0.3278)
2440: 
2441: For our experiments, we adopt S2IP-LLM as the primary baseline, a method that aligns time series embeddings with the semantic space of a pre-trained LLM through a tokenization framework. While effective, S2IP-LLM suffers from significant computational overhead, requiring extensive training and inference time due to its fine-tuning of LLM components. All methods are evaluated in a consistent zero-shot setting without model retraining to isolate the impact of prompting strategies.
2442: 
2443: For our experiments, we adopt S2IP-LLM as the primary baseline, a method that aligns time series embeddings with the semantic space of a pre-trained LLM through a tokenization framework. While effective, S2IP-LLM suffers from significant computational overhead, requiring extensive training and inference time due to its fine-tuning of LLM components. All methods are evaluated in a consistent zero-shot setting without model retraining to isolate the impact of prompting strategies.
2444: 
2445: Using various prompting strategies, we instructed a pre-trained LLM to consider time-series patches and utilize them for forecasting without any additional fine-tuning or retraining. Our experiments demonstrate that such patch-based prompting methods can significantly improve forecasting performance across multiple datasets and over shorter horizons. In contrast to models like S2IP-LLM, which rely on explicit decomposition, semantic alignment, and parameter tuning, our approach leverages instruction-tuned LLMs. Among all the strategies evaluated the PatchInstruct technique consistently delivered the best results. This suggests that prompting pre-trained LLMs with thoughtfully structured temporal context can match or even surpass models trained from scratch, offering a lightweight yet effective alternative for time-series forecasting.
2446: 
2447: Using various prompting strategies, we instructed a pre-trained LLM to consider time-series patches and utilize them for forecasting without any additional fine-tuning or retraining. Our experiments demonstrate that such patch-based prompting methods can significantly improve forecasting performance across multiple datasets and over shorter horizons. In contrast to models like S2IP-LLM, which rely on explicit decomposition, semantic alignment, and parameter tuning, our approach leverages instruction-tuned LLMs. Among all the strategies evaluated the PatchInstruct technique consistently delivered the best results. This suggests that prompting pre-trained LLMs with thoughtfully structured temporal context can match or even surpass models trained from scratch, offering a lightweight yet effective alternative for time-series forecasting.
2448: 
2449: Table 3 presents a performance comparison between S2IPLLM (the baseline) and our best-performing Patch Instruct method across multiple time series datasets and forecast horizons. The results clearly indicate that Patch Instruct consistently outperforms the baseline in terms of both MSE and MAE. Finally, Table 3 compares the two methods in terms of input/output token counts and computation time. The analysis reveals that Patch Instruct not only improves forecasting accuracy but also significantly reduces computational overhead. Overall, this comparison highlights the efficiency and effectiveness of the Patch Instruct method.
2450: 
2451: Table 3 presents a performance comparison between S2IPLLM (the baseline) and our best-performing Patch Instruct method across multiple time series datasets and forecast horizons. The results clearly indicate that Patch Instruct consistently outperforms the baseline in terms of both MSE and MAE. Finally, Table 3 compares the two methods in terms of input/output token counts and computation time. The analysis reveals that Patch Instruct not only improves forecasting accuracy but also significantly reduces computational overhead. Overall, this comparison highlights the efficiency and effectiveness of the Patch Instruct method.
2452: 
2453: Dataset
2454: Horizon

full_text/2508.14302v1.txt:129::143 (0.3363)
 129: 
 130: Our goal is to dynamically prune a subset of FFN hidden units (neurons) at inference-time, to reduce both the parameter count and computational cost, while minimizing degradation in downstream model quality with respect to the base (unpruned) model.
 131: Specifically, given a per-layer budget k<mk<m, we aim to select a subset of kk hidden units (referred to as critical neurons) to retain,
 132: and removing the remaining m−km-k units.
 133: 
 134: 3 Previous Work
 135: 
 136: Transformer sparsification techniques can be broadly categorized into training-based and training-free methods.
 137: Training-based methods, such as
 138: DejaVu (Liu et al. 2023),
 139: ShadowLLM (Akhauri et al. 2024), and
 140: PowerInfer (Song et al. 2024; Xue et al. 2024)
 141: rely on auxiliary predictors or routing mechanisms to achieve sparsity. Despite their effectiveness, they introduce inference-time overhead due to runtime decisions or auxiliary computations.
 142: In contrast, training-free methods operate post-hoc on pre-trained models, and are therefore better suited for latency-sensitive deployments.
 143: 

full_text/2508.14302v1.txt:1901::1915 (0.3363)
1901: 
1902: Our goal is to dynamically prune a subset of FFN hidden units (neurons) at inference-time, to reduce both the parameter count and computational cost, while minimizing degradation in downstream model quality with respect to the base (unpruned) model.
1903: Specifically, given a per-layer budget k<mk<m, we aim to select a subset of kk hidden units (referred to as critical neurons) to retain,
1904: and removing the remaining m−km-k units.
1905: 
1906: 3 Previous Work
1907: 
1908: Transformer sparsification techniques can be broadly categorized into training-based and training-free methods.
1909: Training-based methods, such as
1910: DejaVu (Liu et al. 2023),
1911: ShadowLLM (Akhauri et al. 2024), and
1912: PowerInfer (Song et al. 2024; Xue et al. 2024)
1913: rely on auxiliary predictors or routing mechanisms to achieve sparsity. Despite their effectiveness, they introduce inference-time overhead due to runtime decisions or auxiliary computations.
1914: In contrast, training-free methods operate post-hoc on pre-trained models, and are therefore better suited for latency-sensitive deployments.
1915: 

full_text/2508.14302v1.txt:1942::1956 (0.3363)
1942: focusing on reducing spatial redundancy in convolutional neural networks.
1943: This approach demonstrates the general effectiveness of first-order saliency and sets the stage for later neuron- and kernel-level pruning methods.
1944: 
1945: Similarly, Molchanov et al. (2017) applies the first-order Taylor criterion to prune convolutional channels. Molchanov et al. (2019) generalizes this to second-order expansions, and Kwon et al. (2022) introduces a Fisher information-based, training-free pruning framework for Transformers, enhancing inference efficiency.
1946: 
1947: 3 PREVIOUS WORK
1948: 
1949: Transformer sparsification techniques can be broadly categorized into training-based and training-free methods.
1950: Training-based methods, such as
1951: DejaVu (Liu et al. 2023),
1952: ShadowLLM (Akhauri et al. 2024), and
1953: PowerInfer (Song et al. 2024; Xue et al. 2024)
1954: rely on auxiliary predictors or routing mechanisms to achieve sparsity. Despite their effectiveness, they introduce inference-time overhead due to runtime decisions or auxiliary computations.
1955: In contrast, training-free methods operate post-hoc on pre-trained models, and are therefore better suited for latency-sensitive deployments.
1956: 

full_text/2508.14302v1.txt:1950::1964 (0.3363)
1950: Training-based methods, such as
1951: DejaVu (Liu et al. 2023),
1952: ShadowLLM (Akhauri et al. 2024), and
1953: PowerInfer (Song et al. 2024; Xue et al. 2024)
1954: rely on auxiliary predictors or routing mechanisms to achieve sparsity. Despite their effectiveness, they introduce inference-time overhead due to runtime decisions or auxiliary computations.
1955: In contrast, training-free methods operate post-hoc on pre-trained models, and are therefore better suited for latency-sensitive deployments.
1956: 
1957: Transformer sparsification techniques can be broadly categorized into training-based and training-free methods.
1958: Training-based methods, such as
1959: DejaVu (Liu et al. 2023),
1960: ShadowLLM (Akhauri et al. 2024), and
1961: PowerInfer (Song et al. 2024; Xue et al. 2024)
1962: rely on auxiliary predictors or routing mechanisms to achieve sparsity. Despite their effectiveness, they introduce inference-time overhead due to runtime decisions or auxiliary computations.
1963: In contrast, training-free methods operate post-hoc on pre-trained models, and are therefore better suited for latency-sensitive deployments.
1964: 

full_text/2507.19477v1.txt:32::46 (0.3662)
  32: 
  33: Since ChatGPT was released (OpenAI, 2022), numerous studies have evaluated LLMs’ event forecasting capabilities and compared them with human performance (Schoenegger et al., 2024; Hsieh et al., 2024). Initially, optimistic reports were shared that LLMs showed performance approaching superforecaster-level (Phan et al., 2024). However, subsequent analyses identified methodological issues including insufficient statistical significance, information leakage from data preceding the knowledge cut-off date, and contamination from post-resolution documents in search results, leading to criticism that LLMs’ abilities were overestimated (Lopez-Lira et al., 2025; Bosse et al., 2024). These criticisms resulted in skepticism within the event forecasting community (Paleka et al., 2025a; Matthews, 2025).
  34: 
  35: However, we argue that recent studies provide positive signals for event forecasting. A recent study using more rigorous evaluation methods (Karger et al., 2025) reports that LLM performance in event forecasting is steadily improving with generational advances, and they are getting closer to superforecaster-level. Additionally, recent reasoning models like OpenAI o1 and o3 (OpenAI, 2024; 2025a) have shown improved performance compared to previous models (Hickman, 2025), and performance improvements through reinforcement learning (RL) have also been reported (Turtel et al., 2025a; b). Furthermore, the unprecedented success of reasoning model with tool-use like OpenAI’s and Gemini’s Deep Research (Citron, 2024; OpenAI, 2025b; Anthropic, 2025) suggests that technology capable of greatly improving forecasting performance has been developed.
  36: 
  37: Based on these recent positive trends, we argue that conditions are now favorable for research on large-scale training of event forecasting LLMs to approach superforecaster-level performance. This paper presents two key research directions for this purpose: training methodology (Section 4) and large-scale data acquisition (Section 5).
  38: 
  39: For training methodology, we first introduce three unique difficulties in LLM-based event forecasting training.
  40: First is the noisiness and sparsity problem, which is the difficulty in learning due to inherent uncertainty in event forecasting outcomes and the sparsity of similar events.
  41: Second is the knowledge cut-off problem, where it is difficult to train or evaluate event forecasting questions about knowledge that LLMs already know internally, greatly limiting usable training data.
  42: Third is the simple reward structure problem, where models can obtain rewards more easily than in other RL tasks without developing proper reasoning capabilities, hindering actual prediction ability improvement.
  43: 
  44: To mitigate these problems, we present several solutions. We provide theoretical grounds for various training label assignment strategies through hypothetical event Bayesian network modeling, introduce methods of utilizing poorly-recalled data and generating counterfactual events to tackle the knowledge cut-off problem, and discuss ways to solve the simple reward structure problem through auxiliary reward signals and subquestions.
  45: 
  46: For large-scale data acquisition, we point out that previous research mainly relied on prediction markets and propose aggressive use of three data categories: (1) market dataset - data available from prediction markets like Polymarket and Metaculus, (2) public dataset - structured data available from public databases like GDP and economic indicators, and (3) crawling dataset - unstructured data collected and processed from the web like news. Using these diverse data sources will enable large-scale training and fast evaluation cycles, promoting model performance improvement and development of generalized event forecasting capabilities.


```

</details>


---

### 8. Query: Based on the provided documents, describe the historical evolution of benchmarks for evaluating Vision-Language Large Models (VLLMs) in Document Understanding (DU) and multimodal reasoning, leading up to the introduction of WikiMixQA.

- **Query ID:** `temporal_2`
- **Query Type:** Temporal
- **Curated Source Files:** `full_text/2505.07796v2.txt, full_text/2506.15594v1.txt, full_text/2506.22309v1.txt, full_text/2507.15152v1.txt, full_text/2508.14302v1.txt, full_text/2508.15370v1.txt`

#### LLM Ground Truth Answer

> Early Visual Question Answering (VQA) benchmarks for Document Understanding (DU) primarily focused on single-page documents and evaluated specific components like tables (e.g., Herzig et al., Chen et al., 2020/2021) or charts (e.g., Chaudhry et al., Methani et al., 2020; Masry et al., Kantharaj et al., 2022; Tanaka et al., 2023a). Over time, benchmarks aimed to extend beyond single-page settings. MP-DocVQA (Tito et al., 2023) was an extension of DocVQA (Mathew et al., 2021) but still lacked cross-page questions. DUDE (Van Landeghem et al., 2023) introduced a small proportion of cross-page questions but often yielded less challenging questions focused on layout. SlideVQA (Tanaka et al., 2023b) incorporated cross-page questions tailored to slide decks. Doc2SoarGraph (Zhu et al., 2024) included some multi-page queries but was limited to PDF format. FinanceBench (Islam et al., 2023) addressed long-context and cross-page questions but was domain-specific and required expert evaluation. CRAB (Romanou et al., 2023) focused on causal understanding. MMLongBench-Doc (Ma et al., 2024) integrated diverse sources with cross-page questions but had limited document coverage. Finally, WikiMixQA (Foroutan et al., 2024) was introduced to specifically address the gap in complex cross-modal reasoning over tables and charts from long (average 24.18 pages), digital-only Wikipedia documents, with questions requiring synthesis from multiple modalities.

**Source Document(s):** `full_text/2506.15594v1.txt`

#### `search` Tool Performance

**Command Executed:**

```bash
search "Based on the provided documents, describe the historical evolution of benchmarks for evaluating Vision-Language Large Models (VLLMs) in Document Understanding (DU) and multimodal reasoning, leading up to the introduction of WikiMixQA." full_text/*.txt --top-k 10 --n-lines 7
```

**Retrieval Precision:** `0.00`
**Retrieval Recall:** `0.00`

**Documents Returned by `search`:** `full_text/2507.15882v2.txt`

#### LLM Search-Augmented Answer

> The historical evolution of benchmarks for evaluating Vision-Language Large Models (VLLMs) in Document Understanding (DU) and multimodal reasoning began with traditional Large Language Model (LLM) evaluations. Initially, these focused on short texts and specific tasks like question answering, summarization, and translation, utilizing benchmarks such as GLUE [19] and SuperGLUE [20]. These foundational benchmarks were valuable but did not require long-term context retention.
> 
> As LLMs advanced, there was a growing need to evaluate longer text comprehension, which led to the development of specialized long-context benchmarks. Examples include the Needle in a Haystack [21], designed to test information retrieval from extended contexts, and LongBench [22], which provided the first bilingual, multi-task framework for assessing long-form text understanding.
> 
> The emergence of multimodal VLMs necessitated new evaluation approaches. Benchmarks like VQA [23], NLVR [24], and MileBench [25] were developed to assess models' capabilities in processing and reasoning about combined visual and textual information. Within multimodal evaluation, document understanding emerged as a distinct and significant challenge. Early datasets in this area concentrated on specific elements, such as charts [26], or focused on single-page analysis [27]. More recently, benchmarks like DUDE [28], Loong [29], SlideVQA [30], and MMLongBench-Doc [31] attempted to tackle multi-page document comprehension.
> 
> Despite these advancements, a significant gap remained in benchmarks capable of evaluating VLMs' performance on long, multimodal documents. Existing benchmarks often had limitations: they either lacked sufficient document length (typically less than 50 pages), relied on independently pre-extracted text and images rather than original documents, or did not allow for performance comparison of similar tasks across different document lengths. Recent benchmarks like MM-NIAH [32] and M-LongDoc [33] aimed to address some of these issues, but still had constraints. MM-NIAH had a limited prompt length (less than 72k tokens), making it unsuitable for genuinely long document evaluation, while M-LongDoc, despite featuring documents hundreds of pages long, offered only 851 questions, used a non-objective evaluation method, and did not support evaluating the same task with varying document lengths. Furthermore, both MM-NIAH and M-LongDoc relied on pre-extracting text and figures, preventing VLM providers from utilizing their native processing mechanisms on original PDF documents, which would offer a more accurate indication of real-world performance.
> 
> This evolution highlighted a clear need for additional benchmarks, which Document Haystack aims to fill. Document Haystack is introduced as a comprehensive benchmark designed to evaluate VLMs on long, visually complex documents (5 to 200 pages), incorporating pure text or multimodal text+image “needles” at various depths and supported by an objective, automated evaluation framework. It also includes rich metadata to support fine-grained analysis tasks beyond basic retrieval. The provided documents describe this evolution leading up to the introduction of Document Haystack, but they do not mention WikiMixQA.

<details><summary>View Original `search` Tool Output</summary>

```
full_text/2507.15882v2.txt:551::565 (0.2804)
 551: 
 552: While our primary contribution is a benchmark dataset for long context multimodal retrieval challenges, we recognize the importance of enabling more fine-grained analysis tasks. To facilitate this, our dataset release includes comprehensive metadata for each needle, comprising: (1) page location within the document, (2) precise X-Y coordinates on the page, (3) image size, (4) color specifications, and (5) font type and size.
 553: 
 554: This rich metadata will help support various research directions beyond basic retrieval, such as location-aware information extraction, spatial relationship analysis, visual attribute understanding and document layout comprehension. These additional data points provide researchers with the flexibility to design and evaluate more sophisticated tasks that reflect different real-world document processing challenges. We envision this expanded functionality will drive innovation in both model architectures and evaluation methodologies for long context multimodal understanding.
 555: 
 556: 6 Conclusion
 557: 
 558: Document Haystack marks a significant advancement in the evaluation of Visual Language Models (VLMs) by providing a comprehensive benchmark for assessing their performance on long, visually complex documents. Our findings highlight some limitations of current models, underscoring the need for continued research and development. We believe that Document Haystack will serve as a valuable resource for the research community, driving innovation and progress in the field of multimodal document understanding and paving the way for more effective long context VLMs.
 559: 
 560: References
 561: 
 562: [1]
 563: 
 564: Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al.
 565: 

full_text/2507.15882v2.txt:1952::1966 (0.2804)
1952: 
1953: This rich metadata will help support various research directions beyond basic retrieval, such as location-aware information extraction, spatial relationship analysis, visual attribute understanding and document layout comprehension. These additional data points provide researchers with the flexibility to design and evaluate more sophisticated tasks that reflect different real-world document processing challenges. We envision this expanded functionality will drive innovation in both model architectures and evaluation methodologies for long context multimodal understanding.
1954: 
1955: This rich metadata will help support various research directions beyond basic retrieval, such as location-aware information extraction, spatial relationship analysis, visual attribute understanding and document layout comprehension. These additional data points provide researchers with the flexibility to design and evaluate more sophisticated tasks that reflect different real-world document processing challenges. We envision this expanded functionality will drive innovation in both model architectures and evaluation methodologies for long context multimodal understanding.
1956: 
1957: 6 Conclusion
1958: 
1959: Document Haystack marks a significant advancement in the evaluation of Visual Language Models (VLMs) by providing a comprehensive benchmark for assessing their performance on long, visually complex documents. Our findings highlight some limitations of current models, underscoring the need for continued research and development. We believe that Document Haystack will serve as a valuable resource for the research community, driving innovation and progress in the field of multimodal document understanding and paving the way for more effective long context VLMs.
1960: 
1961: 6 CONCLUSION
1962: 
1963: Document Haystack marks a significant advancement in the evaluation of Visual Language Models (VLMs) by providing a comprehensive benchmark for assessing their performance on long, visually complex documents. Our findings highlight some limitations of current models, underscoring the need for continued research and development. We believe that Document Haystack will serve as a valuable resource for the research community, driving innovation and progress in the field of multimodal document understanding and paving the way for more effective long context VLMs.
1964: 
1965: Document Haystack marks a significant advancement in the evaluation of Visual Language Models (VLMs) by providing a comprehensive benchmark for assessing their performance on long, visually complex documents. Our findings highlight some limitations of current models, underscoring the need for continued research and development. We believe that Document Haystack will serve as a valuable resource for the research community, driving innovation and progress in the field of multimodal document understanding and paving the way for more effective long context VLMs.
1966: 

full_text/2507.15882v2.txt:1956::1970 (0.2804)
1956: 
1957: 6 Conclusion
1958: 
1959: Document Haystack marks a significant advancement in the evaluation of Visual Language Models (VLMs) by providing a comprehensive benchmark for assessing their performance on long, visually complex documents. Our findings highlight some limitations of current models, underscoring the need for continued research and development. We believe that Document Haystack will serve as a valuable resource for the research community, driving innovation and progress in the field of multimodal document understanding and paving the way for more effective long context VLMs.
1960: 
1961: 6 CONCLUSION
1962: 
1963: Document Haystack marks a significant advancement in the evaluation of Visual Language Models (VLMs) by providing a comprehensive benchmark for assessing their performance on long, visually complex documents. Our findings highlight some limitations of current models, underscoring the need for continued research and development. We believe that Document Haystack will serve as a valuable resource for the research community, driving innovation and progress in the field of multimodal document understanding and paving the way for more effective long context VLMs.
1964: 
1965: Document Haystack marks a significant advancement in the evaluation of Visual Language Models (VLMs) by providing a comprehensive benchmark for assessing their performance on long, visually complex documents. Our findings highlight some limitations of current models, underscoring the need for continued research and development. We believe that Document Haystack will serve as a valuable resource for the research community, driving innovation and progress in the field of multimodal document understanding and paving the way for more effective long context VLMs.
1966: 
1967: References
1968: 
1969: [1]
1970: 

full_text/2507.15882v2.txt:1958::1972 (0.2804)
1958: 
1959: Document Haystack marks a significant advancement in the evaluation of Visual Language Models (VLMs) by providing a comprehensive benchmark for assessing their performance on long, visually complex documents. Our findings highlight some limitations of current models, underscoring the need for continued research and development. We believe that Document Haystack will serve as a valuable resource for the research community, driving innovation and progress in the field of multimodal document understanding and paving the way for more effective long context VLMs.
1960: 
1961: 6 CONCLUSION
1962: 
1963: Document Haystack marks a significant advancement in the evaluation of Visual Language Models (VLMs) by providing a comprehensive benchmark for assessing their performance on long, visually complex documents. Our findings highlight some limitations of current models, underscoring the need for continued research and development. We believe that Document Haystack will serve as a valuable resource for the research community, driving innovation and progress in the field of multimodal document understanding and paving the way for more effective long context VLMs.
1964: 
1965: Document Haystack marks a significant advancement in the evaluation of Visual Language Models (VLMs) by providing a comprehensive benchmark for assessing their performance on long, visually complex documents. Our findings highlight some limitations of current models, underscoring the need for continued research and development. We believe that Document Haystack will serve as a valuable resource for the research community, driving innovation and progress in the field of multimodal document understanding and paving the way for more effective long context VLMs.
1966: 
1967: References
1968: 
1969: [1]
1970: 
1971: Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al.
1972: 

full_text/2507.15882v2.txt:31::45 (0.2859)
  31: 
  32: 2 Related Work
  33: 
  34: The evaluation of LLMs has traditionally focused on short texts and specific tasks such as question answering, summarization, and translation, with early benchmarks like GLUE [19] and SuperGLUE [20] playing instrumental roles in assessing natural language understanding capabilities. However, while these foundational benchmarks have been valuable, they primarily consist of short texts and tasks that do not require long-term context retention.
  35: 
  36: As LLMs advanced, the need for evaluating longer text comprehension became apparent, leading to the development of specialized long context benchmarks. Notable examples include the Needle in a Haystack [21], which tests models’ ability to retrieve information from extended contexts, and LongBench [22], which introduced the first bilingual, multi-task framework for assessing long-form text understanding.
  37: 
  38: The emergence of multimodal VLMs necessitated new evaluation approaches. Benchmarks such as VQA [23], NLVR [24], and MileBench [25] were developed to assess models’ capabilities in processing and reasoning about combined visual and textual information. Document understanding then emerged as a distinct challenge in multimodal evaluation. While early datasets focused on specific elements like charts [26] or single-page analysis [27], recent benchmarks such as DUDE [28], Loong [29], SlideVQA [30], and MMLongBench-Doc [31] attempted to tackle multi-page document comprehension.
  39: 
  40: Despite these advancements, there remains a significant gap in benchmarks that evaluate VLMs’ performance on long, multimodal documents. Existing benchmarks either (1) lack the document length (<<50 pages), (2) rely on independently pre-extracted text and images rather than original documents, or (3) don’t allow a performance comparison of a similar task on different document lengths. While recently released benchmarks like MM-NIAH [32] and M-LongDoc [33] address some of these issues, they have their own constraints. MM-NIAH’s limited prompt length (<<72k tokens) makes it unsuitable for long document evaluation, while M-LongDoc, despite featuring documents spanning hundreds of pages, offers only 851 questions, employs a non-objective evaluation method, and doesn’t support evaluating the same task with varying document lengths. Moreover, both rely on pre-extracting text and figures from the documents. This preprocessing approach prevents VLM providers from utilizing their native processing mechanisms on original PDF documents, which would provide a more accurate indication of their real-world performance. Although they are valuable contributions, there is a clear need for additional benchmarks. Document Haystack aims to fill this void.
  41: 
  42: 3 Benchmark Characteristics
  43: 
  44: Document Haystack is a comprehensive benchmark designed to evaluate the performance of VLMs in retrieving key multimodal information from long documents. The following sections detail the essential characteristics of our benchmark.
  45: 

full_text/2507.15882v2.txt:908::922 (0.2859)
 908: 
 909: 2 Related Work
 910: 
 911: The evaluation of LLMs has traditionally focused on short texts and specific tasks such as question answering, summarization, and translation, with early benchmarks like GLUE [19] and SuperGLUE [20] playing instrumental roles in assessing natural language understanding capabilities. However, while these foundational benchmarks have been valuable, they primarily consist of short texts and tasks that do not require long-term context retention.
 912: 
 913: As LLMs advanced, the need for evaluating longer text comprehension became apparent, leading to the development of specialized long context benchmarks. Notable examples include the Needle in a Haystack [21], which tests models’ ability to retrieve information from extended contexts, and LongBench [22], which introduced the first bilingual, multi-task framework for assessing long-form text understanding.
 914: 
 915: The emergence of multimodal VLMs necessitated new evaluation approaches. Benchmarks such as VQA [23], NLVR [24], and MileBench [25] were developed to assess models’ capabilities in processing and reasoning about combined visual and textual information. Document understanding then emerged as a distinct challenge in multimodal evaluation. While early datasets focused on specific elements like charts [26] or single-page analysis [27], recent benchmarks such as DUDE [28], Loong [29], SlideVQA [30], and MMLongBench-Doc [31] attempted to tackle multi-page document comprehension.
 916: 
 917: Despite these advancements, there remains a significant gap in benchmarks that evaluate VLMs’ performance on long, multimodal documents. Existing benchmarks either (1) lack the document length (<<50 pages), (2) rely on independently pre-extracted text and images rather than original documents, or (3) don’t allow a performance comparison of a similar task on different document lengths. While recently released benchmarks like MM-NIAH [32] and M-LongDoc [33] address some of these issues, they have their own constraints. MM-NIAH’s limited prompt length (<<72k tokens) makes it unsuitable for long document evaluation, while M-LongDoc, despite featuring documents spanning hundreds of pages, offers only 851 questions, employs a non-objective evaluation method, and doesn’t support evaluating the same task with varying document lengths. Moreover, both rely on pre-extracting text and figures from the documents. This preprocessing approach prevents VLM providers from utilizing their native processing mechanisms on original PDF documents, which would provide a more accurate indication of their real-world performance. Although they are valuable contributions, there is a clear need for additional benchmarks. Document Haystack aims to fill this void.
 918: 
 919: 2 RELATED WORK
 920: 
 921: The evaluation of LLMs has traditionally focused on short texts and specific tasks such as question answering, summarization, and translation, with early benchmarks like GLUE [19] and SuperGLUE [20] playing instrumental roles in assessing natural language understanding capabilities. However, while these foundational benchmarks have been valuable, they primarily consist of short texts and tasks that do not require long-term context retention.
 922: 

full_text/2507.15882v2.txt:922::936 (0.2859)
 922: 
 923: The evaluation of LLMs has traditionally focused on short texts and specific tasks such as question answering, summarization, and translation, with early benchmarks like GLUE [19] and SuperGLUE [20] playing instrumental roles in assessing natural language understanding capabilities. However, while these foundational benchmarks have been valuable, they primarily consist of short texts and tasks that do not require long-term context retention.
 924: 
 925: As LLMs advanced, the need for evaluating longer text comprehension became apparent, leading to the development of specialized long context benchmarks. Notable examples include the Needle in a Haystack [21], which tests models’ ability to retrieve information from extended contexts, and LongBench [22], which introduced the first bilingual, multi-task framework for assessing long-form text understanding.
 926: 
 927: As LLMs advanced, the need for evaluating longer text comprehension became apparent, leading to the development of specialized long context benchmarks. Notable examples include the Needle in a Haystack [21], which tests models’ ability to retrieve information from extended contexts, and LongBench [22], which introduced the first bilingual, multi-task framework for assessing long-form text understanding.
 928: 
 929: The emergence of multimodal VLMs necessitated new evaluation approaches. Benchmarks such as VQA [23], NLVR [24], and MileBench [25] were developed to assess models’ capabilities in processing and reasoning about combined visual and textual information. Document understanding then emerged as a distinct challenge in multimodal evaluation. While early datasets focused on specific elements like charts [26] or single-page analysis [27], recent benchmarks such as DUDE [28], Loong [29], SlideVQA [30], and MMLongBench-Doc [31] attempted to tackle multi-page document comprehension.
 930: 
 931: The emergence of multimodal VLMs necessitated new evaluation approaches. Benchmarks such as VQA [23], NLVR [24], and MileBench [25] were developed to assess models’ capabilities in processing and reasoning about combined visual and textual information. Document understanding then emerged as a distinct challenge in multimodal evaluation. While early datasets focused on specific elements like charts [26] or single-page analysis [27], recent benchmarks such as DUDE [28], Loong [29], SlideVQA [30], and MMLongBench-Doc [31] attempted to tackle multi-page document comprehension.
 932: 
 933: Despite these advancements, there remains a significant gap in benchmarks that evaluate VLMs’ performance on long, multimodal documents. Existing benchmarks either (1) lack the document length (<<50 pages), (2) rely on independently pre-extracted text and images rather than original documents, or (3) don’t allow a performance comparison of a similar task on different document lengths. While recently released benchmarks like MM-NIAH [32] and M-LongDoc [33] address some of these issues, they have their own constraints. MM-NIAH’s limited prompt length (<<72k tokens) makes it unsuitable for long document evaluation, while M-LongDoc, despite featuring documents spanning hundreds of pages, offers only 851 questions, employs a non-objective evaluation method, and doesn’t support evaluating the same task with varying document lengths. Moreover, both rely on pre-extracting text and figures from the documents. This preprocessing approach prevents VLM providers from utilizing their native processing mechanisms on original PDF documents, which would provide a more accurate indication of their real-world performance. Although they are valuable contributions, there is a clear need for additional benchmarks. Document Haystack aims to fill this void.
 934: 
 935: Despite these advancements, there remains a significant gap in benchmarks that evaluate VLMs’ performance on long, multimodal documents. Existing benchmarks either (1) lack the document length (<<50 pages), (2) rely on independently pre-extracted text and images rather than original documents, or (3) don’t allow a performance comparison of a similar task on different document lengths. While recently released benchmarks like MM-NIAH [32] and M-LongDoc [33] address some of these issues, they have their own constraints. MM-NIAH’s limited prompt length (<<72k tokens) makes it unsuitable for long document evaluation, while M-LongDoc, despite featuring documents spanning hundreds of pages, offers only 851 questions, employs a non-objective evaluation method, and doesn’t support evaluating the same task with varying document lengths. Moreover, both rely on pre-extracting text and figures from the documents. This preprocessing approach prevents VLM providers from utilizing their native processing mechanisms on original PDF documents, which would provide a more accurate indication of their real-world performance. Although they are valuable contributions, there is a clear need for additional benchmarks. Document Haystack aims to fill this void.
 936: 

full_text/2507.15882v2.txt:924::938 (0.2859)
 924: 
 925: As LLMs advanced, the need for evaluating longer text comprehension became apparent, leading to the development of specialized long context benchmarks. Notable examples include the Needle in a Haystack [21], which tests models’ ability to retrieve information from extended contexts, and LongBench [22], which introduced the first bilingual, multi-task framework for assessing long-form text understanding.
 926: 
 927: As LLMs advanced, the need for evaluating longer text comprehension became apparent, leading to the development of specialized long context benchmarks. Notable examples include the Needle in a Haystack [21], which tests models’ ability to retrieve information from extended contexts, and LongBench [22], which introduced the first bilingual, multi-task framework for assessing long-form text understanding.
 928: 
 929: The emergence of multimodal VLMs necessitated new evaluation approaches. Benchmarks such as VQA [23], NLVR [24], and MileBench [25] were developed to assess models’ capabilities in processing and reasoning about combined visual and textual information. Document understanding then emerged as a distinct challenge in multimodal evaluation. While early datasets focused on specific elements like charts [26] or single-page analysis [27], recent benchmarks such as DUDE [28], Loong [29], SlideVQA [30], and MMLongBench-Doc [31] attempted to tackle multi-page document comprehension.
 930: 
 931: The emergence of multimodal VLMs necessitated new evaluation approaches. Benchmarks such as VQA [23], NLVR [24], and MileBench [25] were developed to assess models’ capabilities in processing and reasoning about combined visual and textual information. Document understanding then emerged as a distinct challenge in multimodal evaluation. While early datasets focused on specific elements like charts [26] or single-page analysis [27], recent benchmarks such as DUDE [28], Loong [29], SlideVQA [30], and MMLongBench-Doc [31] attempted to tackle multi-page document comprehension.
 932: 
 933: Despite these advancements, there remains a significant gap in benchmarks that evaluate VLMs’ performance on long, multimodal documents. Existing benchmarks either (1) lack the document length (<<50 pages), (2) rely on independently pre-extracted text and images rather than original documents, or (3) don’t allow a performance comparison of a similar task on different document lengths. While recently released benchmarks like MM-NIAH [32] and M-LongDoc [33] address some of these issues, they have their own constraints. MM-NIAH’s limited prompt length (<<72k tokens) makes it unsuitable for long document evaluation, while M-LongDoc, despite featuring documents spanning hundreds of pages, offers only 851 questions, employs a non-objective evaluation method, and doesn’t support evaluating the same task with varying document lengths. Moreover, both rely on pre-extracting text and figures from the documents. This preprocessing approach prevents VLM providers from utilizing their native processing mechanisms on original PDF documents, which would provide a more accurate indication of their real-world performance. Although they are valuable contributions, there is a clear need for additional benchmarks. Document Haystack aims to fill this void.
 934: 
 935: Despite these advancements, there remains a significant gap in benchmarks that evaluate VLMs’ performance on long, multimodal documents. Existing benchmarks either (1) lack the document length (<<50 pages), (2) rely on independently pre-extracted text and images rather than original documents, or (3) don’t allow a performance comparison of a similar task on different document lengths. While recently released benchmarks like MM-NIAH [32] and M-LongDoc [33] address some of these issues, they have their own constraints. MM-NIAH’s limited prompt length (<<72k tokens) makes it unsuitable for long document evaluation, while M-LongDoc, despite featuring documents spanning hundreds of pages, offers only 851 questions, employs a non-objective evaluation method, and doesn’t support evaluating the same task with varying document lengths. Moreover, both rely on pre-extracting text and figures from the documents. This preprocessing approach prevents VLM providers from utilizing their native processing mechanisms on original PDF documents, which would provide a more accurate indication of their real-world performance. Although they are valuable contributions, there is a clear need for additional benchmarks. Document Haystack aims to fill this void.
 936: 
 937: 3 Benchmark Characteristics
 938: 

full_text/2507.15882v2.txt:9::23 (0.2863)
   9: Srinivasan Veeravanallur
  10: 
  11: Amazon AGI
  12: 
  13: {huybrech,ronanks,saimucja,jgmf,srivee}@amazon.com
  14: 
  15: Abstract
  16: The proliferation of multimodal Large Language Models has significantly advanced the ability to analyze and understand complex data inputs from different modalities. However, the processing of long documents remains under-explored, largely due to a lack of suitable benchmarks. To address this, we introduce Document Haystack111Dataset: https://huggingface.co/datasets/AmazonScience/document-haystack222Code: https://github.com/amazon-science/document-haystack, a comprehensive benchmark designed to evaluate the performance of Vision Language Models (VLMs) on long, visually complex documents. Document Haystack features documents ranging from 5 to 200 pages and strategically inserts pure text or multimodal text+image “needles” at various depths within the documents to challenge VLMs’ retrieval capabilities. Comprising 400 document variants and a total of 8,250 questions, it is supported by an objective, automated evaluation framework. We detail the construction and characteristics of the Document Haystack dataset, present results from prominent VLMs and discuss potential research avenues in this area.
  17: 
  18: 1 Introduction
  19: 
  20: Large Language Models (LLMs) [1, 2, 3, 4] have fundamentally transformed natural language processing, demonstrating unprecedented capabilities in understanding and generating human-like text. This transformation has recently expanded with the emergence of multimodal LLMs, including GPT-4 [5], Gemini 1.5 [6], LLama 3.2 [7], Claude 3 [8], and Nova [9]. These advanced models excel at diverse tasks, from image captioning [10] to video reasoning [11] and speech translation [12].
  21: 
  22: A particularly significant advancement has been in document understanding capabilities. This field is crucial across numerous domains, with particular importance in legal [13, 14], medical [15, 16], and financial sectors [17, 18], where accurate document interpretation directly impacts decision-making and regulatory compliance. The integration of LLMs has markedly improved key aspects of document processing, including information extraction accuracy, contextual understanding and question-answering capabilities based on document content.
  23: 

full_text/2507.15882v2.txt:856::870 (0.2863)
 856: Srinivasan Veeravanallur
 857: 
 858: Amazon AGI
 859: 
 860: {huybrech,ronanks,saimucja,jgmf,srivee}@amazon.com
 861: 
 862: Abstract
 863: The proliferation of multimodal Large Language Models has significantly advanced the ability to analyze and understand complex data inputs from different modalities. However, the processing of long documents remains under-explored, largely due to a lack of suitable benchmarks. To address this, we introduce Document Haystack111Dataset: https://huggingface.co/datasets/AmazonScience/document-haystack222Code: https://github.com/amazon-science/document-haystack, a comprehensive benchmark designed to evaluate the performance of Vision Language Models (VLMs) on long, visually complex documents. Document Haystack features documents ranging from 5 to 200 pages and strategically inserts pure text or multimodal text+image “needles” at various depths within the documents to challenge VLMs’ retrieval capabilities. Comprising 400 document variants and a total of 8,250 questions, it is supported by an objective, automated evaluation framework. We detail the construction and characteristics of the Document Haystack dataset, present results from prominent VLMs and discuss potential research avenues in this area.
 864: 
 865: ABSTRACT
 866: 
 867: The proliferation of multimodal Large Language Models has significantly advanced the ability to analyze and understand complex data inputs from different modalities. However, the processing of long documents remains under-explored, largely due to a lack of suitable benchmarks. To address this, we introduce Document Haystack111Dataset: https://huggingface.co/datasets/AmazonScience/document-haystack222Code: https://github.com/amazon-science/document-haystack, a comprehensive benchmark designed to evaluate the performance of Vision Language Models (VLMs) on long, visually complex documents. Document Haystack features documents ranging from 5 to 200 pages and strategically inserts pure text or multimodal text+image “needles” at various depths within the documents to challenge VLMs’ retrieval capabilities. Comprising 400 document variants and a total of 8,250 questions, it is supported by an objective, automated evaluation framework. We detail the construction and characteristics of the Document Haystack dataset, present results from prominent VLMs and discuss potential research avenues in this area.
 868: 
 869: 1 Introduction
 870: 


```

</details>


---

### 9. Query: According to Zhang et al. (`2508.15370v1.txt`), what were the specific extensions and improvements made in the journal version of their MultiTrust benchmark compared to its NeurIPS conference version, regarding framework dimensions, analysis of mitigation methods, and evaluated MLLMs?

- **Query ID:** `temporal_3`
- **Query Type:** Temporal
- **Curated Source Files:** `full_text/2505.07796v2.txt, full_text/2506.15594v1.txt, full_text/2506.22309v1.txt, full_text/2507.15152v1.txt, full_text/2508.14302v1.txt, full_text/2508.15370v1.txt`

#### LLM Ground Truth Answer

> The journal version of the MultiTrust benchmark, referred to as MultiTrust-X, built upon its NeurIPS conference predecessor (`[92]` in references) with several key extensions and improvements. These include: (1) **Expanded Framework Dimensions:** The original framework was enhanced to a more comprehensive three-dimensional structure for assessing MLLM trustworthiness. (2) **In-depth Analysis of Mitigation Methods:** MultiTrust-X incorporated a detailed analysis of 8 representative mitigation approaches, categorized by machine learning system stages (data, architecture, training, inference), providing practical insights. (3) **Extended Model Evaluation:** The evaluation scope was broadened to include 9 additional modern MLLMs, encompassing both closed-source (e.g., GPT-4o, Hunyuan-V) and open-source models (e.g., Phi-Vision, Cambrian-8B). (4) **Novel Mitigation Method:** A new approach, Reasoning-Enhanced Safety Alignment (RESA), was proposed based on analysis insights to improve utility and achieve state-of-the-art performance. (5) **Manuscript Restructuring:** The manuscript itself was substantially rewritten and restructured with new sections and updated figures to enhance clarity and completeness.

**Source Document(s):** `full_text/2508.15370v1.txt`

#### `search` Tool Performance

**Command Executed:**

```bash
search "According to Zhang et al. (`2508.15370v1.txt`), what were the specific extensions and improvements made in the journal version of their MultiTrust benchmark compared to its NeurIPS conference version, regarding framework dimensions, analysis of mitigation methods, and evaluated MLLMs?" full_text/*.txt --top-k 10 --n-lines 7
```

**Retrieval Precision:** `0.50`
**Retrieval Recall:** `1.00`

**Documents Returned by `search`:** `full_text/2508.12096v2.txt, full_text/2508.15370v1.txt`

#### LLM Search-Augmented Answer

> According to Zhang et al. (`2508.15370v1.txt`), the journal version of their MultiTrust benchmark, referred to as MultiTrust-X, includes several specific extensions and improvements compared to its NeurIPS conference version:
> 
> 1.  **Framework Dimensions:** The original MultiTrust benchmark was expanded with a new dimension, creating a more comprehensive three-dimensional framework, MultiTrust-X, for assessing the trustworthiness of Multimodal Large Language Models (MLLMs).
> 
> 2.  **Analysis of Mitigation Methods:** MultiTrust-X incorporates an in-depth analysis of mitigation methods from a machine learning perspective. This involved examining 8 representative approaches that target hallucination, adversarial robustness, and safety. Controlled experiments were conducted to derive practical insights for improving the overall trustworthiness of MLLMs.
> 
> 3.  **Evaluated MLLMs:** The evaluation was expanded to include 9 additional modern MLLMs. These additions comprise both closed-source models, such as GPT-4o and Hunyuan-V, and open-source models, including Phi-Vision and Cambrian-8B. This expansion aimed to strengthen conclusions and highlight the ongoing significance of trustworthiness challenges.

<details><summary>View Original `search` Tool Output</summary>

```
full_text/2508.15370v1.txt:31::45 (0.2957)
  31: 
  32: Based on the extensive evaluation results, we uncover significant trustworthiness issues. We first identify the gap from open-source MLLMs to proprietary models in trustworthiness, rendering the limited correlation between trustworthiness and general capabilities. Delving into the experimental results of each aspect, we uncover several critical issues including vulnerabilities to multimodal jailbreaking and adversarial attacks, and tendencies to disclose privacy or display biases with multimodal inputs. These findings highlight the intricate challenges posed by the multimodal nature of MLLMs.
  33: 
  34: Furthermore, we conduct a detailed case study to rigorously assess the effectiveness of mitigation methods in facilitating trustworthiness on a subset of tasks. The analysis shows that none of the current approaches yield all-round improvements. Concretely, we observe that methods targeting hallucination are ineffective in reducing safety risks, and that safety training using refusal data or replacing the visual encoder with a more robust alternative often introduces trade-offs between safety and helpfulness. Inspired by the recent advancements in Large Reasoning Models like DeepSeek-R1 [30], we examine the effect of reasoning data for risk mitigation [93] and notice that, compared to direct answers, deliberative analysis achieves similar safety performance as refusal training while better preserves the general utility of the model.
  35: 
  36: Building on our analysis, we propose Reasoning-Enhanced Safety Alignment (RESA), a simple yet effective mitigation method that achieves state-of-the-art performance on MultiTrust-X among open-source MLLMs. Specifically, we restructure VLGuard data [102] into chain-of-thought format for supervised fine-tuning and replace the visual encoder with the robust FARECLIP [64]. This modification raises LLaVA-v1.5-7B’s overall score from 48.45 to 69.66, surpassing Phi-3.5-Vision [2] (66.29), which was previously the highest-performing model due to extensive safety alignment before release. Our approach significantly narrows the trustworthiness gap between open-source and proprietary MLLMs.
  37: 
  38: This journal paper is an extended version of our NeurIPS paper [92]. Compared with the conference version, we have made significant improvements and extensions: (1) We expand the original benchmark of MultiTrust with a new dimension, which constructs a more comprehensive three-dimensional framework, MultiTrust-X, for assessing the trustworthiness of MLLMs (Fig. 1). Beyond simply evaluating existing models, MultiTrust-X incorporates in-depth analysis of mitigation methods from a machine learning perspective. Specifically, we examine 8 representative approaches targeting hallucination, adversarial robustness, and safety, and conduct controlled experiments to derive practical insights for improving the overall trustworthiness of MLLMs. The extended framework is introduced in Section III-C and the detailed analysis is presented in Section V. (2) Based on the insights from analysis, we propose a novel mitigation method, Reasoning-Enhanced Safety Alignment (RESA), which better preserves the general utility and achieves the state-of-the-art performance on MultiTrust-X. The implementation details and experimental results are included in Section VI. (3) We expand our evaluation to include 9 additional modern MLLMs, including closed-source models such as GPT-4o and Hunyuan-V, and open-source models like Phi-Vision and Cambrian-8B. These additions strengthen our conclusions and highlight the continued significance of trustworthiness challenges. (4) We have also substantially restructured and rewritten the manuscript, adding new sections, including Sections III-C, V and VI, as well as updating some figures to enhance the clarity and completeness of this paper.
  39: 
  40: The rest of this paper is structured as follows: Section II reviews the related works of MLLMs and their trustworthiness. Section III describes the overall design of MultiTrust-X in both its framework and the implementations. Section IV presents the benchmarking results of modern MLLMs and Section V provides a more in-depth analysis of relevant mitigation methods with some practical insights. Section VI introduces our newly proposed mitigation method that is based on reasoning. Section VII concludes the paper.
  41: 
  42: II Related Work
  43: 
  44: TABLE I: Comparison between MultiTrust and other trustworthiness-related benchmarks for MLLMs. The numbers in the parenthesis for # MLLM represent the counts of proprietary models.
  45: 

full_text/2508.15370v1.txt:2499::2513 (0.2957)
2499: 
2500: Based on the extensive evaluation results, we uncover significant trustworthiness issues. We first identify the gap from open-source MLLMs to proprietary models in trustworthiness, rendering the limited correlation between trustworthiness and general capabilities. Delving into the experimental results of each aspect, we uncover several critical issues including vulnerabilities to multimodal jailbreaking and adversarial attacks, and tendencies to disclose privacy or display biases with multimodal inputs. These findings highlight the intricate challenges posed by the multimodal nature of MLLMs.
2501: 
2502: Furthermore, we conduct a detailed case study to rigorously assess the effectiveness of mitigation methods in facilitating trustworthiness on a subset of tasks. The analysis shows that none of the current approaches yield all-round improvements. Concretely, we observe that methods targeting hallucination are ineffective in reducing safety risks, and that safety training using refusal data or replacing the visual encoder with a more robust alternative often introduces trade-offs between safety and helpfulness. Inspired by the recent advancements in Large Reasoning Models like DeepSeek-R1 [30], we examine the effect of reasoning data for risk mitigation [93] and notice that, compared to direct answers, deliberative analysis achieves similar safety performance as refusal training while better preserves the general utility of the model.
2503: 
2504: Building on our analysis, we propose Reasoning-Enhanced Safety Alignment (RESA), a simple yet effective mitigation method that achieves state-of-the-art performance on MultiTrust-X among open-source MLLMs. Specifically, we restructure VLGuard data [102] into chain-of-thought format for supervised fine-tuning and replace the visual encoder with the robust FARECLIP [64]. This modification raises LLaVA-v1.5-7B’s overall score from 48.45 to 69.66, surpassing Phi-3.5-Vision [2] (66.29), which was previously the highest-performing model due to extensive safety alignment before release. Our approach significantly narrows the trustworthiness gap between open-source and proprietary MLLMs.
2505: 
2506: This journal paper is an extended version of our NeurIPS paper [92]. Compared with the conference version, we have made significant improvements and extensions: (1) We expand the original benchmark of MultiTrust with a new dimension, which constructs a more comprehensive three-dimensional framework, MultiTrust-X, for assessing the trustworthiness of MLLMs (Fig. 1). Beyond simply evaluating existing models, MultiTrust-X incorporates in-depth analysis of mitigation methods from a machine learning perspective. Specifically, we examine 8 representative approaches targeting hallucination, adversarial robustness, and safety, and conduct controlled experiments to derive practical insights for improving the overall trustworthiness of MLLMs. The extended framework is introduced in Section III-C and the detailed analysis is presented in Section V. (2) Based on the insights from analysis, we propose a novel mitigation method, Reasoning-Enhanced Safety Alignment (RESA), which better preserves the general utility and achieves the state-of-the-art performance on MultiTrust-X. The implementation details and experimental results are included in Section VI. (3) We expand our evaluation to include 9 additional modern MLLMs, including closed-source models such as GPT-4o and Hunyuan-V, and open-source models like Phi-Vision and Cambrian-8B. These additions strengthen our conclusions and highlight the continued significance of trustworthiness challenges. (4) We have also substantially restructured and rewritten the manuscript, adding new sections, including Sections III-C, V and VI, as well as updating some figures to enhance the clarity and completeness of this paper.
2507: 
2508: The rest of this paper is structured as follows: Section II reviews the related works of MLLMs and their trustworthiness. Section III describes the overall design of MultiTrust-X in both its framework and the implementations. Section IV presents the benchmarking results of modern MLLMs and Section V provides a more in-depth analysis of relevant mitigation methods with some practical insights. Section VI introduces our newly proposed mitigation method that is based on reasoning. Section VII concludes the paper.
2509: 
2510: I INTRODUCTION
2511: 
2512: Large Language Models (LLMs) [3][4][35][74] have demonstrated exceptional abilities in language comprehension and reasoning, representing a significant step towards Artificial General Intelligence (AGI) [25]. Leveraging their versatility, recent developments have extended LLMs beyond text to incorporate additional modalities such as vision, leading to Multimodal Large Language Models (MLLMs) [19][46][57][69][101], which excel in diverse multimodal tasks and are increasingly applied across various scenarios [24][31][50][88]. However, MLLMs also present serious concerns regarding trustworthiness, such as factual inaccuracies [6][90], harmful content generation [60][103], and privacy leakage [51][55], which pose critical challenges to the reliability and safety in applications and highlight the significance of further research to tackle them [1][23].
2513: 

full_text/2508.15370v1.txt:2537::2551 (0.2957)
2537: 
2538: Furthermore, we conduct a detailed case study to rigorously assess the effectiveness of mitigation methods in facilitating trustworthiness on a subset of tasks. The analysis shows that none of the current approaches yield all-round improvements. Concretely, we observe that methods targeting hallucination are ineffective in reducing safety risks, and that safety training using refusal data or replacing the visual encoder with a more robust alternative often introduces trade-offs between safety and helpfulness. Inspired by the recent advancements in Large Reasoning Models like DeepSeek-R1 [30], we examine the effect of reasoning data for risk mitigation [93] and notice that, compared to direct answers, deliberative analysis achieves similar safety performance as refusal training while better preserves the general utility of the model.
2539: 
2540: Building on our analysis, we propose Reasoning-Enhanced Safety Alignment (RESA), a simple yet effective mitigation method that achieves state-of-the-art performance on MultiTrust-X among open-source MLLMs. Specifically, we restructure VLGuard data [102] into chain-of-thought format for supervised fine-tuning and replace the visual encoder with the robust FARECLIP [64]. This modification raises LLaVA-v1.5-7B’s overall score from 48.45 to 69.66, surpassing Phi-3.5-Vision [2] (66.29), which was previously the highest-performing model due to extensive safety alignment before release. Our approach significantly narrows the trustworthiness gap between open-source and proprietary MLLMs.
2541: 
2542: Building on our analysis, we propose Reasoning-Enhanced Safety Alignment (RESA), a simple yet effective mitigation method that achieves state-of-the-art performance on MultiTrust-X among open-source MLLMs. Specifically, we restructure VLGuard data [102] into chain-of-thought format for supervised fine-tuning and replace the visual encoder with the robust FARECLIP [64]. This modification raises LLaVA-v1.5-7B’s overall score from 48.45 to 69.66, surpassing Phi-3.5-Vision [2] (66.29), which was previously the highest-performing model due to extensive safety alignment before release. Our approach significantly narrows the trustworthiness gap between open-source and proprietary MLLMs.
2543: 
2544: This journal paper is an extended version of our NeurIPS paper [92]. Compared with the conference version, we have made significant improvements and extensions: (1) We expand the original benchmark of MultiTrust with a new dimension, which constructs a more comprehensive three-dimensional framework, MultiTrust-X, for assessing the trustworthiness of MLLMs (Fig. 1). Beyond simply evaluating existing models, MultiTrust-X incorporates in-depth analysis of mitigation methods from a machine learning perspective. Specifically, we examine 8 representative approaches targeting hallucination, adversarial robustness, and safety, and conduct controlled experiments to derive practical insights for improving the overall trustworthiness of MLLMs. The extended framework is introduced in Section III-C and the detailed analysis is presented in Section V. (2) Based on the insights from analysis, we propose a novel mitigation method, Reasoning-Enhanced Safety Alignment (RESA), which better preserves the general utility and achieves the state-of-the-art performance on MultiTrust-X. The implementation details and experimental results are included in Section VI. (3) We expand our evaluation to include 9 additional modern MLLMs, including closed-source models such as GPT-4o and Hunyuan-V, and open-source models like Phi-Vision and Cambrian-8B. These additions strengthen our conclusions and highlight the continued significance of trustworthiness challenges. (4) We have also substantially restructured and rewritten the manuscript, adding new sections, including Sections III-C, V and VI, as well as updating some figures to enhance the clarity and completeness of this paper.
2545: 
2546: This journal paper is an extended version of our NeurIPS paper [92]. Compared with the conference version, we have made significant improvements and extensions: (1) We expand the original benchmark of MultiTrust with a new dimension, which constructs a more comprehensive three-dimensional framework, MultiTrust-X, for assessing the trustworthiness of MLLMs (Fig. 1). Beyond simply evaluating existing models, MultiTrust-X incorporates in-depth analysis of mitigation methods from a machine learning perspective. Specifically, we examine 8 representative approaches targeting hallucination, adversarial robustness, and safety, and conduct controlled experiments to derive practical insights for improving the overall trustworthiness of MLLMs. The extended framework is introduced in Section III-C and the detailed analysis is presented in Section V. (2) Based on the insights from analysis, we propose a novel mitigation method, Reasoning-Enhanced Safety Alignment (RESA), which better preserves the general utility and achieves the state-of-the-art performance on MultiTrust-X. The implementation details and experimental results are included in Section VI. (3) We expand our evaluation to include 9 additional modern MLLMs, including closed-source models such as GPT-4o and Hunyuan-V, and open-source models like Phi-Vision and Cambrian-8B. These additions strengthen our conclusions and highlight the continued significance of trustworthiness challenges. (4) We have also substantially restructured and rewritten the manuscript, adding new sections, including Sections III-C, V and VI, as well as updating some figures to enhance the clarity and completeness of this paper.
2547: 
2548: The rest of this paper is structured as follows: Section II reviews the related works of MLLMs and their trustworthiness. Section III describes the overall design of MultiTrust-X in both its framework and the implementations. Section IV presents the benchmarking results of modern MLLMs and Section V provides a more in-depth analysis of relevant mitigation methods with some practical insights. Section VI introduces our newly proposed mitigation method that is based on reasoning. Section VII concludes the paper.
2549: 
2550: The rest of this paper is structured as follows: Section II reviews the related works of MLLMs and their trustworthiness. Section III describes the overall design of MultiTrust-X in both its framework and the implementations. Section IV presents the benchmarking results of modern MLLMs and Section V provides a more in-depth analysis of relevant mitigation methods with some practical insights. Section VI introduces our newly proposed mitigation method that is based on reasoning. Section VII concludes the paper.
2551: 

full_text/2508.15370v1.txt:2539::2553 (0.2957)
2539: 
2540: Building on our analysis, we propose Reasoning-Enhanced Safety Alignment (RESA), a simple yet effective mitigation method that achieves state-of-the-art performance on MultiTrust-X among open-source MLLMs. Specifically, we restructure VLGuard data [102] into chain-of-thought format for supervised fine-tuning and replace the visual encoder with the robust FARECLIP [64]. This modification raises LLaVA-v1.5-7B’s overall score from 48.45 to 69.66, surpassing Phi-3.5-Vision [2] (66.29), which was previously the highest-performing model due to extensive safety alignment before release. Our approach significantly narrows the trustworthiness gap between open-source and proprietary MLLMs.
2541: 
2542: Building on our analysis, we propose Reasoning-Enhanced Safety Alignment (RESA), a simple yet effective mitigation method that achieves state-of-the-art performance on MultiTrust-X among open-source MLLMs. Specifically, we restructure VLGuard data [102] into chain-of-thought format for supervised fine-tuning and replace the visual encoder with the robust FARECLIP [64]. This modification raises LLaVA-v1.5-7B’s overall score from 48.45 to 69.66, surpassing Phi-3.5-Vision [2] (66.29), which was previously the highest-performing model due to extensive safety alignment before release. Our approach significantly narrows the trustworthiness gap between open-source and proprietary MLLMs.
2543: 
2544: This journal paper is an extended version of our NeurIPS paper [92]. Compared with the conference version, we have made significant improvements and extensions: (1) We expand the original benchmark of MultiTrust with a new dimension, which constructs a more comprehensive three-dimensional framework, MultiTrust-X, for assessing the trustworthiness of MLLMs (Fig. 1). Beyond simply evaluating existing models, MultiTrust-X incorporates in-depth analysis of mitigation methods from a machine learning perspective. Specifically, we examine 8 representative approaches targeting hallucination, adversarial robustness, and safety, and conduct controlled experiments to derive practical insights for improving the overall trustworthiness of MLLMs. The extended framework is introduced in Section III-C and the detailed analysis is presented in Section V. (2) Based on the insights from analysis, we propose a novel mitigation method, Reasoning-Enhanced Safety Alignment (RESA), which better preserves the general utility and achieves the state-of-the-art performance on MultiTrust-X. The implementation details and experimental results are included in Section VI. (3) We expand our evaluation to include 9 additional modern MLLMs, including closed-source models such as GPT-4o and Hunyuan-V, and open-source models like Phi-Vision and Cambrian-8B. These additions strengthen our conclusions and highlight the continued significance of trustworthiness challenges. (4) We have also substantially restructured and rewritten the manuscript, adding new sections, including Sections III-C, V and VI, as well as updating some figures to enhance the clarity and completeness of this paper.
2545: 
2546: This journal paper is an extended version of our NeurIPS paper [92]. Compared with the conference version, we have made significant improvements and extensions: (1) We expand the original benchmark of MultiTrust with a new dimension, which constructs a more comprehensive three-dimensional framework, MultiTrust-X, for assessing the trustworthiness of MLLMs (Fig. 1). Beyond simply evaluating existing models, MultiTrust-X incorporates in-depth analysis of mitigation methods from a machine learning perspective. Specifically, we examine 8 representative approaches targeting hallucination, adversarial robustness, and safety, and conduct controlled experiments to derive practical insights for improving the overall trustworthiness of MLLMs. The extended framework is introduced in Section III-C and the detailed analysis is presented in Section V. (2) Based on the insights from analysis, we propose a novel mitigation method, Reasoning-Enhanced Safety Alignment (RESA), which better preserves the general utility and achieves the state-of-the-art performance on MultiTrust-X. The implementation details and experimental results are included in Section VI. (3) We expand our evaluation to include 9 additional modern MLLMs, including closed-source models such as GPT-4o and Hunyuan-V, and open-source models like Phi-Vision and Cambrian-8B. These additions strengthen our conclusions and highlight the continued significance of trustworthiness challenges. (4) We have also substantially restructured and rewritten the manuscript, adding new sections, including Sections III-C, V and VI, as well as updating some figures to enhance the clarity and completeness of this paper.
2547: 
2548: The rest of this paper is structured as follows: Section II reviews the related works of MLLMs and their trustworthiness. Section III describes the overall design of MultiTrust-X in both its framework and the implementations. Section IV presents the benchmarking results of modern MLLMs and Section V provides a more in-depth analysis of relevant mitigation methods with some practical insights. Section VI introduces our newly proposed mitigation method that is based on reasoning. Section VII concludes the paper.
2549: 
2550: The rest of this paper is structured as follows: Section II reviews the related works of MLLMs and their trustworthiness. Section III describes the overall design of MultiTrust-X in both its framework and the implementations. Section IV presents the benchmarking results of modern MLLMs and Section V provides a more in-depth analysis of relevant mitigation methods with some practical insights. Section VI introduces our newly proposed mitigation method that is based on reasoning. Section VII concludes the paper.
2551: 
2552: II Related Work
2553: 

full_text/2508.15370v1.txt:13::27 (0.3292)
  13: MultiTrust-X underscores the need for holistic evaluation and elaborate analysis and puts forward a mitigation strategy in the development of trustworthy multimodal AI systems.
  14: 
  15: Index Terms: 
  16: Multimodal Large Language Model, Trustworthiness, Benchmark, Safety Alignment
  17: 
  18: I Introduction
  19: 
  20: Figure 1: Framework of MultiTrust-X, including aspect division of trustworthiness, evaluation strategy of multimodal-related risks, and categorization of mitigation methods from a machine learning perspective. Specifically, we implement 32 tasks to comprehensively benchmark both modern MLLMs and existing approaches, which are exemplified in the grids between the axes of aspect and method, to provide practical insights for future improvements in trustworthy MLLMs.
  21: 
  22: Large Language Models (LLMs) [3][4][35][74] have demonstrated exceptional abilities in language comprehension and reasoning, representing a significant step towards Artificial General Intelligence (AGI) [25]. Leveraging their versatility, recent developments have extended LLMs beyond text to incorporate additional modalities such as vision, leading to Multimodal Large Language Models (MLLMs) [19][46][57][69][101], which excel in diverse multimodal tasks and are increasingly applied across various scenarios [24][31][50][88]. However, MLLMs also present serious concerns regarding trustworthiness, such as factual inaccuracies [6][90], harmful content generation [60][103], and privacy leakage [51][55], which pose critical challenges to the reliability and safety in applications and highlight the significance of further research to tackle them [1][23].
  23: 
  24: Recent studies have attempted to tackle relevant issues, beginning with evaluation efforts to better understand the trustworthiness of current MLLMs. Yet, existing benchmarks often focus narrowly on isolated aspects of trustworthiness (e.g., hallucination [6][40], adversarial robustness [22][97], content safety [10][80]), failing to provide a comprehensive view of this topic. Moreover, the evaluation scenarios and tasks are usually transformed from those for LLMs [42][103], overlooking the distinct risks introduced by multimodal inputs and cross-modal interactions that arise uniquely in MLLMs.
  25: 
  26: Such narrowness is also evident in existing mitigation approaches. While some methods have been proposed to enhance trustworthiness in dimensions such as truthfulness [37][87], safety [96][102], and robustness [64][98], they remain limited in this multifaceted topic. For instance, RLHF-V [86] and RLAIF-V [87] aim at reducing hallucination, while VLGuard [102] mainly reinforces the model’s refusal behavior in response to malicious queries. Nonetheless, these methods lack a holistic analysis of their different impacts on the overall trustworthiness of MLLMs, leaving a gap that can greatly affect their practical utility if not carefully examined.
  27: 

full_text/2508.15370v1.txt:2481::2495 (0.3292)
2481: Index Terms: 
2482: Multimodal Large Language Model, Trustworthiness, Benchmark, Safety Alignment
2483: 
2484: INDEX TERMS:
2485: 
2486: I Introduction
2487: 
2488: Figure 1: Framework of MultiTrust-X, including aspect division of trustworthiness, evaluation strategy of multimodal-related risks, and categorization of mitigation methods from a machine learning perspective. Specifically, we implement 32 tasks to comprehensively benchmark both modern MLLMs and existing approaches, which are exemplified in the grids between the axes of aspect and method, to provide practical insights for future improvements in trustworthy MLLMs.
2489: 
2490: Large Language Models (LLMs) [3][4][35][74] have demonstrated exceptional abilities in language comprehension and reasoning, representing a significant step towards Artificial General Intelligence (AGI) [25]. Leveraging their versatility, recent developments have extended LLMs beyond text to incorporate additional modalities such as vision, leading to Multimodal Large Language Models (MLLMs) [19][46][57][69][101], which excel in diverse multimodal tasks and are increasingly applied across various scenarios [24][31][50][88]. However, MLLMs also present serious concerns regarding trustworthiness, such as factual inaccuracies [6][90], harmful content generation [60][103], and privacy leakage [51][55], which pose critical challenges to the reliability and safety in applications and highlight the significance of further research to tackle them [1][23].
2491: 
2492: Recent studies have attempted to tackle relevant issues, beginning with evaluation efforts to better understand the trustworthiness of current MLLMs. Yet, existing benchmarks often focus narrowly on isolated aspects of trustworthiness (e.g., hallucination [6][40], adversarial robustness [22][97], content safety [10][80]), failing to provide a comprehensive view of this topic. Moreover, the evaluation scenarios and tasks are usually transformed from those for LLMs [42][103], overlooking the distinct risks introduced by multimodal inputs and cross-modal interactions that arise uniquely in MLLMs.
2493: 
2494: Such narrowness is also evident in existing mitigation approaches. While some methods have been proposed to enhance trustworthiness in dimensions such as truthfulness [37][87], safety [96][102], and robustness [64][98], they remain limited in this multifaceted topic. For instance, RLHF-V [86] and RLAIF-V [87] aim at reducing hallucination, while VLGuard [102] mainly reinforces the model’s refusal behavior in response to malicious queries. Nonetheless, these methods lack a holistic analysis of their different impacts on the overall trustworthiness of MLLMs, leaving a gap that can greatly affect their practical utility if not carefully examined.
2495: 

full_text/2508.12096v2.txt:166::180 (0.3334)
 166: 
 167: 2.1 LLM Evaluation Paradigms
 168: 
 169: Evaluating LLMs has become a central concern as their capabilities rapidly expand. Current evaluation methods generally fall into two mainstream categories: full-benchmark evaluation and random-sample evaluation. The former involves testing the LLM on entire standard benchmark such as MMLU (Hendrycks et al. 2021a), GPQA (Rein et al. 2023), GSM8K (Cobbe et al. 2021) and MATH (Hendrycks et al. 2021b). It provides stable and comprehensive results but incurs high computational costs, making it often impractical for routine assessments (Zhang, Cai, and Chen 2025; Biderman et al. 2024). Random-sample evaluation, on the other hand, offers a more resource-efficient alternative by selecting subsets of benchmark items for testing, typically in multiple sampling rounds. While this method reduces computational burden, it raises concerns about representativeness, reproducibility and sensitivity to model differences, especially when the benchmark contains a high proportion of trivial or low-difficulty items (Madaan et al. 2024). These shortcomings become particularly noticeable when distinguishing between models with similar performance levels.
 170: 
 171: 2.2 Benchmark Structural Bias
 172: 
 173: Recent studies have increasingly highlighted structural bias in public benchmarks for LLMs. Data contamination, a type of structural bias, has become a central concern in the evaluation of LLMs. Studies have demonstrated that LLMs often memorize benchmark samples during pretraining or alignment stages, resulting in artificially inflated performance that fails to reflect their true reasoning abilities (Zhou et al. 2023; López et al. 2025). To assess the extent of such leakage, several detection methods have been proposed, including n-gram-based method for GSM8K and MATH (Xu et al. 2024b), as well as permutation (Ni et al. 2025) and semi-half techniques for multiple-choice benchmarks (Hidayat et al. 2025). However, these methods are typically designed for specific types of benchmarks and may not generalize well across different evaluation settings. The STS defined in this paper provides a sample-level data contamination analysis tool and reveals a previously underexplored structural bias, that is the imbalance in sample difficulty distribution.
 174: 
 175: 2.3 Emergent Abilities of LLMs
 176: 
 177: Emergent abilities in large language models have been widely recognized, referring to the sudden appearance of complex capabilities as model scale increases (Wei et al. 2022). Most existing studies concentrate on task-level emergence, where improvements are observed across entire benchmarks (Schaeffer, Miranda, and Koyejo 2023; Lu et al. 2024). However, the hypothesis that certain individual samples may display sensitivity to model scale has not been thoroughly investigated. Our work extends this direction by introducing a structured evaluation perspective based on capability transition patterns observed across model scales.
 178: 
 179: 3 Methodology
 180: 

full_text/2508.12096v2.txt:1213::1227 (0.3334)
1213: 
1214: 2.1 LLM Evaluation Paradigms
1215: 
1216: Evaluating LLMs has become a central concern as their capabilities rapidly expand. Current evaluation methods generally fall into two mainstream categories: full-benchmark evaluation and random-sample evaluation. The former involves testing the LLM on entire standard benchmark such as MMLU (Hendrycks et al. 2021a), GPQA (Rein et al. 2023), GSM8K (Cobbe et al. 2021) and MATH (Hendrycks et al. 2021b). It provides stable and comprehensive results but incurs high computational costs, making it often impractical for routine assessments (Zhang, Cai, and Chen 2025; Biderman et al. 2024). Random-sample evaluation, on the other hand, offers a more resource-efficient alternative by selecting subsets of benchmark items for testing, typically in multiple sampling rounds. While this method reduces computational burden, it raises concerns about representativeness, reproducibility and sensitivity to model differences, especially when the benchmark contains a high proportion of trivial or low-difficulty items (Madaan et al. 2024). These shortcomings become particularly noticeable when distinguishing between models with similar performance levels.
1217: 
1218: 2.2 Benchmark Structural Bias
1219: 
1220: Recent studies have increasingly highlighted structural bias in public benchmarks for LLMs. Data contamination, a type of structural bias, has become a central concern in the evaluation of LLMs. Studies have demonstrated that LLMs often memorize benchmark samples during pretraining or alignment stages, resulting in artificially inflated performance that fails to reflect their true reasoning abilities (Zhou et al. 2023; López et al. 2025). To assess the extent of such leakage, several detection methods have been proposed, including n-gram-based method for GSM8K and MATH (Xu et al. 2024b), as well as permutation (Ni et al. 2025) and semi-half techniques for multiple-choice benchmarks (Hidayat et al. 2025). However, these methods are typically designed for specific types of benchmarks and may not generalize well across different evaluation settings. The STS defined in this paper provides a sample-level data contamination analysis tool and reveals a previously underexplored structural bias, that is the imbalance in sample difficulty distribution.
1221: 
1222: 2.3 Emergent Abilities of LLMs
1223: 
1224: Emergent abilities in large language models have been widely recognized, referring to the sudden appearance of complex capabilities as model scale increases (Wei et al. 2022). Most existing studies concentrate on task-level emergence, where improvements are observed across entire benchmarks (Schaeffer, Miranda, and Koyejo 2023; Lu et al. 2024). However, the hypothesis that certain individual samples may display sensitivity to model scale has not been thoroughly investigated. Our work extends this direction by introducing a structured evaluation perspective based on capability transition patterns observed across model scales.
1225: 
1226: 2 RELATED WORK
1227: 

full_text/2508.12096v2.txt:1233::1247 (0.3334)
1233: 
1234: Evaluating LLMs has become a central concern as their capabilities rapidly expand. Current evaluation methods generally fall into two mainstream categories: full-benchmark evaluation and random-sample evaluation. The former involves testing the LLM on entire standard benchmark such as MMLU (Hendrycks et al. 2021a), GPQA (Rein et al. 2023), GSM8K (Cobbe et al. 2021) and MATH (Hendrycks et al. 2021b). It provides stable and comprehensive results but incurs high computational costs, making it often impractical for routine assessments (Zhang, Cai, and Chen 2025; Biderman et al. 2024). Random-sample evaluation, on the other hand, offers a more resource-efficient alternative by selecting subsets of benchmark items for testing, typically in multiple sampling rounds. While this method reduces computational burden, it raises concerns about representativeness, reproducibility and sensitivity to model differences, especially when the benchmark contains a high proportion of trivial or low-difficulty items (Madaan et al. 2024). These shortcomings become particularly noticeable when distinguishing between models with similar performance levels.
1235: 
1236: Evaluating LLMs has become a central concern as their capabilities rapidly expand. Current evaluation methods generally fall into two mainstream categories: full-benchmark evaluation and random-sample evaluation. The former involves testing the LLM on entire standard benchmark such as MMLU (Hendrycks et al. 2021a), GPQA (Rein et al. 2023), GSM8K (Cobbe et al. 2021) and MATH (Hendrycks et al. 2021b). It provides stable and comprehensive results but incurs high computational costs, making it often impractical for routine assessments (Zhang, Cai, and Chen 2025; Biderman et al. 2024). Random-sample evaluation, on the other hand, offers a more resource-efficient alternative by selecting subsets of benchmark items for testing, typically in multiple sampling rounds. While this method reduces computational burden, it raises concerns about representativeness, reproducibility and sensitivity to model differences, especially when the benchmark contains a high proportion of trivial or low-difficulty items (Madaan et al. 2024). These shortcomings become particularly noticeable when distinguishing between models with similar performance levels.
1237: 
1238: 2.2 Benchmark Structural Bias
1239: 
1240: Recent studies have increasingly highlighted structural bias in public benchmarks for LLMs. Data contamination, a type of structural bias, has become a central concern in the evaluation of LLMs. Studies have demonstrated that LLMs often memorize benchmark samples during pretraining or alignment stages, resulting in artificially inflated performance that fails to reflect their true reasoning abilities (Zhou et al. 2023; López et al. 2025). To assess the extent of such leakage, several detection methods have been proposed, including n-gram-based method for GSM8K and MATH (Xu et al. 2024b), as well as permutation (Ni et al. 2025) and semi-half techniques for multiple-choice benchmarks (Hidayat et al. 2025). However, these methods are typically designed for specific types of benchmarks and may not generalize well across different evaluation settings. The STS defined in this paper provides a sample-level data contamination analysis tool and reveals a previously underexplored structural bias, that is the imbalance in sample difficulty distribution.
1241: 
1242: 2.2 BENCHMARK STRUCTURAL BIAS
1243: 
1244: Recent studies have increasingly highlighted structural bias in public benchmarks for LLMs. Data contamination, a type of structural bias, has become a central concern in the evaluation of LLMs. Studies have demonstrated that LLMs often memorize benchmark samples during pretraining or alignment stages, resulting in artificially inflated performance that fails to reflect their true reasoning abilities (Zhou et al. 2023; López et al. 2025). To assess the extent of such leakage, several detection methods have been proposed, including n-gram-based method for GSM8K and MATH (Xu et al. 2024b), as well as permutation (Ni et al. 2025) and semi-half techniques for multiple-choice benchmarks (Hidayat et al. 2025). However, these methods are typically designed for specific types of benchmarks and may not generalize well across different evaluation settings. The STS defined in this paper provides a sample-level data contamination analysis tool and reveals a previously underexplored structural bias, that is the imbalance in sample difficulty distribution.
1245: 
1246: Recent studies have increasingly highlighted structural bias in public benchmarks for LLMs. Data contamination, a type of structural bias, has become a central concern in the evaluation of LLMs. Studies have demonstrated that LLMs often memorize benchmark samples during pretraining or alignment stages, resulting in artificially inflated performance that fails to reflect their true reasoning abilities (Zhou et al. 2023; López et al. 2025). To assess the extent of such leakage, several detection methods have been proposed, including n-gram-based method for GSM8K and MATH (Xu et al. 2024b), as well as permutation (Ni et al. 2025) and semi-half techniques for multiple-choice benchmarks (Hidayat et al. 2025). However, these methods are typically designed for specific types of benchmarks and may not generalize well across different evaluation settings. The STS defined in this paper provides a sample-level data contamination analysis tool and reveals a previously underexplored structural bias, that is the imbalance in sample difficulty distribution.
1247: 

full_text/2508.12096v2.txt:1237::1251 (0.3334)
1237: 
1238: 2.2 Benchmark Structural Bias
1239: 
1240: Recent studies have increasingly highlighted structural bias in public benchmarks for LLMs. Data contamination, a type of structural bias, has become a central concern in the evaluation of LLMs. Studies have demonstrated that LLMs often memorize benchmark samples during pretraining or alignment stages, resulting in artificially inflated performance that fails to reflect their true reasoning abilities (Zhou et al. 2023; López et al. 2025). To assess the extent of such leakage, several detection methods have been proposed, including n-gram-based method for GSM8K and MATH (Xu et al. 2024b), as well as permutation (Ni et al. 2025) and semi-half techniques for multiple-choice benchmarks (Hidayat et al. 2025). However, these methods are typically designed for specific types of benchmarks and may not generalize well across different evaluation settings. The STS defined in this paper provides a sample-level data contamination analysis tool and reveals a previously underexplored structural bias, that is the imbalance in sample difficulty distribution.
1241: 
1242: 2.2 BENCHMARK STRUCTURAL BIAS
1243: 
1244: Recent studies have increasingly highlighted structural bias in public benchmarks for LLMs. Data contamination, a type of structural bias, has become a central concern in the evaluation of LLMs. Studies have demonstrated that LLMs often memorize benchmark samples during pretraining or alignment stages, resulting in artificially inflated performance that fails to reflect their true reasoning abilities (Zhou et al. 2023; López et al. 2025). To assess the extent of such leakage, several detection methods have been proposed, including n-gram-based method for GSM8K and MATH (Xu et al. 2024b), as well as permutation (Ni et al. 2025) and semi-half techniques for multiple-choice benchmarks (Hidayat et al. 2025). However, these methods are typically designed for specific types of benchmarks and may not generalize well across different evaluation settings. The STS defined in this paper provides a sample-level data contamination analysis tool and reveals a previously underexplored structural bias, that is the imbalance in sample difficulty distribution.
1245: 
1246: Recent studies have increasingly highlighted structural bias in public benchmarks for LLMs. Data contamination, a type of structural bias, has become a central concern in the evaluation of LLMs. Studies have demonstrated that LLMs often memorize benchmark samples during pretraining or alignment stages, resulting in artificially inflated performance that fails to reflect their true reasoning abilities (Zhou et al. 2023; López et al. 2025). To assess the extent of such leakage, several detection methods have been proposed, including n-gram-based method for GSM8K and MATH (Xu et al. 2024b), as well as permutation (Ni et al. 2025) and semi-half techniques for multiple-choice benchmarks (Hidayat et al. 2025). However, these methods are typically designed for specific types of benchmarks and may not generalize well across different evaluation settings. The STS defined in this paper provides a sample-level data contamination analysis tool and reveals a previously underexplored structural bias, that is the imbalance in sample difficulty distribution.
1247: 
1248: 2.3 Emergent Abilities of LLMs
1249: 
1250: Emergent abilities in large language models have been widely recognized, referring to the sudden appearance of complex capabilities as model scale increases (Wei et al. 2022). Most existing studies concentrate on task-level emergence, where improvements are observed across entire benchmarks (Schaeffer, Miranda, and Koyejo 2023; Lu et al. 2024). However, the hypothesis that certain individual samples may display sensitivity to model scale has not been thoroughly investigated. Our work extends this direction by introducing a structured evaluation perspective based on capability transition patterns observed across model scales.
1251: 


```

</details>

