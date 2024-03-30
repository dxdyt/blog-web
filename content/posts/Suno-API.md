---
title: Suno-API
date: 2024-03-30T12:16:07+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1709625862206-84f82e0754a8?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTE3NzIwNTd8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1709625862206-84f82e0754a8?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTE3NzIwNTd8&ixlib=rb-4.0.3
---

# [SunoAI-API/Suno-API](https://github.com/SunoAI-API/Suno-API)

[简体中文](README_ZH.md)


# Unofficial Suno API

This is an unofficial Suno API based on Python and FastAPI. It currently supports generating songs, lyrics, etc.  
It comes with a built-in token maintenance and keep-alive feature, so you don't have to worry about the token expiring.

### Features

- Automatic token maintenance and keep-alive
- Fully asynchronous, fast, suitable for later expansion
- Simple code, easy to maintain, convenient for secondary development


### Usage

#### Configuration

Edit the `.env.example` file, rename to `.env` and fill in the session_id and cookie.

These are initially obtained from the browser, and will be automatically kept alive later.

![cookie](./images/cover.png)


#### Run

Install dependencies 

```bash
pip3 install -r requirements.txt
```

For this part, refer to the FastAPI documentation on your own.
```bash
uvicorn main:app 
```

#### Docker

```bash
docker compose build && docker compose up
```

#### Documentation

After setting up the service, visit /docs

![docs](./images/docs.png)


#### Contanct me


<img src="./images/wechat.jpg" width="382px" height="511px" />