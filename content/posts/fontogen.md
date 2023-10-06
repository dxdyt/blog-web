---
title: fontogen
date: 2023-10-06T12:17:12+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1694638278223-4c3907aa2354?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTY1NjU2OTF8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1694638278223-4c3907aa2354?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTY1NjU2OTF8&ixlib=rb-4.0.3
---

# [SerCeMan/fontogen](https://github.com/SerCeMan/fontogen)

# FontoGen

Generate your very own font with FontoGen. Read more about the project in
my [blog article](https://serce.me/posts/02-10-2023-hey-computer-make-me-a-font).

![screenshot](./img/fontogen.png)

## Installation

```bash
pipenv install
pipenv shell
# Nightly Triton is required
pip install -U --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/Triton-Nightly/pypi/simple/ triton-nightly==2.1.0.dev20230801015042 --no-deps
```

#### Inference

The model needs to be re-trained on a large dataset of OFL fonts. If anyone would like to contribute and re-train the model, please reach out and I'll be happy to help you set up the environment.
