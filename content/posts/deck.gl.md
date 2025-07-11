---
title: deck.gl
date: 2025-07-01T12:38:55+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1743805350606-56ed5103769c?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTEzNDQ2MTd8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1743805350606-56ed5103769c?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTEzNDQ2MTd8&ixlib=rb-4.1.0
---

# [visgl/deck.gl](https://github.com/visgl/deck.gl)

<p align="right">
  <a href="https://npmjs.org/package/deck.gl">
    <img src="https://img.shields.io/npm/v/deck.gl.svg?style=flat-square" alt="version" />
  </a>
  <a href="https://github.com/visgl/deck.gl/actions?query=workflow%3Atest+branch%3Amaster">
    <img src="https://github.com/visgl/deck.gl/workflows/test/badge.svg?branch=master" alt="build" />
  </a>
  <a href="https://npmjs.org/package/deck.gl">
    <img src="https://img.shields.io/npm/dm/@deck.gl/core.svg?style=flat-square" alt="downloads" />
  </a>
  <a href='https://coveralls.io/github/visgl/deck.gl?branch=master'>
    <img src='https://img.shields.io/coveralls/visgl/deck.gl.svg?style=flat-square' alt='Coverage Status' />
  </a>
</p>

<h1 align="center">deck.gl | <a href="https://deck.gl">Website</a></h1>

<h5 align="center"> GPU-powered, highly performant large-scale data visualization</h5>

[![docs](http://i.imgur.com/mvfvgf0.jpg)](https://visgl.github.io/deck.gl)


deck.gl is designed to simplify high-performance, WebGL2/WebGPU based visualization of large data sets. Users can quickly get impressive visual results with minimal effort by composing existing layers, or leverage deck.gl's extensible architecture to address custom needs.

deck.gl maps **data** (usually an array of JSON objects) into a stack of visual **layers** - e.g. icons, polygons, texts; and look at them with **views**: e.g. map, first-person, orthographic.

deck.gl handles a number of challenges out of the box:

* Performant rendering and updating of large data sets
* Interactive event handling such as picking, highlighting and filtering
* Cartographic projections and integration with major basemap providers
* A catalog of proven, well-tested layers

Deck.gl is designed to be highly customizable. All layers come with flexible APIs to allow programmatic control of each aspect of the rendering. All core classes such are easily extendable by the users to address custom use cases.

## Flavors

### Script Tag

```html
<script src="https://unpkg.com/deck.gl@latest/dist.min.js"></script>
```

- [Get started](/docs/get-started/using-standalone.md#using-the-scripting-api)
- [Full examples](https://github.com/visgl/deck.gl/tree/master/examples/get-started/scripting)

### NPM Module

```bash
npm install deck.gl
```

#### Pure JS

- [Get started](/docs/get-started/using-standalone.md)
- [Full examples](/examples/get-started/pure-js)

#### React

- [Get started](/docs/get-started/using-with-react.md)
- [Full examples](/examples/get-started/react)

### Python

```bash
pip install pydeck
```

- [Get started](https://deckgl.readthedocs.io/en/latest/installation.html)
- [Examples](https://deckgl.readthedocs.io/en/latest/layer.html)

### Third-Party Goodies

- [deckgl-typings](https://github.com/danmarshall/deckgl-typings) (Typescript)
- [mapdeck](https://symbolixau.github.io/mapdeck/articles/mapdeck.html) (R)
- [vega-deck.gl](https://github.com/microsoft/SandDance/tree/master/packages/vega-deck.gl) ([Vega](https://vega.github.io/))
- [earthengine-layers](https://earthengine-layers.com/) ([Google Earth Engine](https://earthengine.google.com/))
- [deck.gl-native](https://github.com/UnfoldedInc/deck.gl-native) (C++)
- [deck.gl-raster](https://github.com/kylebarron/deck.gl-raster/) (Computation on rasters)

## Learning Resources

* [API documentation](https://deck.gl/docs) for the latest release
* [Website demos](https://deck.gl/examples) with links to source
* [Interactive playground](https://deck.gl/playground)
* [deck.gl Codepen demos](https://codepen.io/vis-gl/)
* [deck.gl Observable demos](https://beta.observablehq.com/@pessimistress)
* [vis.gl Medium blog](https://medium.com/vis-gl)
* [deck.gl Slack workspace](https://slack-invite.openjsf.org/)

## Contributing

deck.gl is part of vis.gl, an [OpenJS Foundation](https://openjsf.org/) project. Read the [contribution guidelines](/CONTRIBUTING.md) if you are interested in contributing.


## Attributions

#### Data sources

Data sources are listed in each example.


#### The deck.gl project is supported by

<a href="https://www.unfolded.ai"><img src="https://raw.githubusercontent.com/visgl/deck.gl-data/master/images/branding/unfolded.png" height="32" /></a>
<a href="https://www.foursquare.com"><img src="https://raw.githubusercontent.com/visgl/deck.gl-data/master/images/branding/fsq.svg" height="40" /></a>

<a href="https://www.carto.com"><img src="https://raw.githubusercontent.com/visgl/deck.gl-data/master/images/branding/carto.svg" height="48" /></a>

<a href="https://www.mapbox.com"><img src="https://raw.githubusercontent.com/visgl/deck.gl-data/master/images/branding/mapbox.svg" height="44" /></a>
<a href="https://www.uber.com"><img src="https://raw.githubusercontent.com/visgl/deck.gl-data/master/images/branding/uber.png" height="40" /></a>

<a href="https://www.browserstack.com/"><img src="https://d98b8t1nnulk5.cloudfront.net/production/images/static/logo.svg" alt="BrowserStack" width="200" /></a>
