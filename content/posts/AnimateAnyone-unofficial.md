---
title: AnimateAnyone-unofficial
date: 2023-12-14T12:17:27+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1699882236909-b66077950046?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDI1MjczNTZ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1699882236909-b66077950046?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDI1MjczNTZ8&ixlib=rb-4.0.3
---

# [guoqincode/AnimateAnyone-unofficial](https://github.com/guoqincode/AnimateAnyone-unofficial)

# Unofficial Implementation of Animate Anyone

## Overview
This repository contains an simple and unofficial implementation of [Animate Anyone](https://humanaigc.github.io/animate-anyone/). This project is built upon [magic-animate](https://github.com/magic-research/magic-animate/tree/main) and [AnimateDiff](https://github.com/guoyww/AnimateDiff).

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

#### Second Stage

## Acknowledgements
Special thanks to the original authors of the [Animate Anyone](https://humanaigc.github.io/animate-anyone/) project and the contributors to the [magic-animate](https://github.com/magic-research/magic-animate/tree/main) and [AnimateDiff](https://github.com/guoyww/AnimateDiff) repository for their open research and foundational work that inspired this unofficial implementation.
