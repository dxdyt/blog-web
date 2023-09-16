---
title: whisper-turbo
date: 2023-09-16T12:14:42+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1694119548114-0427d1f51cf6?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTQ4Mzc2NDN8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1694119548114-0427d1f51cf6?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTQ4Mzc2NDN8&ixlib=rb-4.0.3
---

# [FL33TW00D/whisper-turbo](https://github.com/FL33TW00D/whisper-turbo)

<div align="center">
<img width="550px" height="200px" src="https://github.com/FL33TW00D/whisper-turbo/raw/master/.github/whisper-turbo.png">
<p><a href="https://whisper-turbo.com">Demo Site</a> | <a href="">Docs</a> | <a href="https://github.com/users/FL33TW00D/projects/1"> Roadmap </a></p>
</div>


## What is Whisper Turbo?
Whisper Turbo is a lightning-fast, **cross-platform** Whisper implementation, designed to run entirely client-side on your browser or electron app.
Powered by Rust, WebAssembly & WebGPU, you can see ~20x real-time speeds.

Being client-side, Whisper-Turbo offers a few key benefits:
1. Real-time streaming (WIP) - simply speak into your microphone and watch the text appear in real-time like a sci-fi movie.
2. Completely private & offline
3. Free!*

## Supported Platforms

WebGPU is only currently available on stable release Chrome Version >= 113.
Firefox & Safari do not currently ship WebGPU.

Windows + MacOS are supported, Linux is not.
Given that WebGPU is not supported on all platforms, we (intend to) offer the ability to provide your OAI key, so that
100% of your users have the best possible experience.

## Install

In alpha currently, use at your own risk.

```bash
npm install whisper-turbo
```

## Docs

Coming soon

## Want to help?

- Are you a GPU wizard?
- Do you know what a HRTB is in Rust?
- Do you know what is going on [here](https://github.com/RuyiLi/cursed-typescript/blob/master/random/game-of-life.ts)?
- Reach out: chris@fleetwood.dev
