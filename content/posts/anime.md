---
title: anime
date: 2025-04-09T12:22:23+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1742302954292-1f903368084e?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDQxNzI0NTB8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1742302954292-1f903368084e?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDQxNzI0NTB8&ixlib=rb-4.0.3
---

# [juliangarnier/anime](https://github.com/juliangarnier/anime)

# Anime.js

<p align="center">
  <picture align="center">
    <source media="(prefers-color-scheme: dark)" srcset="./assets/images/animejs-v4-logo-animation-dark.gif">
    <img align="center" alt="Anime.js V4 logo animation" src="./assets/images/animejs-v4-logo-animation.gif" width="560">
  </picture>
</p>

<p align="center">
  <strong>
  <em>Anime.js</em> is a fast, multipurpose and lightweight JavaScript animation library with a simple, yet powerful API.<br>
  It works with CSS properties, SVG, DOM attributes and JavaScript Objects.
  </strong>
</p>

<p align="center">
  <img alt="NPM Downloads" src="https://img.shields.io/npm/dm/animejs?style=flat-square&logo=npm">
  <img alt="jsDelivr hits (npm)" src="https://img.shields.io/jsdelivr/npm/hm/animejs?style=flat-square&logo=jsdeliver">
  <img alt="GitHub Sponsors" src="https://img.shields.io/github/sponsors/juliangarnier?style=flat-square&logo=github">
</p>

## Usage

Anime.js V4 works by importing ES modules like so:

<table>
<tr>
  <td>

```javascript
import {
  animate,
  stagger,
} from 'animejs';

animate('.square', {
  x: 320,
  rotate: { from: -180 },
  duration: 1250,
  delay: stagger(65, { from: 'center' }),
  ease: 'inOutQuint',
  loop: true,
  alternate: true
});
```

  </td>
  <td>
    <img align="center" alt="Anime.js code example" src="./assets/images/usage-example-result.gif">
  </td>
</tr>
</table>

## V4 Documentation

