---
title: orange
date: 2024-04-08T12:17:51+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1711065917747-e9570ba94c5f?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTI1NDk3NTd8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1711065917747-e9570ba94c5f?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MTI1NDk3NTd8&ixlib=rb-4.0.3
---

# [cloudflare/orange](https://github.com/cloudflare/orange)

# Welcome to Orange Meets

Orange Meets is a demo application built using [Cloudflare Calls](https://developers.cloudflare.com/calls/).
To build your own WebRTC application using Cloudflare Calls, get started in the [Cloudflare Dashboard](https://dash.cloudflare.com/?to=/:account/calls).

[Try the demo here!](https://demo.orange.cloudflare.dev)

![A screenshot showing a room in Orange Meets](orange-meets.png)

## Variables

Go to the [Cloudflare Calls dashboard](https://dash.cloudflare.com/?to=/:account/calls) and create an application.

Put these variables into `.dev.vars`

```
CALLS_APP_ID=<APP_ID_GOES_HERE>
CALLS_APP_SECRET=<SECRET_GOES_HERE>
```

## Development

```sh
npm run dev
```

Open up [http://127.0.0.1:8787](http://127.0.0.1:8787) and you should be ready to go!

## Deployment

1. Make sure you've installed `wrangler` and are logged in by running:

```sh
wrangler login
```

2. Update the `account_id` and `CALLS_APP_ID` in `wrangler.toml` to use your own Cloudflare Account ID and Calls App ID

3. You will also need to set the token as a secret by running:

```sh
wrangler secret put CALLS_APP_SECRET
```

4. Then you can run

```sh
npm run deploy
```
