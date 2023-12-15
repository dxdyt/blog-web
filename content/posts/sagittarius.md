---
title: sagittarius
date: 2023-12-15T12:17:16+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1700387412251-0e747cb53b6b?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDI2MTM3NTh8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1700387412251-0e747cb53b6b?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDI2MTM3NTh8&ixlib=rb-4.0.3
---

# [gregsadetsky/sagittarius](https://github.com/gregsadetsky/sagittarius)

# A Remake of the Google Gemini Fake Demo, Except Using GPT-4 and It's Real

[Original video here](https://www.youtube.com/watch?v=__nL7Vc0OCg).

[Heads-to-heads comparison of Gemini Pro and GPT-4](https://www.youtube.com/watch?v=1RrkRA7wuoE).

## how to build

- clone this repo, cd into it
- duplicate `.env.example` and name the copy `.env`
- fill out the `VITE_OPENAI_KEY=` value with your OpenAI api key. you must have access to the `gpt-4-vision-preview` model
- you can also try out the Gemini API if you have a key -- fill out `VITE_GEMINI_KEY` in the same `.env`
- then, run:
- `npm install`
- `npm run dev`
- the demo will be running at [http://localhost:5173](http://localhost:5173)

note: the in-browser speech recognition works best in Google Chrome
