---
title: chatnio
date: 2024-11-09T12:18:23+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1730401723426-5ef4de56df92?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzExMjU4OTd8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1730401723426-5ef4de56df92?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzExMjU4OTd8&ixlib=rb-4.0.3
---

# [zmh-program/chatnio](https://github.com/zmh-program/chatnio)

<div align="center">

![chatnio](/app/public/logo.png)

# [🥳 Chat Nio](https://chatnio.com)

#### 🚀 Next Generation AIGC One-Stop Business Solution

#### *"Chat Nio > [Next Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) + [One API](https://github.com/songquanpeng/one-api)"*


English · [简体中文](./README_zh-CN.md) · [Docs](https://chatnio.com) · [Discord](https://discord.gg/rpzNSmqaF2) · [Deployment Guide](https://chatnio.com/docs/deploy)

[![Deploy on Zeabur](https://zeabur.com/button.svg)](https://zeabur.com/templates/M86XJI)

[![Chat Nio: #1 Repo Of The Day](https://trendshift.io/api/badge/repositories/6369)](https://trendshift.io/repositories/6369)

<img alt="Chat Nio Preview" src="./screenshot/chatnio.png" width="100%" style="border-radius: 8px">

</div>

## 📝 Features
1. 🤖️ **Rich Model Support**: Multi-model service provider support (OpenAI / Anthropic / Gemini / Midjourney and more than ten compatible formats & private LLM support)
2. 🤯 **Beautiful UI Design**: UI compatible with PC / Pad / Mobile, following [Shadcn UI](https://ui.shadcn.com) & [Tremor Charts](https://blocks.tremor.so) design standards, rich and beautiful interface design and backend dashboard
3. 🎃 **Complete Markdown Support**: Support for **LaTeX formulas** / **Mermaid mind maps** / table rendering / code highlighting / chart drawing / progress bars and other advanced Markdown syntax support
4. 👀 **Multi-theme Support**: Support for multiple theme switching, including **Light Mode** for light themes and **Dark Mode** for dark themes. 👉 [Custom Color Scheme](https://github.com/Deeptrain-Community/chatnio/blob/main/app/src/assets/globals.less)
5. 📚 **Internationalization Support**: Support for internationalization, multi-language switching 🇨🇳 🇺🇸 🇯🇵 🇷🇺 👉 Welcome to contribute translations [Pull Request](https://github.com/Deeptrain-Community/chatnio/pulls)
6. 🎨 **Text-to-Image Support**: Support for multiple text-to-image models: **OpenAI DALL-E**✅ & **Midjourney** (support for **U/V/R** operations)✅ & Stable Diffusion✅ etc.
7. 📡 **Powerful Conversation Sync**: **Zero-cost cross-device conversation sync support for users**, support for **conversation sharing** (link sharing & save as image & share management), **no need for WebDav / WebRTC and other dependencies and complex learning costs**
8. 🎈 **Model Market & Preset System**: Support for customizable model market in the backend, providing model introductions, tags, and other parameters. Site owners can customize model introductions according to the situation. Also supports a preset system, including **custom presets** and **cloud synchronization** functions.
9. 📖 **Rich File Parsing**: **Out-of-the-box**, supports file parsing for **all models** (PDF / Docx / Pptx / Excel / image formats parsing), **supports more cloud image storage solutions** (S3 / R2 / MinIO etc.), **supports OCR image recognition** 👉 See project [Chat Nio Blob Service](https://github.com/Deeptrain-Community/chatnio-blob-service) for details (supports Vercel / Docker one-click deployment)
10. 🌏 **Full Model Internet Search**: Based on the [SearXNG](https://github.com/searxng/searxng) open-source engine, supports rich search engines such as Google / Bing / DuckDuckGo / Yahoo / Wikipedia / Arxiv / Qwant, supports safe search mode, content truncation, image proxy, test search availability, and other functions.
11. 💕 **Progressive Web App (PWA)**: Supports PWA applications & desktop support (desktop based on [Tauri](https://github.com/tauri-apps/tauri))
12. 🤩 **Comprehensive Backend Management**: Supports beautiful and rich dashboard, announcement & notification management, user management, subscription management, gift code & redemption code management, price setting, subscription setting, custom model market, custom site name & logo, SMTP email settings, and other functions
13. 🤑 **Multiple Billing Methods**: Supports 💴 **Subscription** and 💴 **Elastic Billing** two billing methods. Elastic billing supports per-request billing / token billing / no billing / anonymous calls and **minimum request points** detection and other powerful features
14. 🎉 **Innovative Model Caching**: Supports enabling model caching: i.e., under the same request parameter hash, if it has been requested before, it will directly return the cached result (hitting the cache will not be billed), reducing the number of requests. You can customize whether to cache models, cache time, multiple cache result numbers, and other advanced cache settings
15. 🥪 **Additional Features** (Support Discontinued): 🍎 **AI Project Generator Function** / 📂 **Batch Article Generation Function** / 🥪 **AI Card Function** (Deprecated)
16. 😎 **Excellent Channel Management**: Self-written excellent channel algorithm, supports ⚡ **multi-channel management**, supports 🥳**priority** setting for channel call order, supports 🥳**weight** setting for load balancing probability distribution of channels at the same priority, supports 🥳**user grouping**, 🥳**automatic retry on failure**, 🥳**model redirection**, 🥳**built-in upstream hiding**, 🥳**channel status management** and other powerful **enterprise-level functions**
17. ⭐ **OpenAI API Distribution & Proxy System**: Supports calling various large models in **OpenAI API** standard format, integrates powerful channel management functions, only needs to deploy one site to achieve simultaneous development of B/C-end business💖
18. 👌 **Quick Upstream Synchronization**: Channel settings, model market, price settings, and other settings can quickly synchronize with upstream sites, modify your site configuration based on this, quickly build your site, save time and effort, one-click synchronization, quick launch
19. 👋 **SEO Optimization**: Supports SEO optimization, supports custom site name, site logo, and other SEO optimization settings to make search engines crawl faster, making your site stand out👋
20. 🎫 **Multiple Redemption Code Systems**: Supports multiple redemption code systems, supports gift codes and redemption codes, supports batch generation, gift codes are suitable for promotional distribution, redemption codes are suitable for card sales, for gift codes of one type, a user can only redeem one code, which to some extent reduces the situation of one user redeeming multiple times in promotions😀
21. 🥰 **Business-Friendly License**: Adopts the **Apache-2.0** open-source license, friendly for commercial secondary development & distribution (please also comply with the provisions of the Apache-2.0 license, do not use for illegal purposes)

> ### ✨ Chat Nio Business
>
> ![Pro Version Preview](./screenshot/chatnio-pro.png)
>
> - ✅ Beautiful commercial-grade UI, elegant frontend interface and backend management
> - ✅ Supports TTS & STT, plugin marketplace, RAG knowledge base and other rich features and modules
> - ✅ More payment providers, more billing models and advanced order management
> - ✅ Supports more authentication methods, including SMS login, OAuth login, etc.
> - ✅ Supports model monitoring, channel health detection, fault alarm automatic channel switching
> - ✅ Supports multi-tenant API Key distribution system, enterprise-level token permission management and visitor restrictions
> - ✅ Supports security auditing, logging, model rate limiting, API Gateway and other advanced features
> - ✅ Supports promotion rewards, professional data statistics, user profile analysis and other business analysis capabilities
> - ✅ Supports Discord/Telegram/Feishu and other bot integration capabilities (extension modules)
> - ...
>
> [👉 Learn More](https://www.chatnio.com/docs/contact)


## 🔨 Supported Models
1. OpenAI & Azure OpenAI *(✅ Vision ✅ Function Calling)*
2. Anthropic Claude *(✅ Vision ✅ Function Calling)*
3. Google Gemini & PaLM2 *(✅ Vision)*
4. Midjourney *(✅ Mode Toggling ✅ U/V/R Actions)*
5. iFlytek SparkDesk *(✅ Vision ✅ Function Calling)*
6. Zhipu AI ChatGLM *(✅ Vision)*
7. Alibaba Tongyi Qwen
8. Tencent Hunyuan
9. Baichuan AI
10. Moonshot AI (👉 OpenAI)
11. DeepSeek AI (👉 OpenAI)
12. ByteDance Skylark *(✅ Function Calling)*
13. Groq Cloud AI
14. OpenRouter (👉 OpenAI)
15. 360 GPT
16. LocalAI / Ollama (👉 OpenAI)

## 👻 OpenAI Compatible API Proxy
   - [x] Chat Completions _(/v1/chat/completions)_
   - [x] Image Generation _(/v1/images)_
   - [x] Model List _(/v1/models)_
   - [x] Dashboard Billing _(/v1/billing)_


## 📦 Deployment
> [!TIP]
> **After successful deployment, the admin account is `root`, with the default password `chatnio123456`**

### ✨ Zeabur (One-Click)
[![Deploy on Zeabur](https://zeabur.com/button.svg)](https://zeabur.com/templates/M86XJI)

> Zeabur provides a certain free quota, you can use non-paid regions for one-click deployment, and also supports plan subscriptions and elastic billing for flexible expansion.
> 1. Click `Deploy` to deploy, and enter the domain name you wish to bind, wait for the deployment to complete.
> 2. After deployment is complete, please visit your domain name and log in to the backend management using the username `root` and password `chatnio123456`. Please follow the prompts to change the password in the chatnio backend in a timely manner.

### ⚡ Docker Compose Installation (Recommended)
> [!NOTE]
> After successful execution, the host machine mapping address is `http://localhost:8000`

```shell
git clone --depth=1 --branch=main --single-branch https://github.com/Deeptrain-Community/chatnio.git
cd chatnio
docker-compose up -d # Run the service
# To use the stable version, use docker-compose -f docker-compose.stable.yaml up -d instead
# To use Watchtower for automatic updates, use docker-compose -f docker-compose.watch.yaml up -d instead
```

Version update (_If Watchtower automatic updates are enabled, manual updates are not necessary_):
```shell
docker-compose down 
docker-compose pull
docker-compose up -d
```

> - MySQL database mount directory: ~/**db**
> - Redis database mount directory: ~/**redis**
> - Configuration file mount directory: ~/**config**

### ⚡ Docker Installation (Lightweight runtime, commonly used for external _MYSQL/RDS_ services)
> [!NOTE]
> After successful execution, the host machine address is `http://localhost:8094`.
> 
> To use the stable version, use `programzmh/chatnio:stable` instead of `programzmh/chatnio:latest`

```shell
docker run -d --name chatnio \
   --network host \
   -v ~/config:/config \
   -v ~/logs:/logs \
   -v ~/storage:/storage \
   -e MYSQL_HOST=localhost \
   -e MYSQL_PORT=3306 \
   -e MYSQL_DB=chatnio \
   -e MYSQL_USER=root \
   -e MYSQL_PASSWORD=chatnio123456 \
   -e REDIS_HOST=localhost \
   -e REDIS_PORT=6379 \
   -e SECRET=secret \
   -e SERVE_STATIC=true \
   programzmh/chatnio:latest
```

> - *--network host* means using the host machine's network, allowing the Docker container to use the host's network. You can modify this as needed.
> - SECRET: JWT secret key, generate a random string and modify accordingly
> - SERVE_STATIC: Whether to enable static file serving (normally this doesn't need to be changed, see FAQ below for details)
> - *-v ~/config:/config* mounts the configuration file, *-v ~/logs:/logs* mounts the host machine directory for log files, *-v ~/storage:/storage* mounts the directory for additional feature generated files
> - MySQL and Redis services need to be configured. Please refer to the information above to modify the environment variables accordingly

Version update (_After enabling Watchtower, manual updates are not necessary. After execution, follow the steps above to run again_):

```shell
docker stop chatnio
docker rm chatnio
docker pull programzmh/chatnio:latest
```

### ⚒ Compile and Install

> [!NOTE]
> After successful deployment, the default port is **8094**, and the access address is `http://localhost:8094`
> 
> Config settings (~/config/**config.yaml**) can be overridden using environment variables. For example, the `MYSQL_HOST` environment variable can override the `mysql.host` configuration item

```shell
git clone https://github.com/Deeptrain-Community/chatnio.git
cd chatnio

cd app
npm install -g pnpm
pnpm install
pnpm build

cd ..
go build -o chatnio

# e.g. using nohup (you can also use systemd or other service manager)
nohup ./chatnio > output.log & # using nohup to run in background
```

## 📦 Tech Stack

- 🥗 Frontend: React + Redux + Radix UI + Tailwind CSS
- 🍎 Backend: Golang + Gin + Redis + MySQL
- 🍒 Application Technology: PWA + WebSocket

## 🤯 Why Create This Project & Project Advantages

- We found that most AIGC commercial sites on the market are frontend-oriented lightweight deployment projects with beautiful UI interface designs, such as the commercial version of [Next Chat](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web). Due to its personal privatization-oriented design, there are some limitations in secondary commercial development, presenting some issues, such as:
  1. **Difficult conversation synchronization**, for example, requiring services like WebDav, high user learning costs, and difficulties in real-time cross-device synchronization.
  2. **Insufficient billing**, for example, only supporting elastic billing or only subscription-based, unable to meet the needs of different users.
  3. **Inconvenient file parsing**, for example, only supporting uploading images to an image hosting service first, then returning to the site to input the URL direct link in the input box, without built-in file parsing functionality.
  4. **No support for conversation URL sharing**, for example, only supporting conversation screenshot sharing, unable to support conversation URL sharing (or only supporting tools like ShareGPT, which cannot promote the site).
  5. **Insufficient channel management**, for example, the backend only supports OpenAI format channels, making it difficult to be compatible with other format channels. And only one channel can be filled in, unable to support multi-channel management.
  6. **No API call support**, for example, only supporting user interface calls, unable to support API proxying and management.

- Another type is API distribution-oriented sites with powerful distribution systems, such as projects based on [One API](https://github.com/songquanpeng/one-api).
Although these projects support powerful API proxying and management, they lack interface design and some C-end features, such as:
  1. **Insufficient user interface**, for example, only supporting API calls, without built-in user interface chat. User interface chat requires manually copying the key and going to other sites to use, which has a high learning cost for ordinary users.
  2. **No subscription system**, for example, only supporting elastic billing, lacking billing design for C-end users, unable to meet different user needs, and not user-friendly in terms of cost perception for users without a foundation.
  3. **Insufficient C-end features**, for example, only supporting API calls, not supporting conversation synchronization, conversation sharing, file parsing, and other functions.
  4. **Insufficient load balancing**, the open-source version does not support the **weight** parameter, unable to achieve balanced load distribution probability for channels at the same priority ([New API](https://github.com/Calcium-Ion/new-api) also solves this pain point, with a more beautiful UI).

Therefore, we hope to combine the advantages of these two types of projects to create a project that has both a powerful API distribution system and a rich user interface design,
thus meeting the needs of C-end users while developing B-end business, improving user experience, reducing user learning costs, and increasing user stickiness.

Thus, **Chat Nio** was born. We hope to create a project that has both a powerful API distribution system and a rich user interface design, becoming the next-generation open-source AIGC project's one-stop commercial solution.


## ❤ Donations

If you find this project helpful, you can give it a Star to show your support!
