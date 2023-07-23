---
title: Walnut
date: 2023-07-23T12:15:30+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1688367785310-c8c013548288?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTAwODU2NjR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1688367785310-c8c013548288?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTAwODU2NjR8&ixlib=rb-4.0.3
---

# [StudioCherno/Walnut](https://github.com/StudioCherno/Walnut)

# Walnut

Walnut is a simple application framework built with Dear ImGui and designed to be used with Vulkan - basically this means you can seemlessly blend real-time Vulkan rendering with a great UI library to build desktop applications. The plan is to expand Walnut to include common utilities to make immediate-mode desktop apps and simple Vulkan applications.

Currently supports Windows - with macOS and Linux support planned. Setup scripts support Visual Studio 2022 by default.

![WalnutExample](https://hazelengine.com/images/ForestLauncherScreenshot.jpg)
_<center>Forest Launcher - an application made with Walnut</center>_

## Requirements
- [Visual Studio 2022](https://visualstudio.com) (not strictly required, however included setup scripts only support this)
- [Vulkan SDK](https://vulkan.lunarg.com/sdk/home#windows) (preferably a recent version)

## Getting Started
Once you've cloned, run `scripts/Setup.bat` to generate Visual Studio 2022 solution/project files. Once you've opened the solution, you can run the WalnutApp project to see a basic example (code in `WalnutApp.cpp`). I recommend modifying that WalnutApp project to create your own application, as everything should be setup and ready to go.

### 3rd party libaries
- [Dear ImGui](https://github.com/ocornut/imgui)
- [GLFW](https://github.com/glfw/glfw)
- [stb_image](https://github.com/nothings/stb)
- [GLM](https://github.com/g-truc/glm) (included for convenience)

### Additional
- Walnut uses the [Roboto](https://fonts.google.com/specimen/Roboto) font ([Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0))