---
title: cms
date: 2024-04-14T12:38:06+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1711639105861-f55ef78adc51?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTMwNjk0MzJ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1711639105861-f55ef78adc51?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTMwNjk0MzJ8&ixlib=rb-4.0.3
---

# [code100x/cms](https://github.com/code100x/cms)

<h1 align='center'>CMS</h1>

## Setup Procedure

* Docker

    OR

* Copy .env.example to .env
* Get a postgres db from https://neon.tech/ (or any other provider)
* Replace the DATABASE_URL in .env
* Run ```npx prisma migrate dev``` to setup schema
## Steps to run locally
With Docker

* ```docker compose up```

Without Docker
* ```npm install```
* ```npm run db:seed``` to seed the database
* ```npm run dev```
* Login using any userid and password 123456
* You should be able to see some test courses

---

Read [contributing guidelines](./CONTRIBUTING.md) to start making contributions