The full documentation is available [here](https://animejs.com/documentation).

## Our sponsors

Anime.js is 100% free and is only made possible with the help of our sponsors.
Help the project become sustainable by sponsoring us on <a target="_blank" href="https://github.com/sponsors/juliangarnier">GitHub Sponsors</a>.

## Platinum sponsors

<table>
  <tr>
    <td>
      <a target="_blank" href="https://huly.io/?ref=animejs">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="./assets/sponsors/huly-logomark.svg">
          <img align="center" src="./assets/sponsors/huly-logomark-dark.svg" width="128">
        </picture>
      </a>
    </td>
    <td>
      <a target="_blank" href="https://ice.io/?ref=animejs">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="./assets/sponsors/ice-open-network-logomark.svg">
          <img align="center" src="./assets/sponsors/ice-open-network-logomark-dark.svg" width="128">
        </picture>
      </a>
    </td>
    <td>
      <a target="_blank" href="https://github.com/sponsors/juliangarnier">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="./assets/sponsors/placeholder.svg">
          <img align="center" src="./assets/sponsors/placeholder-dark.svg" width="128">
        </picture>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a target="_blank" href="https://huly.io/?ref=animejs">Huly</a>
    </td>
    <td align="center">
      <a target="_blank" href="https://ice.io/?ref=animejs">Ice Open Network</a>
    </td>
    <td align="center">
      <a target="_blank" href="https://github.com/sponsors/juliangarnier">Your logo here</a>
    </td>
  </tr>
</table>

## NPM development scripts

First, run `npm i` to install all the necessary packages.
Then, execute the following scripts with `npm run <script>`.

| script | action |
| ------ | ------ |
| `dev` | Watch any changes in `src/` and compiles the esm version to `lib/anime.esm.js` |
| `dev-types` | Same as `dev`, but also run TypeScript and generate the `types/index.d.ts` file |
| `build` | Generate types definition and compiles ESM / UMD / IIFE versions to `lib/` |
| `test-browser` | Start a local server and start all browser related tests |
| `test-node` | Start all Node related tests |
| `open-examples` | Start a local server to browse the examples locally |

## V4 API breaking changes overview

### Animations

```diff
- import anime from 'animejs';
+ import { animate, createSpring, utils } from 'animejs';

- anime({
-   targets: 'div',
+ animate('div', {
    translateX: 100,
      rotate: {
-     value: 360,
+     to: 360,
-     easing: 'spring(.7, 80, 10, .5)',
+     ease: createSpring({ mass: .7, damping: 80, stiffness: 10, velocity: .5}),
    },
-   easing: 'easeinOutExpo',
+   ease: 'inOutExpo',
-   easing: () => t => Math.cos(t),
+   ease: t => Math.cos(t),
-   direction: 'reverse',
+   reversed: true,
-   direction: 'alternate',
+   alternate: true,
-   loop: 1,
+   loop: 0,
-   round: 100,
+   modifier: utils.round(2),
-   begin: () => {},
+   onBegin: () => {},
-   update: () => {},
+   onUpdate: () => {},
-   change: () => {},
+   onRender: () => {},
-   changeBegin: () => {},
-   changeComplete: () => {},
-   loopBegin: () => {},
-   loopComplete: () => {},
+   onLoop: () => {},
-   complete: () => {},
+   onComplete: () => {},
  });
```

### Promises

```diff
- import anime from 'animejs';
+ import { animate, utils } from 'animejs';

- anime({ targets: target, prop: x }).finished.then(() => {});
+ animate(target, { prop: x }).then(() => {});
```

### Timers

```diff
- import anime from 'animejs';
+ import { createTimer } from 'animejs';

- anime({
+ createTimer({
-   duration: Infinity,
-   update: () => {},
+   onUpdate: () => {},
  });
```

### Timelines

```diff
- import anime from 'animejs';
+ import { createTimeline, stagger } from 'animejs';

- anime.timeline({
+ createTimeline({
-   duration: 500,
-   easing: 'easeInOutQuad',
+   defaults: {
+     duration: 500,
+     ease: 'inOutQuad',
+   }
-   loop: 2,
+   loop: 1,
- }).add({
-   targets: 'div',
+ }).add('div', {
    rotate: 90,
  })
- .add('.target:nth-child(1)', { opacity: 0, onComplete }, 0)
- .add('.target:nth-child(2)', { opacity: 0, onComplete }, 100)
- .add('.target:nth-child(3)', { opacity: 0, onComplete }, 200)
- .add('.target:nth-child(4)', { opacity: 0, onComplete }, 300)
+ .add('.target', { opacity: 0, onComplete }, stagger(100))
```

### Stagger

```diff
- import anime from 'animejs';
+ import { animate, stagger } from 'animejs';

- anime({
-   targets: 'div',
+ animate('div', {
-   translateX: anime.stagger(100),
+   translateX: stagger(100),
-   delay: anime.stagger(100, { direction: 'reversed' }),
+   translateX: stagger(100, { reversed: true }),
  });
```

### SVG

```diff
- import anime from 'animejs';
+ import { animate, svg } from 'animejs';

- const path = anime.path('path');
+ const { x, y, angle } = svg.createMotionPath('path');

- anime({
-   targets: '#shape1',
+ animate('#shape1', {
-   points: '70 41 118.574 59.369 111.145 132.631 60.855 84.631 20.426 60.369',
+   points: svg.morphTo('#shape2'),
-   strokeDashoffset: [anime.setDashoffset, 0],
+   strokeDashoffset: svg.drawLine(),
-   translateX: path('x'),
-   translateY: path('y'),
-   rotate: path('angle'),
+   translateX: x,
+   translateY: y,
+   rotate: angle,
  });
```

### Utils

```diff
- import anime from 'animejs';
+ import { utils } from 'animejs';

- const value = anime.get('#target1', 'translateX');
+ const value = utils.get('#target1', 'translateX');

- anime.set('#target1', { translateX: 100 });
+ utils.set('#target1', { translateX: 100 });

- anime.remove('#target1');
+ utils.remove('#target1');

- const rounded = anime.round(value);
+ const rounded = utils.round(value, 0);
```

### Engine

```diff
- import anime from 'animejs';
+ import { engine } from 'animejs';

- anime.suspendWhenDocumentHidden = false;
+ engine.pauseWhenHidden = false;

- anime.speed = .5;
+ engine.playbackRate = .5;
```