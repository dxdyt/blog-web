---
title: mesh2motion-app
date: 2025-08-25T12:26:13+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1755311901131-c0b8f91a21c0?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTYwOTU5NDZ8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1755311901131-c0b8f91a21c0?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTYwOTU5NDZ8&ixlib=rb-4.1.0
---

# [scottpetrovic/mesh2motion-app](https://github.com/scottpetrovic/mesh2motion-app)

<img src="./mesh2motion.svg" alt="Mesh2Motion Logo" width="400"/>

Import a 3D Model and automatically assign and export animations with Mesh2Motion. This is kind of similar to a web application like Mixamo, but I would like it to be more flexible so it can support other model and skeleton types. Hopefully the open source nature means it can be expanded on and evolve more than than the closed tools have. 

The marketing site that explains features and release notes: https://mesh2motion.org/

Try it live: https://app.mesh2motion.org/

![Screenshot](./readme.png)

## Usage
There are instructions built into the web application, but this is the general flow of how to use it:
1. Import a 3d model of your choosing (currently only supports GLB/GLTF format)
2. Pick what type of skeleton that the 3d model will use
3. Modify the skeleton to fit inside of the model (optionally test the results)
4. Test out various animations to see the results.
5. Select which animations you want to use, then export (currently only GLB/GLTF supported format)

## Building and running locally
The main dependency you need is Node.js. I am using 18.15, but other versions probably work fine too. Open you command line tool to the directory this readme is in. Run ths following commands to start the web server.

    npm install
    npm run dev

## Creating a production build for the web
We mostly just have typescript for this project, which web browsers cannot just read, so we need to do a build step to get everything ready for deploying. This project uses Vite for the web server and builder. See the vite.config.js for more info. This command will create a "dist" folder with all the files to serve to the web:

    npm run build

## Running in Docker
If you don't want to modify your local file system, you can alternitvely build and run the project from Docker. Make sure you have Docker and Docker Compose installed. Navigate your command line tool to this directory where your Dockerfile is at. Make sure Docker is actually started and running before you run this command.

Execute the following command.

    docker-compose up -d

To try it out, visit http://localhost:3000

## Running and creating video previews
There is separate tool in the web app where you can generate video previews for each animation. It isn't too hard to run, but it has a separate README file that explains how that works. It is more of an internal tool, so I didn't want to muddy up this page too much.

[Preview Generator Documentation](src/preview-generator/README.md)

## Animator Guide
Are you an animator who wants to help build out animations for this tool? This is by far my weakest skill, which is why I have been avoiding it. In the **static > blender** folder, you can see all the source Blender files where I have been working. There are a couple of model files where I just have the model, and other files that actually contain the animations. These are the files we can build animations into.

🦊 fox.blend (animations for the quadruped character)

🫡 human.blend (animations for the humanoid character)

🐦‍⬛ bird.blend (animations for the bird character)

When new animations are added, I export everything to GLB and save the file in the **static > animation** folder. Just overwrite the file that correlates. For the human animations, use the "addon" GLB file since these are being appended to the Quaternius ones. The Mixamo one is unused right now. Just a reference if I were to later add some type of support.

If you come up with anything, just get me the source .blend file and let me know what you changed. I can export it out to GLB and rebuild the animation previews.

## Contribute to the animation fund
I don't expect to be receiving money for working on this, but I am also not the best animator. If people want to see better, and more, animations made, add to the fund. I can pay for an animator to help build out the animation library better. Or, if you know an animator that wants to help with this, send them my way! I am just a dude working on this during nights and weekends.

<img src="./venmo.png" alt="Venmo Animator Fund" width="400"/>









