---
title: clash-verge-rev
date: 2025-08-18T12:39:16+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1753010840134-45b2b059a7d5?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTU0OTE4Njl8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1753010840134-45b2b059a7d5?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTU0OTE4Njl8&ixlib=rb-4.1.0
---

# [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)

<h1 align="center">
  <img src="./src-tauri/icons/icon.png" alt="Clash" width="128" />
  <br>
  Continuation of <a href="https://github.com/zzzgydi/clash-verge">Clash Verge</a>
  <br>
</h1>

<h3 align="center">
A Clash Meta GUI based on <a href="https://github.com/tauri-apps/tauri">Tauri</a>.
</h3>

## Preview

| Dark                             | Light                             |
| -------------------------------- | --------------------------------- |
| ![预览](./docs/preview_dark.png) | ![预览](./docs/preview_light.png) |

## Install

请到发布页面下载对应的安装包：[Release page](https://github.com/clash-verge-rev/clash-verge-rev/releases)<br>
Go to the [Release page](https://github.com/clash-verge-rev/clash-verge-rev/releases) to download the corresponding installation package<br>
Supports Windows (x64/x86), Linux (x64/arm64) and macOS 10.15+ (intel/apple).

#### 我应当怎样选择发行版

| 版本      | 特征                                     | 链接                                                                                   |
| :-------- | :--------------------------------------- | :------------------------------------------------------------------------------------- |
| Stable    | 正式版，高可靠性，适合日常使用。         | [Release](https://github.com/clash-verge-rev/clash-verge-rev/releases)                 |
| Alpha     | 早期测试版，功能未完善，可能存在缺陷。   | [Alpha](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/alpha)         |
| AutoBuild | 滚动更新版，持续集成更新，适合开发测试。 | [AutoBuild](https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/autobuild) |

#### 安装说明和常见问题，请到 [文档页](https://clash-verge-rev.github.io/) 查看

---

### TG 频道: [@clash_verge_rev](https://t.me/clash_verge_re)

## Promotion

#### [狗狗加速 —— 技术流机场 Doggygo VPN](https://verge.dginv.click/#/register?code=oaxsAGo6)

- 高性能海外机场，免费试用，优惠套餐，解锁流媒体，全球首家支持 Hysteria 协议。
- 使用 Clash Verge 专属邀请链接注册送 3 天，每天 1G 流量免费试用：[点此注册](https://verge.dginv.click/#/register?code=oaxsAGo6)
- Clash Verge 专属 8 折优惠码: verge20 (仅有 500 份)
- 优惠套餐每月仅需 15.8 元，160G 流量，年付 8 折
- 海外团队，无跑路风险，高达 50% 返佣
- 集群负载均衡设计，高速专线(兼容老客户端)，极低延迟，无视晚高峰，4K 秒开
- 全球首家 Hysteria 协议机场，现已上线更快的 `Hysteria2` 协议(Clash Verge 客户端最佳搭配)
- 解锁流媒体及 ChatGPT
- 官网：[https://狗狗加速.com](https://verge.dginv.click/#/register?code=oaxsAGo6)

#### 本项目的构建与发布环境由 [YXVM](https://yxvm.com/aff.php?aff=827) 独立服务器全力支持，

感谢提供 独享资源、高性能、高速网络 的强大后端环境。如果你觉得下载够快、使用够爽，那是因为我们用了好服务器！

🧩 YXVM 独立服务器优势：

- 🌎 优质网络，回程优化，下载快到飞起
- 🔧 物理机独享资源，非VPS可比，性能拉满
- 🧠 适合跑代理、搭建 WEB 站 CDN 站 、搞 CI/CD 或任何高负载应用
- 💡 支持即开即用，多机房选择，CN2 / IEPL 可选
- 📦 本项目使用配置已在售，欢迎同款入手！
- 🎯 想要同款构建体验？[立即下单 YXVM 独立服务器！](https://yxvm.com/aff.php?aff=827)

## Features

- 基于性能强劲的 Rust 和 Tauri 2 框架
- 内置[Clash.Meta(mihomo)](https://github.com/MetaCubeX/mihomo)内核，并支持切换 `Alpha` 版本内核。
- 简洁美观的用户界面，支持自定义主题颜色、代理组/托盘图标以及 `CSS Injection`。
- 配置文件管理和增强（Merge 和 Script），配置文件语法提示。
- 系统代理和守卫、`TUN(虚拟网卡)` 模式。
- 可视化节点和规则编辑
- WebDav 配置备份和同步

### FAQ

Refer to [Doc FAQ Page](https://clash-verge-rev.github.io/faq/windows.html)

### Donation

[捐助Clash Verge Rev的开发](https://github.com/sponsors/clash-verge-rev)

## Development

See [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

To run the development server, execute the following commands after all prerequisites for **Tauri** are installed:

> [!NOTE]
> **If you are using a Windows ARM device, you additionally need to install [LLVM](https://github.com/llvm/llvm-project/releases) (including clang) and set the environment variable.**
>
> Because the `ring` crate is compiled based on `clang` under Windows ARM.

```shell
pnpm i
pnpm run prebuild
pnpm dev
```

## Contributions

Issue and PR welcome!

## Acknowledgement

Clash Verge rev was based on or inspired by these projects and so on:

- [zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge): A Clash GUI based on tauri. Supports Windows, macOS and Linux.
- [tauri-apps/tauri](https://github.com/tauri-apps/tauri): Build smaller, faster, and more secure desktop applications with a web frontend.
- [Dreamacro/clash](https://github.com/Dreamacro/clash): A rule-based tunnel in Go.
- [MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo): A rule-based tunnel in Go.
- [Fndroid/clash_for_windows_pkg](https://github.com/Fndroid/clash_for_windows_pkg): A Windows/macOS GUI based on Clash.
- [vitejs/vite](https://github.com/vitejs/vite): Next generation frontend tooling. It's fast!

## License

GPL-3.0 License. See [License here](./LICENSE) for details.
