---
title: telegram-search
date: 2025-05-26T12:25:06+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1746263658731-469853340643?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDgyMzM0NzN8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1746263658731-469853340643?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDgyMzM0NzN8&ixlib=rb-4.1.0
---

# [groupultra/telegram-search](https://github.com/groupultra/telegram-search)

# Telegram Search

[English](./README_EN.md)

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/+Gs3SH2qAPeFhYmU9)
[![Discord](https://dcbadge.limes.pink/api/server/NzYsmJSgCT)](https://discord.gg/NzYsmJSgCT)

<a href="https://trendshift.io/repositories/13868" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13868" alt="groupultra%2Ftelegram-search | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

一个功能强大的 Telegram 聊天记录搜索工具，支持向量搜索和语义匹配。基于 OpenAI 的语义向量技术，让你的 Telegram 消息检索更智能、更精准。

- 欢迎 PR 贡献！
- 由于项目处于快速迭代阶段，可能会出现数据库不兼容的情况，建议定期备份数据。
- 获取 API key: [#111](https://github.com/GramSearch/telegram-search/issues/111)

![image](https://github.com/user-attachments/assets/0fa3ba2f-9a3d-4530-9ecd-3336a0f952ad)

## 💖 赞助者

![Sponsors](https://github.com/luoling8192/luoling8192/raw/master/sponsorkit/sponsors.svg)

## 🚀 快速开始

### 安装步骤

1. 克隆仓库：

```bash
git clone https://github.com/GramSearch/telegram-search.git
cd telegram-search
```

2. 安装依赖：

```bash
pnpm install
```

3. 配置环境：

```bash
cp config/config.example.yaml config/config.yaml
```

4. 启动数据库容器:

```bash
docker compose up -d
```

5. 同步数据库表结构：

```bash
pnpm run db:migrate
```

6. 启动服务：

```bash
# 启动后端服务
pnpm run dev:server

# 启动前端界面
pnpm run dev:frontend
```

访问 `http://localhost:3333` 即可打开搜索界面。

## 🚀 Activity

[![Star History Chart](https://api.star-history.com/svg?repos=luoling8192/telegram-search&type=Date)](https://star-history.com/#luoling8192/telegram-search&Date)

![Alt](https://repobeats.axiom.co/api/embed/c0fe5f057a33ce830a632c6ae421433f50e9083f.svg "Repobeats analytics image")

## 📝 License

MIT License © 2025
