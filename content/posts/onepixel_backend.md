---
title: onepixel_backend
date: 2023-11-07T12:16:13+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1697163524619-c98e0b4140e8?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTkzMzA1MTR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1697163524619-c98e0b4140e8?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTkzMzA1MTR8&ixlib=rb-4.0.3
---

# [championswimmer/onepixel_backend](https://github.com/championswimmer/onepixel_backend)

# onepixel (1px.li)

Backend code for the 1px.li URL shortener service.

#### Status Badges 
[![codecov](https://codecov.io/gh/championswimmer/onepixel_backend/graph/badge.svg?token=DL3DR6CS40)](https://codecov.io/gh/championswimmer/onepixel_backend)
[![Build and test](https://github.com/championswimmer/onepixel_backend/actions/workflows/build_test.yaml/badge.svg)](https://github.com/championswimmer/onepixel_backend/actions/workflows/build_test.yaml)

## Development 

### Deploy everything (with Docker)

Simplest way to get it running is 

1. make a `./data` directory where your database will be stored 
2. run `docker-compose up`

### Run with hot-reload for local development 

We will use docker to run an instance of database, but we will run the project using [air](https://github.com/cosmtrek/air) locally  

1. make a `./data` directory where your database will be stored
2. run `docker-compose up -d postgres`
3. add `127.0.0.1    postgres` to your `/etc/hosts` file <sup>1</sup>
4. run `air` in the root directory of the project <sup>2</sup>


> Note[1] This is because the server is configured to connect to `host=postgres` for the database.

> Note[2]: you can also run `go run src/main.go` but it will not reload on changes
