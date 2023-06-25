---
title: chatgpt-retrieval
date: 2023-06-25T12:17:56+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1684019329793-f86cf9cf38af?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODc2NjY2Mjh8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1684019329793-f86cf9cf38af?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODc2NjY2Mjh8&ixlib=rb-4.0.3
---

# [techleadhd/chatgpt-retrieval](https://github.com/techleadhd/chatgpt-retrieval)

# chatgpt-retrieval

Simple script to use ChatGPT on your own files.

Here's the [YouTube Video](https://youtu.be/9AXP7tCI9PI).

## Installation

Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```
Modify `constants.py` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys).

Place your own data into `data/data.txt`.

## Example usage
Test reading `data/data.txt` file.
```
> python chatgpt.py "what is my dog's name"
Your dog's name is Sunny.
```

Test reading `data/cat.pdf` file.
```
> python chatgpt.py "what is my cat's name"
Your cat's name is Muffy.
```
