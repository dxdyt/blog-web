---
title: coze-discord-proxy
date: 2024-02-02T12:18:09+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1706009260917-302d912a3074?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDY4NDczNDR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1706009260917-302d912a3074?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDY4NDczNDR8&ixlib=rb-4.0.3
---

# [deanxv/coze-discord-proxy](https://github.com/deanxv/coze-discord-proxy)

<div align="center">

# coze-discord-proxy

_coze+discord 代理服务—通过接口调用被`coze`托管的`discord-bot`_

_觉得有点意思的话 别忘了点个🌟_

🐞<a href="https://t.me/+LGKwlC_xa-E5ZDk9" style="font-size: 15px;">COZE-DISCORD-PROXY交流群</a>

</div>

## 功能

- [x] 完美适配`NextChat`,`one-api`,`LobeChat`等
- [x] 对话支持流式返回
- [x] 对话支持文生图(需`coze`配置`DALL·E3`插件)返回图片url
- [x] 对话支持图生文(需`coze`配置`GPT4V`插件)(发送的文本消息中携带图片url/按照GPT4V识图请求格式发起请求)
- [x] 支持创建 `discord`频道/子频道/线程
- [x] 支持对话指定 `discord`频道/子频道/线程 实现对话隔离
- [x] 支持和`openai`对齐的对话接口(`v1/chat/completions`)(支持文生图)
- [x] 支持和`openai`对齐的GPT4V识图接口(`v1/chat/completions`)(读取 `url`/`base64`)
- [x] 支持和`openai`对齐的`dall-e-3`接口(`v1/images/generations`)
- [x] 支持配置多个[机器人-频道] (通过`PROXY_SECRET`指定) 详细请看[进阶配置](#进阶配置)

### 接口文档:

`http://<ip>:<port>/swagger/index.html`

<span><img src="docs/img.png" width="800"/></span>

### 示例:

<span><img src="docs/img2.png" width="800"/></span>

## 如何使用

1. 打开 [discord开发者平台](https://discord.com/developers/applications) 。
2. 创建bot-A,并记录bot专属的`token`和`id(COZE_BOT_ID)`,此bot为被coze托管的bot。
3. 创建bot-B,并记录bot专属的`token(BOT_TOKEN)`,此bot为我们与discord交互的bot。
4. 两个bot开通对应权限(`Send Messages`,`Read Message History`等)并邀请进服务器,记录服务器ID(`GUILD_ID`) (
   过程不在此赘述)。
5. 打开 [coze官网](https://www.coze.com) 创建自己bot。
6. 创建好后推送，配置discord-bot的`token`,即bot-A的`token`,点击完成后在discord的服务器中可看到bot-A在线并可以@使用。
7. 配置环境变量，并启动本项目。
8. 访问接口地址即可开始调试。

## 如何集成NextChat

填 接口地址(ip:端口/域名) 及 API-Key(`PROXY_SECRET`)，其它的随便填随便选。

> 如果自己没有搭建NextChat面板，这里有个已经搭建好的可以使用 [NextChat](https://ci.goeast.io/)

<span><img src="docs/img5.png" width="800"/></span>

## 如何集成one-api

填 `BaseURL`(ip:端口/域名) 及 密钥(`PROXY_SECRET`)，其它的随便填随便选。

<span><img src="docs/img3.png" width="800"/></span>

## 部署

### 基于 Docker-Compose(All In One) 进行部署

```shell
docker-compose pull && docker-compose up -d
```

#### docker-compose.yml

```docker
version: '3.4'

services:
  coze-discord-proxy:
    image: deanxv/coze-discord-proxy:latest
    container_name: coze-discord-proxy
    restart: always
    ports:
      - "7077:7077"
    volumes:
      - ./data:/app/coze-discord-proxy/data
    environment:
      - BOT_TOKEN=MTE5OTk2xxxxxxxxxxxxxxrwUrUWNbG63w  # 必须修改为我们主动发送消息的Bot-Token
      - GUILD_ID=119xxxxxxxx796  # 必须修改为两个机器人所在的服务器ID
      - COZE_BOT_ID=119xxxxxxxx7  # 必须修改为由coze托管的机器人ID
      - CHANNEL_ID=119xxxxxx24  # 默认频道-在使用与openai对齐的接口时(/v1/chat/completions) 消息会默认发送到此频道
      - PROXY_SECRET=123456  # [可选]接口密钥-修改此行为请求头校验的值(多个请以,分隔)
      - TZ=Asia/Shanghai
```

### 基于 Docker 进行部署

```shell
docker run --name coze-discord-proxy -d --restart always \
-p 7077:7077 \
-v $(pwd)/data:/app/coze-discord-proxy/data \
-e BOT_TOKEN="MTE5OTk2xxxxxxxxxxxxxxrwUrUWNbG63w" \
-e GUILD_ID="119xxxxxxxx796" \
-e COZE_BOT_ID="119xxxxxxxx7" \
-e PROXY_SECRET="123456" \
-e CHANNEL_ID="119xxxxxx24" \
-e TZ=Asia/Shanghai \
deanxv/coze-discord-proxy
```

其中，`BOT_TOKEN`,`GUILD_ID`,`COZE_BOT_ID`,`PROXY_SECRET`,`CHANNEL_ID`修改为自己的。

### 部署到第三方平台

<details>
<summary><strong>部署到 Zeabur</strong></summary>
<div>

> Zeabur 的服务器在国外，自动解决了网络的问题，同时免费的额度也足够个人使用

点击一键部署:

[![Deploy on Zeabur](https://zeabur.com/button.svg)](https://zeabur.com/templates/GMU8C8?referralCode=deanxv)

**一键部署后 `BOT_TOKEN`,`GUILD_ID`,`COZE_BOT_ID`,`PROXY_SECRET`,`CHANNEL_ID`变量也需要替换！**

或手动部署:

1. 首先 **fork** 一份代码。
2. 进入 [Zeabur](https://zeabur.com?referralCode=deanxv)，使用github登录，进入控制台。
3. 在 Service -> Add Service，选择 Git（第一次使用需要先授权），选择你 fork 的仓库。
4. Deploy 会自动开始，先取消。
5. 添加环境变量

   `BOT_TOKEN:MTE5OTk2xxxxxxxxxxxxxxrwUrUWNbG63w`  主动发送消息的Bot-Token

   `GUILD_ID:119xxxxxxxx796`  两个机器人所在的服务器ID

   `COZE_BOT_ID:119xxxxxxxx7` 由coze托管的机器人ID

   `CHANNEL_ID:119xxxxxx24`  # 默认频道-在使用与openai对齐的接口时(/v1/chat/completions) 消息会默认发送到此频道

   `PROXY_SECRET:123456` [可选]接口密钥-修改此行为请求头校验的值(多个请以,分隔)，配置此参数后，每次发起请求时请求头加上`proxy-secret`
   参数，即`header`中添加 `proxy-secret：123456`

保存。

6. 选择 Redeploy。

</div>


</details>

<details>
<summary><strong>部署到 Render</strong></summary>
<div>

> Render 提供免费额度，绑卡后可以进一步提升额度

Render 可以直接部署 docker 镜像，不需要 fork 仓库：[Render](https://dashboard.render.com)

</div>
</details>

## 配置

### 环境变量

1. `BOT_TOKEN:MTE5OTk2xxxxxxxxxxxxxxrwUrUWNbG63w`  主动发送消息的Bot-Token
2. `GUILD_ID:119xxxxxxxx796`  两个机器人所在的服务器ID
3. `COZE_BOT_ID:119xxxxxxxx7`  由coze托管的机器人ID
4. `CHANNEL_ID:119xxxxxx24`  默认频道-在使用与openai对齐的接口时(/v1/chat/completions) 消息会默认发送到此频道
5. `PROXY_SECRET:123456`  [可选]接口密钥-修改此行为请求头校验的值(多个请以,分隔),配置此参数后，每次发起请求时请求头加上`proxy-secret`
   参数，即`header`中添加 `proxy-secret：123456`
6. `REQUEST_OUT_TIME:60`  [可选]对话接口非流响应下的请求超时时间
7. `STREAM_REQUEST_OUT_TIME:60`  [可选]对话接口流响应下的每次流返回超时时间
8. `PROXY_URL:http://127.0.0.1:10801`  [可选]代理

## 进阶配置

### 配置多个[机器人-频道]

1. 部署前在`docker`/`docker-compose`部署同级目录下创建`data/config/bot_config.json`文件
2. 编写该`json`文件,`bot_config.json`格式如下

```shell
[
  {
    "proxySecret": "123", // 接口请求密钥(PROXY_SECRET)
    "cozeBotId": "12***************31", // coze托管的机器人ID
    "channelId": "12***************56"  // discord频道ID(机器人必须在此频道所在的服务器)
  },
  {
    "proxySecret": "456",
    "cozeBotId": "12***************64",
    "channelId": "12***************78"
  },
  {
    "proxySecret": "789",
    "cozeBotId": "12***************12",
    "channelId": "12***************24"
  }
]
```

3. 重启服务

> 当有此配置时,会通过请求头携带的请求密钥匹配此配置中的`cozeBotId`,`channelId`,若匹配到多个则随机匹配一个，所以当存在多用户使用时可对每个用户分发独立的请求密钥。

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=deanxv/coze-discord-proxy&type=Date)](https://star-history.com/#deanxv/coze-discord-proxy&Date)

## 其他

Coze 官网 : https://www.coze.com

Discord 开发地址 : https://discord.com/developers/applications



