---
title: plugins
date: 2026-06-07T15:55:00+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1777863073427-63ea42020da9?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3ODA4MTg4NjR8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1777863073427-63ea42020da9?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3ODA4MTg4NjR8&ixlib=rb-4.1.0
---

# [openai/plugins](https://github.com/openai/plugins)

# Plugins

This repository contains a curated collection of Codex plugin examples.

Each plugin lives under `plugins/<name>/` with a required
`.codex-plugin/plugin.json` manifest and optional companion surfaces such as
`skills/`, `.app.json`, `.mcp.json`, plugin-level `agents/`, `commands/`,
`hooks.json`, `assets/`, and other supporting files.

Highlighted richer examples in this repo include:

- `plugins/figma` for `use_figma`, Code to Canvas, Code Connect, and design system rules
- `plugins/notion` for planning, research, meetings, and knowledge capture
- `plugins/build-ios-apps` for SwiftUI implementation, refactors, performance, and debugging
- `plugins/build-macos-apps` for macOS SwiftUI/AppKit workflows, build/run/debug loops, and packaging guidance
- `plugins/build-web-apps` for deployment, UI, payments, and database workflows
- `plugins/expo` for Expo and React Native apps, SDK upgrades, EAS workflows, and Codex Run actions
- `plugins/netlify`, `plugins/remotion`, and `plugins/google-slides` for additional public skill- and MCP-backed plugin bundles
