---
title: starcoder2
date: 2024-03-04T12:43:54+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1709028942660-f8525396a90d?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDk1MjczNTR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1709028942660-f8525396a90d?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDk1MjczNTR8&ixlib=rb-4.0.3
---

# [bigcode-project/starcoder2](https://github.com/bigcode-project/starcoder2)

# StarCoder 2

<p align="center"><a href="https://huggingface.co/bigcode">[🤗 Models & Datasets]</a> | <a href="https://drive.google.com/file/d/17iGn3c-sYNiLyRSY-A85QOzgzGnGiVI3/view">[Paper]</a></a> 
</p>

StarCoder2 is a family of code generation models (3B, 7B, and 15B), trained on 600+ programming languages from [The Stack v2](https://huggingface.co/datasets/bigcode/the-stack-v2) and some natural language text such as Wikipedia, Arxiv, and GitHub issues. The models use Grouped Query Attention, a context window of 16,384 tokens, with sliding window attention of 4,096 tokens. The 3B & 7B models were trained on 3+ trillion tokens, while the 15B was trained on 4+ trillion tokens. For more details check out the [paper](https://drive.google.com/file/d/17iGn3c-sYNiLyRSY-A85QOzgzGnGiVI3/view).

# Table of Contents
1. [Quickstart](#quickstart)
    - [Installation](#installation)
    - [Model usage and memory footprint](#model-usage-and-memory-footprint)
    - [Text-generation-inference code](#text-generation-inference)
2. [Fine-tuning](#fine-tuning)
    - [Setup](#setup)
    - [Training](#training)
3. [Evaluation](#evaluation)

# Quickstart
StarCoder2 models are intended for code completion, they are not instruction models and commands like "Write a function that computes the square root." do not work well. 

## Installation
First, we have to install all the libraries listed in `requirements.txt`
```bash
pip install -r requirements.txt
# export your HF token, found here: https://huggingface.co/settings/account
export HF_TOKEN=xxx
```

## Model usage and memory footprint
Here are some examples to load the model and generate code, with the memory footprint of the largest model, `StarCoder2-15B`. Ensure you've installed `transformers` from source (it should be the case if you used `requirements.txt`)
```bash
pip install git+https://github.com/huggingface/transformers.git
```

### Running the model on CPU/GPU/multi GPU
* _Using full precision_
```python
# pip install git+https://github.com/huggingface/transformers.git # TODO: merge PR to main
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigcode/starcoder2-15b"
device = "cuda" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# to use Multiple GPUs do `model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto")`
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```

* _Using `torch.bfloat16`_
```python
# pip install accelerate
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

checkpoint = "bigcode/starcoder2-15b"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# for fp16 use `torch_dtype=torch.float16` instead
model = AutoModelForCausalLM.from_pretrained(checkpoint, device_map="auto", torch_dtype=torch.bfloat16)

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to("cuda")
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```
```bash
>>> print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")
Memory footprint: 32251.33 MB
```

### Quantized Versions through `bitsandbytes`
* _Using 8-bit precision (int8)_

```python
# pip install bitsandbytes accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# to use 4bit use `load_in_4bit=True` instead
quantization_config = BitsAndBytesConfig(load_in_8bit=True)

checkpoint = "bigcode/starcoder2-15b_16k"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained("bigcode/starcoder2-15b_16k", quantization_config=quantization_config)

inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to("cuda")
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```
```bash
>>> print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")
# load_in_8bit
Memory footprint: 16900.18 MB
# load_in_4bit
>>> print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")
Memory footprint: 9224.60 MB
```
You can also use `pipeline` for the generation:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
checkpoint = "bigcode/starcoder2-15b"

model = AutoModelForCausalLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)
print( pipe("def hello():") )
```

## Text-generation-inference: 

```bash
docker run -p 8080:80 -v $PWD/data:/data -e HUGGING_FACE_HUB_TOKEN=<YOUR BIGCODE ENABLED TOKEN> -d  ghcr.io/huggingface/text-generation-inference:latest --model-id bigcode/starcoder2-15b --max-total-tokens 8192
```
For more details, see [here](https://github.com/huggingface/text-generation-inference).

# Fine-tuning

Here, we showcase how you can fine-tune StarCoder2 models. For more fine-tuning resources you can check [StarCoder's GitHub repository](https://github.com/bigcode-project/starcoder) and [SantaCoder-Finetuning](https://github.com/loubnabnl/santacoder-finetuning).

## Setup

Install `pytorch` [see documentation](https://pytorch.org/), for example the following command works with cuda 12.1:
```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

Install the requirements (this installs `transformers` from source to support the StarCoder2 architecture):
```bash
pip install -r requirements.txt
```

Before you run any of the scripts make sure you are logged in `wandb` and HuggingFace Hub to push the checkpoints:
```bash
wandb login
huggingface-cli login
``` 
Now that everything is done, you can clone the repository and get into the corresponding directory.

## Training
To fine-tune efficiently with a low cost, we use [PEFT](https://github.com/huggingface/peft) library for Low-Rank Adaptation (LoRA) training and [bitsandbytes](https://github.com/TimDettmers/bitsandbytes) for 4bit quantization. We also use the `SFTTrainer` from [TRL](https://github.com/huggingface/trl).


For this example, we will fine-tune StarCoder2-3b on the `Rust` subset of [the-stack-smol](https://huggingface.co/datasets/bigcode/the-stack-smol). This is just for illustration purposes; for a larger and cleaner dataset of Rust code, you can use [The Stack dedup](https://huggingface.co/datasets/bigcode/the-stack-dedup). 

To launch the training:
```bash
accelerate launch finetune.py \
        --model_id "bigcode/starcoder2-3b" \
        --dataset_name "bigcode/the-stack-smol" \
        --subset "data/rust" \
        --dataset_text_field "content" \
        --split "train" \
        --max_seq_length 1024 \
        --max_steps 10000 \
        --micro_batch_size 1 \
        --gradient_accumulation_steps 8 \
        --learning_rate 2e-5 \
        --warmup_steps 20 \
        --num_proc "$(nproc)"
```

If you want to fine-tune on other text datasets, you need to change `dataset_text_field` argument to the name of the column containing the code/text you want to train on.
 
# Evaluation
To evaluate StarCoder2 and its derivatives, you can use the [BigCode-Evaluation-Harness](https://github.com/bigcode-project/bigcode-evaluation-harness) for evaluating Code LLMs. You can also check the [BigCode Leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard).
