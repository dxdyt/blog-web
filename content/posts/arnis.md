---
title: arnis
date: 2025-01-06T12:20:57+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1733653023250-33739d0d8dc4?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzYxMzcxOTF8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1733653023250-33739d0d8dc4?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzYxMzcxOTF8&ixlib=rb-4.0.3
---

# [louis-e/arnis](https://github.com/louis-e/arnis)

<p align="center">
  <img width="456" height="125" src="https://github.com/louis-e/arnis/blob/main/gitassets/logo.png?raw=true">
</p>

# Arnis [![CI Build Status](https://github.com/louis-e/arnis/actions/workflows/ci-build.yml/badge.svg)](https://github.com/louis-e/arnis/actions) [<img alt="GitHub Release" src="https://img.shields.io/github/v/release/louis-e/arnis" />](https://github.com/louis-e/arnis/releases) [<img alt="GitHub Downloads (all assets, all releases" src="https://img.shields.io/github/downloads/louis-e/arnis/total" />](https://github.com/louis-e/arnis/releases)

This open source project written in Rust generates any chosen location from the real world in Minecraft Java Edition with a high level of detail.

## :desktop_computer: Example
![Minecraft Preview](https://github.com/louis-e/arnis/blob/main/gitassets/mc.gif?raw=true)

By leveraging geospatial data from OpenStreetMap and utilizing the powerful capabilities of Rust, Arnis provides an efficient and robust solution for creating complex and accurate Minecraft worlds that reflect real-world geography and architecture.

Arnis is designed to handle large-scale data and generate rich, immersive environments that bring real-world cities, landmarks, and natural features into the Minecraft universe. Whether you're looking to replicate your hometown, explore urban environments, or simply build something unique and realistic, Arnis generates your vision.

**This is the official project website. Any other website pretending to be associated with Arnis is fake and should be avoided.**

## :keyboard: Usage
<img width="60%" src="https://github.com/louis-e/arnis/blob/main/gitassets/gui.png?raw=true"><br>
Download the [latest release](https://github.com/louis-e/arnis/releases/) or [compile](#trophy-open-source) the project on your own.
 
Choose your area in Arnis using the rectangle tool and select your Minecraft world - then simply click on 'Start Generation'!
The world will always be generated starting from the Minecraft coordinates 0 0 0 (/tp 0 0 0). This is the top left of your selected area.

If you choose to select an own world, make sure to generate a new flat world in advance in Minecraft.

Minecraft version 1.16.5 and below is currently not supported, but we are working on it! For the best results, use Minecraft version 1.21.4.

## :floppy_disk: How it works
![CLI Generation](https://github.com/louis-e/arnis/blob/main/gitassets/cli.gif?raw=true)

The raw data obtained from the API *[(see FAQ)](#question-faq)* includes each element (buildings, walls, fountains, farmlands, etc.) with its respective corner coordinates (nodes) and descriptive tags. When you run Arnis, the following steps are performed automatically to generate a Minecraft world:

#### Processing Pipeline
1. **Fetching Data from the Overpass API:** The script retrieves geospatial data for the desired bounding box from the Overpass API.
2. **Parsing Raw Data:** The raw data is parsed to extract essential information like nodes, ways, and relations. Nodes are converted into Minecraft coordinates, and relations are handled similarly to ways, ensuring all relevant elements are processed correctly. Relations and ways cluster several nodes into one specific object.
3. **Prioritizing and Sorting Elements:** The elements (nodes, ways, relations) are sorted by priority to establish a layering system, which ensures that certain types of elements (e.g., entrances and buildings) are generated in the correct order to avoid conflicts and overlapping structures.
4. **Generating Minecraft World:** The Minecraft world is generated using a series of element processors (generate_buildings, generate_highways, generate_landuse, etc.) that interpret the tags and nodes of each element to place the appropriate blocks in the Minecraft world. These processors handle the logic for creating 3D structures, roads, natural formations, and more, as specified by the processed data.
5. **Generating Ground Layer:** A ground layer is generated based on the provided scale factors to provide a base for the entire Minecraft world. This step ensures all areas have an appropriate foundation (e.g., grass and dirt layers).
6. **Saving the Minecraft World:** All the modified chunks are saved back to the Minecraft region files.

## :question: FAQ
- *Wasn't this written in Python before?*<br>
Yes! Arnis was initially developed in Python, which benefited from Python's open-source friendliness and ease of readability. This is why we strive for clear, well-documented code in the Rust port of this project to find the right balance. I decided to port the project to Rust to learn more about the language and push the algorithm's performance further. We were nearing the limits of optimization in Python, and Rust's capabilities allow for even better performance and efficiency. The old Python implementation is still available in the python-legacy branch.
- *Where does the data come from?*<br>
The geographic data is sourced from OpenStreetMap (OSM)[^1], a free, collaborative mapping project that serves as an open-source alternative to commercial mapping services. The data is accessed via the Overpass API, which queries OSM's database.
- *How does the Minecraft world generation work?*<br>
The script uses the [fastnbt](https://github.com/owengage/fastnbt) cargo package to interact with Minecraft's world format. This library allows Arnis to manipulate Minecraft region files, enabling the generation of real-world locations. The section 'Processing Pipeline' goes a bit further into the details and steps of the generation process itself.
- *Where does the name come from?*<br>
The project is named after the smallest city in Germany, Arnis[^2]. The city's small size made it an ideal test case for developing and debugging the algorithm efficiently.
- *I don't have Minecraft installed but want to generate a world for my kids. How?*<br>
When selecting a world, click on 'Select existing world' and choose a directory. The world will be generated there.
- *Arnis instantly closes again or the window is empty!*<br>
If you're on Windows, please install the [Evergreen Bootstrapper from Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/webview2/?form=MA13LH#download).
- *What Minecraft version should I use?*<br>
Please use Minecraft version 1.21.4 for the best results. Minecraft version 1.16.5 and below is currently not supported, but we are working on it!
- *The generation did finish, but there's nothing in the world!*<br>
Make sure to teleport to the generation starting point (/tp 0 0 0). If there is still nothing, you might need to travel a bit further into the positive X and positive Z direction.

## :memo: ToDo and Known Bugs
Feel free to choose an item from the To-Do or Known Bugs list, or bring your own idea to the table. Bug reports shall be raised as a Github issue. Contributions are highly welcome and appreciated!
- [ ] Fix compilation for Linux
- [ ] Rotate maps (https://github.com/louis-e/arnis/issues/97)
- [ ] Add street names as signs
- [ ] Add support for older Minecraft versions (<=1.16.5) (https://github.com/louis-e/arnis/issues/124, https://github.com/louis-e/arnis/issues/137)
- [ ] Mapping real coordinates to Minecraft coordinates (https://github.com/louis-e/arnis/issues/29)
- [ ] Add interior to buildings
- [ ] Implement house roof types
- [ ] Evaluate and implement elevation (https://github.com/louis-e/arnis/issues/66)
- [ ] Add support for inner attribute in multipolygons and multipolygon elements other than buildings
- [ ] Fix Github Action Workflow for releasing Linux & MacOS Binary
- [ ] Evaluate and implement faster region saving
- [ ] Refactor bridges implementation
- [ ] Refactor railway implementation
- [ ] Better code documentation
- [ ] Refactor fountain structure implementation
- [ ] Luanti Support (https://github.com/louis-e/arnis/issues/120)
- [ ] Minecraft Bedrock Edition Support (https://github.com/louis-e/arnis/issues/148)
- [x] Support multipolygons (https://github.com/louis-e/arnis/issues/112, https://github.com/louis-e/arnis/issues/114)
- [x] Memory optimization
- [x] Design and implement a GUI
- [x] Automatic new world creation instead of using an existing world
- [x] Fix faulty empty chunks ([https://github.com/owengage/fastnbt/issues/120](https://github.com/owengage/fastnbt/issues/120)) (workaround found)
- [x] Setup fork of [https://github.com/aaronr/bboxfinder.com](https://github.com/aaronr/bboxfinder.com) for easy bbox picking

## :trophy: Open Source
#### Key objectives of this project
- **Modularity**: Ensure that all components (e.g., data fetching, processing, and world generation) are cleanly separated into distinct modules for better maintainability and scalability.
- **Performance Optimization**: Utilize Rust’s memory safety and concurrency features to optimize the performance of the world generation process.
- **Comprehensive Documentation**: Detailed in-code documentation for a clear structure and logic.
- **User-Friendly Experience**: Focus on making the project easy to use for end users.
- **Cross-Platform Support**: Ensure the project runs smoothly on Windows, macOS, and Linux.

#### How to contribute
This project is open source and welcomes contributions from everyone! Whether you're interested in fixing bugs, improving performance, adding new features, or enhancing documentation, your input is valuable. Simply fork the repository, make your changes, and submit a pull request. We encourage discussions and suggestions to ensure the project remains modular, optimized, and easy to use for the community. You can use the parameter --debug to get a more detailed output of the processed values, which can be helpful for debugging and development. Contributions of all levels are appreciated, and your efforts help improve this tool for everyone.

Build and run it using: ```cargo run --release -- --path="C:/YOUR_PATH/.minecraft/saves/worldname" --bbox="min_lng,min_lat,max_lng,max_lat"```<br>
For the GUI: ```cargo run --release```<br>

After your pull request was merged, I will take care of regularly creating update releases which will include your changes.

## :star: Star History

<a href="https://star-history.com/#louis-e/arnis&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=louis-e/arnis&Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=louis-e/arnis&Date&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=louis-e/arnis&Date&type=Date" />
 </picture>
</a>

## :copyright: License Information
This project is licensed under the GNU General Public License v3.0 (GPL-3.0).[^3]

Copyright (c) 2022-2025 Louis Erbkamm (louis-e)

[^1]: https://en.wikipedia.org/wiki/OpenStreetMap

[^2]: https://en.wikipedia.org/wiki/Arnis,_Germany

[^3]:
    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
    For the full license text, see the LICENSE file.
