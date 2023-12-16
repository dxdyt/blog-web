---
title: AnimateAnyone-unofficial
date: 2023-12-16T12:17:05+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1701979396507-4f4f8db40269?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDI3MDAxMjR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1701979396507-4f4f8db40269?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDI3MDAxMjR8&ixlib=rb-4.0.3
---

# [guoqincode/AnimateAnyone-unofficial](https://github.com/guoqincode/AnimateAnyone-unofficial)

# Unofficial Implementation of Animate Anyone

## Overview
This repository contains an simple and unofficial implementation of [Animate Anyone](https://humanaigc.github.io/animate-anyone/). This project is built upon [magic-animate](https://github.com/magic-research/magic-animate/tree/main) and [AnimateDiff](https://github.com/guoyww/AnimateDiff).

## News 🤗🤗🤗
The first training phase basic test passed, currently in training and testing the second phase.

Training may be slow due to GPU shortage.😢

## Note !!!
This project is under continuous development in part-time, there may be bugs in the code, welcome to correct them, I will optimize the code after the pre-trained model is released!

## Requirements
Same as [magic-animate](https://github.com/magic-research/magic-animate/tree/main).

## ToDo
- [x] **Release Training Code.**
- [ ] DeepSpeed + Accelerator Training
- [ ] **Release Inference Code and unofficial pre-trained weights.**

## Training

#### First Stage

```python
torchrun --nnodes=1 --nproc_per_node=1 train.py --config configs/training/train_stage_1.yaml
```

#### Second Stage

```python
torchrun --nnodes=1 --nproc_per_node=1 train.py --config configs/training/train_stage_2.yaml
```

## Inference

#### First Stage

```python
python3 -m pipelines.animation_stage_1 --config configs/prompts/animation_stage_1.yaml
```

#### Second Stage

## Acknowledgements
Special thanks to the original authors of the [Animate Anyone](https://humanaigc.github.io/animate-anyone/) project and the contributors to the [magic-animate](https://github.com/magic-research/magic-animate/tree/main) and [AnimateDiff](https://github.com/guoyww/AnimateDiff) repository for their open research and foundational work that inspired this unofficial implementation.

## Email
guoqin@stu.pku.edu.cn
