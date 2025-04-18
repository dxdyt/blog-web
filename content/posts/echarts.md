---
title: echarts
date: 2024-12-29T12:20:00+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1733591486986-2a9c1086c5d8?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzU0NDU5NDB8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1733591486986-2a9c1086c5d8?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzU0NDU5NDB8&ixlib=rb-4.0.3
---

# [apache/echarts](https://github.com/apache/echarts)

# Apache ECharts

<a href="https://echarts.apache.org/">
    <img style="vertical-align: top;" src="./asset/logo.png?raw=true" alt="logo" height="50px">
</a>

Apache ECharts is a free, powerful charting and visualization library offering easy ways to add intuitive, interactive, and highly customizable charts to your commercial products. It is written in pure JavaScript and based on <a href="https://github.com/ecomfe/zrender">zrender</a>, which is a whole new lightweight canvas library.

**[中文官网](https://echarts.apache.org/zh/index.html)** | **[ENGLISH HOMEPAGE](https://echarts.apache.org/en/index.html)**

[![License](https://img.shields.io/npm/l/echarts?color=5470c6)](https://github.com/apache/echarts/blob/master/LICENSE) [![Latest npm release](https://img.shields.io/npm/v/echarts?color=91cc75)](https://www.npmjs.com/package/echarts) [![NPM downloads](https://img.shields.io/npm/dm/echarts.svg?label=npm%20downloads&style=flat&color=fac858)](https://www.npmjs.com/package/echarts) [![Contributors](https://img.shields.io/github/contributors/apache/echarts?color=3ba272)](https://github.com/apache/echarts/graphs/contributors)

[![Build Status](https://github.com/apache/echarts/actions/workflows/ci.yml/badge.svg)](https://github.com/apache/echarts/actions/workflows/ci.yml)

## Get Apache ECharts

You may choose one of the following methods:

+ Download from the [official website](https://echarts.apache.org/download.html)
+ `npm install echarts --save`
+ CDN: [jsDelivr CDN](https://www.jsdelivr.com/package/npm/echarts?path=dist)

## Docs

+ [Get Started](https://echarts.apache.org/handbook)
+ [API](https://echarts.apache.org/api.html)
+ [Option Manual](https://echarts.apache.org/option.html)
+ [Examples](https://echarts.apache.org/examples)

## Get Help

+ [GitHub Issues](https://github.com/apache/echarts/issues) for bug report and feature requests
+ Email [dev@echarts.apache.org](mailto:dev@echarts.apache.org) for general questions
+ Subscribe to the [mailing list](https://echarts.apache.org/maillist.html) to get updated with the project

## Build

Build echarts source code:

Execute the instructions in the root directory of the echarts:
([Node.js](https://nodejs.org) is required)

```shell
# Install the dependencies from NPM:
npm install

# Rebuild source code immediately in watch mode when changing the source code.
# It opens the `./test` directory, and you may open `-cases.html` to get the list
# of all test cases.
# If you wish to create a test case, run `npm run mktest:help` to learn more.
npm run dev

# Check the correctness of TypeScript code.
npm run checktype

# If intending to build and get all types of the "production" files:
npm run release
```

Then the "production" files are generated in the `dist` directory.

## Contribution

Please refer to the [contributing](https://github.com/apache/echarts/blob/master/CONTRIBUTING.md) document if you wish to debug locally or make pull requests.

## Resources

### Awesome ECharts

[https://github.com/ecomfe/awesome-echarts](https://github.com/ecomfe/awesome-echarts)

### Extensions

+ [ECharts GL](https://github.com/ecomfe/echarts-gl) An extension pack of ECharts, which provides 3D plots, globe visualization, and WebGL acceleration.

+ [Liquidfill 水球图](https://github.com/ecomfe/echarts-liquidfill)

+ [Wordcloud 字符云](https://github.com/ecomfe/echarts-wordcloud)

+ [Extension for Baidu Map 百度地图扩展](https://github.com/apache/echarts/tree/master/extension-src/bmap) An extension provides a wrapper of Baidu Map Service SDK.

+ [vue-echarts](https://github.com/ecomfe/vue-echarts) ECharts component for Vue.js

+ [echarts-stat](https://github.com/ecomfe/echarts-stat) Statistics tool for ECharts

## License

ECharts is available under the Apache License V2.

## Code of Conduct

Please refer to [Apache Code of Conduct](https://www.apache.org/foundation/policies/conduct.html).

## Paper

Deqing Li, Honghui Mei, Yi Shen, Shuang Su, Wenli Zhang, Junting Wang, Ming Zu, Wei Chen.
[ECharts: A Declarative Framework for Rapid Construction of Web-based Visualization](https://www.sciencedirect.com/science/article/pii/S2468502X18300068).
Visual Informatics, 2018.
