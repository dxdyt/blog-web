---
title: chatgpt-retrieval
date: 2023-06-22T12:15:33+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1684419081530-d0dd7ed6921a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODc0MDcyOTR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1684419081530-d0dd7ed6921a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODc0MDcyOTR8&ixlib=rb-4.0.3
---

# [techleadhd/chatgpt-retrieval](https://github.com/techleadhd/chatgpt-retrieval)

# chatgpt-retrieval

Simple script to use ChatGPT on your own files.

Here's the [YouTube Video](https://youtu.be/9AXP7tCI9PI).

## Installation

Install [Langchain](https://github.com/hwchase17/langchain).
```
pip install langchain
pip install openai
pip install chromadb
pip install tiktoken
```
Modify `constants.py` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys).

Place your own data into `data.txt`.

## Example usage
```
> python chatgpt.py "what is my dog's name"
Your dog's name is Sunny.
```
