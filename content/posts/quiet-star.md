---
title: quiet-star
date: 2024-03-25T12:18:44+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1710537432988-516a114f5955?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTEzNDAxNzB8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1710537432988-516a114f5955?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTEzNDAxNzB8&ixlib=rb-4.0.3
---

# [ezelikman/quiet-star](https://github.com/ezelikman/quiet-star)

# Quiet-STaR

Code for [Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking](https://arxiv.org/abs/2403.09629).

This project is implemented by simply patching the base Mistral implementation in Huggingface `transformers` using a new `modeling_mistral.py` and a new `configuration_mistral.py` and otherwise applying standard `transformers` features (e.g. the default Trainer). Our patches were applied to Huggingface's `transformers` version `4.37.0.dev0` under `src/transformers/models/mistral/` -- we cannot guarantee that other changes to their implementation will not affect our implementation, so for reproducibility, we encourage using the same version.

One pitfall to be wary of: the model is not taught not to generate start and end thought tokens. Thus, when performing actual inference, it is necessary to mask these out.

We make an 8-thought-token ahead (including start and end tokens) model [available via Huggingface](https://huggingface.co/ezelikman/quietstar-8-ahead).
