---
title: documentation
date: 2023-06-12T12:17:46+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1659259540528-0240ad70e92a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODY1NDMzMDR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1659259540528-0240ad70e92a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODY1NDMzMDR8&ixlib=rb-4.0.3
---

# [iv-org/documentation](https://github.com/iv-org/documentation)

# The Invidious documentation

## Running the documentation locally for development purposes

Run those commands in the repository's folder.

### Local `mkdocs-material` installation

```bash
# You might want to create a virtualenv first
pip install mkdocs-material
mkdocs-material serve
```

### With docker

```bash
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material:latest
```
