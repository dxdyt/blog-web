---
title: grimoire
date: 2023-11-29T12:18:27+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1698254064280-d986d3d9cc91?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDEyMzEzNDF8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1698254064280-d986d3d9cc91?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDEyMzEzNDF8&ixlib=rb-4.0.3
---

# [goniszewski/grimoire](https://github.com/goniszewski/grimoire)

# Grimoire

![Grimoire Logo](static/grimoire_logo_300.webp)

Glimpse into the magical book of _your_ forbidden knowledge - **Grimoire!** 📖💫

Unleash your inner sorcerer and conquer the chaos of bookmarks! With Grimoire, you'll have a bewitching way to store and sort your enchanted links.

But wait, there's **more**!

Transmute your saved pages into juicy content snippets with our mystical extraction feature. Embrace the magic, tame the clutter, and let Grimoire be your mystical companion in the vast library of the web.

It's time to conjure up some organization! 📚✨

## Features

- add and organize bookmarks easily 🔖
- create new user accounts, each with their own bookmarks, categories and tags 🙋
- fuzzy search through bookmarks 🔍
- supports tags and categories 🏷️
- fetch metadata from websites, store it locally and update it when needed 🌐
- add your personal notes to bookmarks 📝

## Installation

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Steps

```bash
# Clone the repository
git clone https://github.com/goniszewski/grimoire

# [RECOMMENDED] Update the `.env.docker` to set the initial admin user credentials

# Build and run the containers
docker-compose up
```

## Development

Check out the [development guide](https://grimoire.pro/docs/getting-started/development) to learn how to set up the project for development.

## Roadmap

- sharing bookmarks with other users or publicly 🤸
- Flows - keep your bookmarks in a session-like order with related notes (e.g. for learning, research, etc.) 🔥
- import bookmarks from popular formats files 📤
- export bookmarks as HTML, CSV and JSON 📦
- add universal bookmarklet to add bookmarks from any browser 📎
- quickly change bookmark categories and tags from the bookmarks list ⏩
- the official browser extension 🌐

## Feature requests

If you have an idea for a feature, please [open an issue](https://github.com/goniszewski/grimoire/issues) and describe it in detail. If you have a mockup, please attach it to the issue.

## Contributing

If you want to contribute to the project, please read the [contributing guide](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

Special thanks to: [@extractus/article-extractor](https://github.com/extractus/article-extractor),
[DaisyUI](https://github.com/saadeghi/daisyui),
[Fuse.js](https://github.com/krisk/fuse),
[MetaScraper](https://github.com/microlinkhq/metascraper),
[PocketBase](https://github.com/pocketbase/pocketbase),
[sanitize-html](https://github.com/apostrophecms/sanitize-html),
[SvelteKit](https://github.com/sveltejs/kit),
[Svelte Select](https://github.com/rob-balfre/svelte-select),
[Svelte French Toast](https://github.com/kbrgl/svelte-french-toast),
[Tailwind CSS](https://tailwindcss.com)
