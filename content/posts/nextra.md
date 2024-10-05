---
title: nextra
date: 2024-09-30T12:21:57+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1727294810277-5da030783146?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3Mjc2NzAwMDd8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1727294810277-5da030783146?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3Mjc2NzAwMDd8&ixlib=rb-4.0.3
---

# [shuding/nextra](https://github.com/shuding/nextra)

# Nextra

Simple, powerful and flexible site generation framework with everything you love
from Next.js.

## Documentation

https://nextra.site

## Development

### Installation

The Nextra repository uses [PNPM Workspaces](https://pnpm.io/workspaces) and
[Turborepo](https://github.com/vercel/turborepo). To install dependencies, run
`pnpm install` in the project root directory.

### Build Nextra Core

```bash
cd packages/nextra
pnpm build
```

Watch mode: `pnpm dev`

### Build Nextra Theme

```bash
cd packages/nextra-theme-docs
pnpm build
```

| Command           | Description              |
| ----------------- | ------------------------ |
| pnpm dev          | Watch mode               |
| pnpm dev:layout   | Watch mode (layout only) |
| pnpm dev:tailwind | Watch mode (style only)  |

### Development

You can also debug them together with a website locally. For instance, to start
examples/docs locally, run

```bash
cd examples/docs
pnpm dev
```

Any change to example/docs will be re-rendered instantly.

If you update the core or theme packages, a rebuild is required. Or you can use
the watch mode for both nextra and the theme in separated terminals.

### Sponsors

<div>
 <a href="https://speakeasyapi.dev/docs?utm_source=github&utm_campaign=nextra&utm_content=logolink">
   <img src="/docs/pages/showcase/speakeasy.png" alt="Speakeasy" width="256">
 </a>
</div>