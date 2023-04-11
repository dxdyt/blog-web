---
title: ChatFiles
date: 2023-04-11T12:17:47+08:00
draft: False
featuredImage: https://wallpaperhub.app/api/v1/get/12006/0/1080p
featuredImagePreview: https://wallpaperhub.app/api/v1/get/12006/0/1080p
---

# [guangzhengli/ChatFiles](https://github.com/guangzhengli/ChatFiles)

[![My Skills](https://skillicons.dev/icons?i=nextjs,tailwind,react,python,flask)](https://skillicons.dev)

# ChatFiles

EN | [中文文档](README.zh.md)

> this repository use [jerryjliu/llama_index](https://github.com/jerryjliu/llama_index), based on [mckaywrigley/chatbot-ui](https://github.com/mckaywrigley/chatbot-ui), inspired by [madawei2699/myGPTReader](https://github.com/madawei2699/myGPTReader)

![Chatfiles](./doc/chatfiles.png)

**Upload your file and have a conversation with it.**

## How to use it
1. clone this repository.
2. create a .env file on root path.
3. put your OpenAI Key to .env file with OPENAI_API_KEY='your token'

run this project with docker compose.
```shell
docker compose up
```

open browser with http://localhost:3000

### chat with file
1. upload a file.
2. have a conversation with it.

### chat with GPT
1. send message without upload file.

## How to run locally
### chatfiles-ui

```shell
cd chatfiles-ui
npm install
npm run dev
```

### chatfiles
```shell
cd chatfiles
```

create a file named .env with value(OPENAI_API_KEY=your token)

```shell
python3 server.py
```


## Feature

- [x] Chat with GPT-3.5
- [x] Chat with file by llama_index
- [ ] Upload multiple files to one index, chat with multiple files.