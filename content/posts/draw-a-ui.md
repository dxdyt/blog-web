---
title: draw-a-ui
date: 2023-11-13T12:15:26+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1699126600586-9bc597e5ee2d?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk4NDg5MTd8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1699126600586-9bc597e5ee2d?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTk4NDg5MTd8&ixlib=rb-4.0.3
---

# [SawyerHood/draw-a-ui](https://github.com/SawyerHood/draw-a-ui)

# draw-a-ui

This is an app that uses tldraw and the gpt-4-vision api to generate html based on a wireframe you draw.

![A demo of the app](./demo.gif)

This works by just taking the current canvas SVG, converting it to a PNG, and sending that png to gpt-4-vision with instructions to return a single html file with tailwind.

> Disclaimer: This is a demo and is not intended for production use. It doesn't have any auth so you will go broke if you deploy it.

## Getting Started

This is a Next.js app. To get started run the following commands in the root directory of the project. You will need an OpenAI API key with access to the GPT-4 Vision API.

```bash
echo "OPENAI_API_KEY=sk-your-key" > .env.local
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.