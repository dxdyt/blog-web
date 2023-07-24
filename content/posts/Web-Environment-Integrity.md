---
title: Web-Environment-Integrity
date: 2023-07-24T12:16:53+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1689832870997-18b825b4b676?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTAxNzIxMTB8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1689832870997-18b825b4b676?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTAxNzIxMTB8&ixlib=rb-4.0.3
---

# [RupertBenWiser/Web-Environment-Integrity](https://github.com/RupertBenWiser/Web-Environment-Integrity)

# Web Environment Integrity API

This repository details the proposal to add a new API for determining the integrity
of web environments:

```js
const attestation = await navigator.getEnvironmentIntegrity("...");
```

The [explainer](./explainer.md) goes gives a high level overview of the proposal.

The [spec](https://rupertbenwiser.github.io/Web-Environment-Integrity/) currently describes how this is being prototyped in Chromium.
