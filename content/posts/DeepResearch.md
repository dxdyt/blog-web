---
title: DeepResearch
date: 2025-09-18T12:22:13+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1756786605218-28f7dd95a493?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTgxNjkyMzl8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1756786605218-28f7dd95a493?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTgxNjkyMzl8&ixlib=rb-4.1.0
---

# [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch)

<div align="center">
  <picture>
      <img src="./assets/logo.png" width="100%">
  </picture>
</div>

<hr>

<div align="center" style="line-height: 1;">

[![MODELS](https://img.shields.io/badge/Models-5EDDD2?style=for-the-badge&logo=huggingface&logoColor=ffffff&labelColor)](https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B)
[![GITHUB](https://img.shields.io/badge/Github-24292F?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Alibaba-NLP/DeepResearch)
[![Blog](https://img.shields.io/badge/Blog-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/)

</div>
<p align="center">
🤗 <a href="https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B" target="_blank">HuggingFace</a> ｜
<img src="./assets/tongyi.png" width="14px" style="display:inline;"> <a href="https://modelscope.cn/models/iic/Tongyi-DeepResearch-30B-A3B" target="_blank">ModelScope</a>
<p align="center">
<a href="https://trendshift.io/repositories/14217" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14217" 
alt="Alibaba-NLP%2FWebAgent | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

# Introduction

We present <img src="./assets/tongyi.png" width="14px" style="display:inline;"> **Tongyi DeepResearch**, an agentic large language model featuring 30.5 billion total parameters, with only 3.3 billion activated per token. Developed by Tongyi Lab, the model is specifically designed for **long-horizon, deep information-seeking** tasks. Tongyi DeepResearch demonstrates state-of-the-art performance across a range of agentic search benchmarks, including Humanity's Last Exam, BrowserComp, BrowserComp-ZH, WebWalkerQA,xbench-DeepSearch, FRAMES and SimpleQA.

> Tongyi DeepResearch builds upon our previous work on the <img src="./assets/tongyi.png" width="14px" style="display:inline;"> [WebAgent](./WebAgent/) project.

More details can be found in our 📰&nbsp;<a href="https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/">Tech Blog</a>.

<p align="center">
  <img width="100%" src="./assets/performance.png">
</p>

## Features

- ⚙️ **Fully automated synthetic data generation pipeline**: We design a highly scalable data synthesis pipeline, which is fully automatic and empowers agentic pre-training, supervised fine-tuning, and reinforcement learning.
- 🔄 **Large-scale continual pre-training on agentic data**: Leveraging diverse, high-quality agentic interaction data to extend model capabilities, maintain freshness, and strengthen reasoning performance.
- 🔁 **End-to-end reinforcement learning**: We employ a strictly on-policy RL approach based on a customized Group Relative Policy Optimization framework, with token-level policy gradients, leave-one-out advantage estimation, and selective filtering of negative samples to stabilize training in a non‑stationary environment.
- 🤖 **Agent Inference Paradigm Compatibility**: At inference, Tongyi DeepResearch is compatible with two inference paradigms: ReAct, for rigorously evaluating the model's core intrinsic abilities, and an IterResearch-based 'Heavy' mode, which uses a test-time scaling strategy to unlock the model's maximum performance ceiling.

# Model Download

You can directly download the model by following the links below.

| Model             | Download Links                            | Model Size | Context Length |
| :-----------------: | :-----------------------------------------: | :----------: | :--------------: |
| Tongyi-DeepResearch-30B-A3B | [🤗 HuggingFace](https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B)<br> [🤖 ModelScope](https://modelscope.cn/models/iic/Tongyi-DeepResearch-30B-A3B) | 30B-A3B | 128K |

# News

[2025/09/17]🔥 We have released **Tongyi-DeepResearch-30B-A3B**.

# Deep Research Benchmark Results
<p align="center">
  <img width="100%" src="./assets/benchmark.png">
</p>

## Quick Start

This guide provides instructions for setting up the environment and running inference scripts located in the [inference](./inference/) folder.

### 1. Environment Setup
- Recommended Python version: **3.10.0** (using other versions may cause dependency issues).
- It is strongly advised to create an isolated environment using `conda` or `virtualenv`.

```bash
# Example with Conda
conda create -n react_infer_env python=3.10.0 
conda activate react_infer_env
```

### 2. Installation

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Prepare Evaluation Data
- Create a folder named `eval_data/` in the project root.
- Place your QA file in **JSONL** format inside this directory, e.g. `eval_data/example.jsonl`.
- Each line must be a JSON object that includes **both** of the following keys:
  ```json
  {"question": "...","answer": "..."}
  ```
- A sample file is provided in the `eval_data` folder for reference.
- If you plan to use the *file parser* tool, **prepend the file name to the `question` field** and place the referenced file inside the `eval_data/file_corpus/` directory.

### 4. Configure the Inference Script
- Open `run_react_infer.sh` and modify the following variables as instructed in the comments:
  * `MODEL_PATH`  - path to the local or remote model weights.
  * `DATASET`     - path to the evaluation set, e.g. `example`.
  * `OUTPUT_PATH` - path for saving the prediction results, e.g. `./outputs`.
- Depending on the tools you enable (retrieval, calculator, web search, etc.), provide the required `API_KEY`, `BASE_URL`, or other credentials. Each key is explained inline in the bash script.


### 5. Run the Inference Script

```bash
bash run_react_infer.sh
```
---

With these steps, you can fully prepare the environment, configure the dataset, and run the model. For more details, consult the inline comments in each script or open an issue.

## Benchmark Evaluation

We provide benchmark evaluation scripts for various datasets. Please refer to the [evaluation scripts](./evaluation/) directory for more details.

## Deep Research Agent Family

<p align="center">
  <img width="100%" src="./assets/family.png">
</p>

Tongyi DeepResearch also has an extensive deep research agent family. You can find more information in the following paper:

[1] [WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/pdf/2501.07572)<br>
[2] [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/pdf/2505.22648)<br>
[3] [WebSailor: Navigating Super-human Reasoning for Web Agent](https://arxiv.org/pdf/2507.02592)<br>
[4] [WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization](https://arxiv.org/pdf/2507.15061)<br>
[5] [WebWatcher: Breaking New Frontier of Vision-Language Deep Research Agent](https://arxiv.org/pdf/2508.05748)<br>
[6] [WebResearcher: Unleashing unbounded reasoning capability in Long-Horizon Agents](https://arxiv.org/pdf/2509.13309)<br>
[7] [ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization](https://arxiv.org/pdf/2509.13313)<br>
[8] [WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research](https://arxiv.org/pdf/2509.13312)<br>
[9] [WebSailor-V2: Bridging the Chasm to Proprietary Agents via Synthetic Data and Scalable Reinforcement Learning](https://arxiv.org/pdf/2509.13305)<br>
[10] [Scaling Agents via Continual Pre-training](https://arxiv.org/pdf/2509.13310)<br>
[11] [Towards General Agentic Intelligence via Environment Scaling](https://arxiv.org/pdf/2509.13311)


## 🌟 Misc

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=Alibaba-NLP/DeepResearch&type=Date)](https://www.star-history.com/#Alibaba-NLP/DeepResearch&Date)

</div>

## 🚩 Talent Recruitment

🔥🔥🔥 We are hiring! Research intern positions are open (based in Hangzhou、Beijing、Shanghai)

📚 **Research Area**：Web Agent, Search Agent, Agent RL, MultiAgent RL, Agentic RAG

☎️ **Contact**：[yongjiang.jy@alibaba-inc.com]()

## Contact Information

For communications, please contact Yong Jiang (yongjiang.jy@alibaba-inc.com).

## Citation
```bibtex
@misc{tongyidr,
  author={Tongyi DeepResearch Team},
  title={Tongyi-DeepResearch},
  year={2025},
  howpublished={\url{https://github.com/Alibaba-NLP/DeepResearch}}
}
```