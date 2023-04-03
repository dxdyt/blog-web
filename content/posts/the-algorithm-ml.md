---
title: the-algorithm-ml
date: 2023-04-03T12:15:45+08:00
draft: False
featuredImage: https://wallpaperhub.app/api/v1/get/11959/0/1080p
featuredImagePreview: https://wallpaperhub.app/api/v1/get/11959/0/1080p
---

# [twitter/the-algorithm-ml](https://github.com/twitter/the-algorithm-ml)

This project open sources some of the ML models used at Twitter.

Currently these are:

1. The "For You" Heavy Ranker (projects/home/recap).

2. TwHIN embeddings (projects/twhin) https://arxiv.org/abs/2202.05387


This project can be run inside a python virtualenv. We have only tried this on Linux machines and because we use torchrec it works best with an Nvidia GPU. To setup run

`./images/init_venv.sh` (Linux only).

The READMEs of each project contain instructions about how to run each project.
