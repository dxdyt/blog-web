---
title: codel
date: 2024-03-27T12:18:01+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1707400711008-dd2fa19e76ef?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTE1MTMwMjJ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1707400711008-dd2fa19e76ef?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTE1MTMwMjJ8&ixlib=rb-4.0.3
---

# [semanser/codel](https://github.com/semanser/codel)

<div align="center">
  <img src="./.github/logo.png" width="200" />
</div>

<div align="center">Fully autonomous AI Agent that can perform complicated tasks and projects using terminal, browser, and editor.</div>

<img src="./.github/demo.png" />

Discord: https://discord.gg/uMaGSHNjzc

# Features
- 🔓 Secure. Everything is running in a sandboxed Docker environment.
- 🤖 Autonomous. Automatically detects the next step and performs it.
- 🔍 Built-in browser. Fetches latest information from the web (tutorials, docs, etc.) if needed.
- 📙 Built-in text editor. View all the modified files right in your browser.
- 🧠 All the history commands and outputs are saved in the PostgreSQL database.
- 📦 Automatic Docker-image picker based on the user task.
- 🤳 Self-hosted
- 💅 Modern UI

# How to run
## Prerequisites
- golang
- nodejs
- docker

## Environment variables
Add to `.env` file in the `backend` folder.

### Backend
- `OPEN_AI_KEY` - OpenAI API key
- `DATABASE_URL` - PostgreSQL database URL (eg. `postgres://user:password@localhost:5432/database`)
- `DOCKER_HOST` - Docker SDK API (eg. `DOCKER_HOST=unix:///Users/<my-user>/Library/Containers/com.docker.docker/Data/docker.raw.sock`) [more info](https://stackoverflow.com/a/62757128/5922857)

Optional:
- `OPEN_AI_MODEL` - OpenAI model (default: `gpt-4-0125-preview`). The list of supported OpenAI models can be found [here](https://pkg.go.dev/github.com/sashabaranov/go-openai#pkg-constants).
### Frontend
Frontend environment variables can be set by creating a `.env.local` file in the `frontend` folder.
- `VITE_API_URL` - Backend API URL. *Omit* the URL scheme (e.g., `localhost:8080` *NOT* `http://localhost:8080`).

## Steps
- Run `go run .` in `backend` folder
- Run `yarn dev` in `frontend` folder
- Open your browser and enjoy!

# Roadmap
- [x] Agent API
- [x] Frontend
- [x] Backend API + PostgreSQL integration
- [x] Docker runner
- [x] Terminal output streaming
- [ ] Browser output streaming (in progress)
- [ ] Editor output
- [ ] SWE-bench
- [ ] Better way to run it (eg a single docker command)



# Credits
This project wouldn't be possible without:
- https://arxiv.org/abs/2308.00352
- https://arxiv.org/abs/2403.08299
- https://www.cognition-labs.com/introducing-devin
- https://github.com/semanser/JsonGenius
