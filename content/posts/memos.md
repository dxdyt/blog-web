---
title: memos
date: 2024-02-05T12:18:59+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1704642220407-392955316c7a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDcxMDY1ODB8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1704642220407-392955316c7a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDcxMDY1ODB8&ixlib=rb-4.0.3
---

# [usememos/memos](https://github.com/usememos/memos)

<img height="56px" src="https://www.usememos.com/full-logo-landscape.png" alt="Memos" />

A privacy-first, lightweight note-taking service. Easily capture and share your great thoughts.

<a href="https://www.usememos.com">Home Page</a> •
<a href="https://www.usememos.com/blog">Blogs</a> •
<a href="https://www.usememos.com/docs">Docs</a> •
<a href="https://demo.usememos.com/">Live Demo</a>

<p>
  <a href="https://hub.docker.com/r/neosmemo/memos"><img alt="Docker pull" src="https://img.shields.io/docker/pulls/neosmemo/memos.svg"/></a>
  <a href="https://hosted.weblate.org/engage/memos-i18n/"><img src="https://hosted.weblate.org/widget/memos-i18n/english/svg-badge.svg" alt="Translation status" /></a>
  <a href="https://discord.gg/tfPJa4UmAv"><img alt="Discord" src="https://img.shields.io/badge/discord-chat-5865f2?logo=discord&logoColor=f5f5f5" /></a>
</p>

![demo](https://www.usememos.com/demo.png)

## Key points

- **Open source and free forever**. Embrace a future where creativity knows no boundaries with our open-source solution – free today, tomorrow, and always.
- **Self-hosting with Docker in just seconds**. Enjoy the flexibility, scalability, and ease of setup that Docker provides, allowing you to have full control over your data and privacy.
- **Pure text with added Markdown support.** Say goodbye to the overwhelming mental burden of rich formatting and embrace a minimalist approach.
- **Customize and share your notes effortlessly**. With our intuitive sharing features, you can easily collaborate and distribute your notes with others.
- **RESTful API for third-party services.** Embrace the power of integration and unleash new possibilities with our RESTful API support.

## Deploy with Docker in seconds

```bash
docker run -d --name memos -p 5230:5230 -v ~/.memos/:/var/opt/memos neosmemo/memos:stable
```

> The `~/.memos/` directory will be used as the data directory on your local machine, while `/var/opt/memos` is the directory of the volume in Docker and should not be modified.

Learn more about [other installation methods](https://www.usememos.com/docs/install).

## Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. We greatly appreciate any contributions you make. Thank you for being a part of our community! 🥰

<a href="https://github.com/usememos/memos/graphs/contributors">
  <img src="https://contri-graphy.yourselfhosted.com/graph?repo=usememos/memos&format=svg" />
</a>

## Star history

[![Star History Chart](https://api.star-history.com/svg?repos=usememos/memos&type=Date)](https://star-history.com/#usememos/memos&Date)

## Other resources

- [**Gomark**](https://github.com/yourselfhosted/gomark): A markdown parser written in Go for Memos. And its [WebAssembly version](https://github.com/yourselfhosted/gomark-wasm) is also available.
- [**Bytebase**](https://www.bytebase.com): World's most advanced database DevOps and CI/CD for Developer, DBA and Platform Engineering teams. The GitLab/GitHub for database DevOps.
