---
title: epeius
date: 2024-05-08T12:16:16+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1711000328044-d90e2b181b95?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTUxNDE2NDd8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1711000328044-d90e2b181b95?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTUxNDE2NDd8&ixlib=rb-4.0.3
---

# [ca110us/epeius](https://github.com/ca110us/epeius)

# Epeius
English | [简体中文](./README-zh_CN.md)

Deploy Trojan using a Serverless approach

## Quick start
- Create a new Worker in Cloudflare Workers dashboard. 
- Paste code from [worker.js](./src/worker.js) into the worker code editor. 
- Replace `sha224Password` with your own password. You can generate [here](https://www.atatus.com/tools/sha224-to-hash). Alternatively, you can add the `SHA224PASS` environment variable in Cloudflare Workers settings later.
- Binding a custom domain to the worker.
- Visit `https://[YOUR_DOMAIN]/link` and replace `ca110us` with your plain password.

## Not supported
- UDP 🙅 (Cloudflare workers runtime does not support UDP yet)

## Disclaimer
This project is for study/research purposes only. Users are responsible for legal compliance and ethical conduct. The author disclaims all liability for misuse.

## Reference
[zizifn/edgetunnel](https://github.com/zizifn/edgetunnel)