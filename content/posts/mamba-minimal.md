---
title: mamba-minimal
date: 2023-12-23T12:15:04+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1702651364906-f4312ed8f4a6?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDMzMDQ4OTF8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1702651364906-f4312ed8f4a6?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDMzMDQ4OTF8&ixlib=rb-4.0.3
---

# [johnma2006/mamba-minimal](https://github.com/johnma2006/mamba-minimal)

## mamba-minimal

Simple, minimal implementation of Mamba in one file of PyTorch.

Featuring:
* Equivalent numerical output as official implementation for both forward and backward pass
* Simplified, readable, annotated code

Does NOT include:
* Speed. The official implementation is heavily optimized, and these optimizations are core contributions of the Mamba paper. I kept most implementations simple for readability.
* Proper parameter initialization (though this could be added without sacrificing readability)

## Demo

See [demo.ipynb](demo.ipynb) for examples of prompt completions.

```python
from model import Mamba
from transformers import AutoTokenizer

model = Mamba.from_pretrained('state-spaces/mamba-370m')
tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neox-20b')

generate(model, tokenizer, 'Mamba is the')
```
> Mamba is the world's longest venomous snake with an estimated length of over 150 m. With such a large size and a venomous bite, Mamba kills by stabbing the victim (which is more painful and less effective than a single stab of the bite)

150 meters... 🫢 scary!

## References

The Mamba architecture was introduced in [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) by [Albert Gu](https://twitter.com/_albertgu?lang=en) and [Tri Dao](https://twitter.com/tri_dao?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor).

The official implementation is here: https://github.com/state-spaces/mamba/tree/main
