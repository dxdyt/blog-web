---
title: llama3v
date: 2024-06-01T12:19:04+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1713560625744-46175f1b4a37?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTcyMTUzOTF8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1713560625744-46175f1b4a37?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTcyMTUzOTF8&ixlib=rb-4.0.3
---

# [mustafaaljadery/llama3v](https://github.com/mustafaaljadery/llama3v)

# llama3v

llama3v is a SOTA vision model that is powered by [Llama3 8B](https://llama.meta.com/llama3/) and [siglip-so400m](https://huggingface.co/google/siglip-so400m-patch14-384).

[ [GitHub](https://github.com/mustafaaljadery/llama3v) ] [ [Model Weights](https://huggingface.co/mustafaaljadery/llama3v) ] [ [Blog Post](https://aksh-garg.medium.com/llama-3v-building-an-open-source-gpt-4v-competitor-in-under-500-7dd8f1f6c9ee) ]

## Features

- SOTA open-source VLLM
- Model is available on Huggingface
- Fast local inference
- Release inference code (training code is coming soon, just cleaning up)

Checkout [huggingface](https://huggingface.co/mustafaaljadery/llama3v) for the model weights.

![Metrics](./images/metrics.png)

## Usage

You can use **llama3v** with the Transformers library.

```python
from transformers import AutoTokenizer, AutoModel
from PIL import Image

model = AutoModel.from_pretrained("mustafaaljadery/llama3v").cuda()
tokenizer = AutoTokenizer.from_pretrained("mustafaaljadery/llama3v")

image = Image.open("test_image.png")

answer = model.generate(image=image, message="What is this image?", temperature=0.1, tokenizer=tokenizer)

print(answer)
```

The model first passes through the image through the vision model to extract the features, then pass through the language model to generate the answer. Here is a sample inference pipeline:

![Architecture](./images/architecture.png)

## Training Process

In our training process, we combine the siglip-so400m model for vision with the Llama3 8B model for multi-modal image-text input with text generation.

We add a projection layer to the siglip-so400m model to project the image features to the LLaMA embedding space for the model to better understand the image.

In the pretraining process, we use freeze all the weights other than the projection layer. We train on about 600K images.

In the fine-tuning process, we update the weights of the Llama3 8B model while freezing the weights of the siglip-so400m model and the projection layer. We train for approximately 1M images. Moreover, we generate synthetic multimodal data from YI's model family for multimodal text generation as well. We finetune our model on this synsthetic data.

Read more about our training process [here](https://aksh-garg.medium.com/llama-3v-building-an-open-source-gpt-4v-competitor-in-under-500-7dd8f1f6c9ee).

## Acknowledgements

- [Mustafa Aljadery](https://www.linkedin.com/in/mustafaaljadery/)
- [Aksh Garg](https://www.linkedin.com/in/aksh-garg)
- [Siddharth Sharma](https://www.linkedin.com/in/siddharth-sharma-9942b2104/)

## Citations

This was built with the help of the following resources:

- [llama 3 8B](https://llama.meta.com/llama3/)
- [siglip-so400m](https://huggingface.co/google/siglip-so400m-patch14-384)
- [idefics2](https://huggingface.co/blog/idefics2)
- [Llava](https://llava-vl.github.io/)
- [LLava-UHD + OpenBMB](https://github.com/thunlp/LLaVA-UHD)
- [YI Model Family](https://arxiv.org/abs/2403.04652)
