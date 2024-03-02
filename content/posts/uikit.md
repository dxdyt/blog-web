---
title: uikit
date: 2024-03-02T12:15:11+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1707730376818-a7a02fe896d5?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDkzNTI4Njh8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1707730376818-a7a02fe896d5?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MDkzNTI4Njh8&ixlib=rb-4.0.3
---

# [pmndrs/uikit](https://github.com/pmndrs/uikit)

<h1>@react-three/uikit</h1>

Build performant 3D user interfaces for Three.js using @react-three/fiber and yoga

# Changes over Koestlich

- higher performance (GPU + CPU)
- no suspense (similarly to html/css images and texts don't suspend)
- objects are nested for correct event propagation
- no default animations
- complete freedom to use R3F inside of UI => <Content>...</Content>
- better scroll experiences (scrollbar + overscroll)
- overall DX improvements (hover, responsive, ...)

TODO Release

- fix: changing font weight with hot reload (test if its the same for normal react state change)
- fix: conditionally render children (see Discord)
- feat: ref.current.setStyle({ ... })
- feat: nesting inside non root/container components (e.g. image)
- fix: scrollbar border radius to high (happens with very long panels)
- feat: drag/click threshold
- feat: add apfel components
- feat: input
- fix: decrease clipping rect when scrollbar present

Roadmap

- on demand rendering to save battery for UI only apps / rendering to render targets
- upgrade to yoga2.0
- virtual lists (support thousands of elements in a list by using fixed sizes and not using yoga)
- option to render to seperate render targets depending on element type (e.g. render text to high quality quad layer for WebXR)
- scrollIntoView
- Instancing for icons
- Support more characters for different languages
- Support for visibility="hidden" & display="none"

Limitations

- nested clipping with rotation in z-axis (the clipping area can become more complex than a rectangle)

## Development

`pnpm install`  
`pnpm -r inline-wasm`  
`pnpm -r convert`  
`pnpm -r generate`  
`pnpm -r build`  

go to `examples/market` and run `pnpm dev` to view the example dashboard
