---
title: daily-code
date: 2024-04-15T12:29:26+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1712229307272-5cbb18c96f94?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTMxNTUyOTR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1712229307272-5cbb18c96f94?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTMxNTUyOTR8&ixlib=rb-4.0.3
---

# [code100x/daily-code](https://github.com/code100x/daily-code)

# Quick Setup Locally

> Install the Dependencies

```
cd daily-code
yarn install
```

> Copy the env example

```
cd  packages/db
cp .env.example .env
```

> Update the .env file with the database url

> Migrate and the Database

```
npx prisma migrate dev
npx prisma db seed
```

> If previous commands fail, try these; Otherwise, skip.

```
yarn prisma migrate dev
yarn prisma db seed
```

> Run locally

```
cd ../..
yarn run dev
```
