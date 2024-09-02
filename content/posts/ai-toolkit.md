---
title: ai-toolkit
date: 2024-08-17T12:20:06+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1723391962154-8a2b6299bc09?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MjM4NjgzNDN8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1723391962154-8a2b6299bc09?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MjM4NjgzNDN8&ixlib=rb-4.0.3
---

# [ostris/ai-toolkit](https://github.com/ostris/ai-toolkit)

# AI Toolkit by Ostris

## IMPORTANT NOTE - READ THIS
This is my research repo. I do a lot of experiments in it and it is possible that I will break things.
If something breaks, checkout an earlier commit. This repo can train a lot of things, and it is
hard to keep up with all of them.

## Support my work

<a href="https://glif.app" target="_blank">
<img alt="glif.app" src="https://raw.githubusercontent.com/ostris/ai-toolkit/main/assets/glif.svg?v=1" width="256" height="auto">
</a>


My work on this project would not be possible without the amazing support of [Glif](https://glif.app/) and everyone on the 
team. If you want to support me, support Glif. [Join the site](https://glif.app/), 
[Join us on Discord](https://discord.com/invite/nuR9zZ2nsh), [follow us on Twitter](https://x.com/heyglif)
and come make some cool stuff with us

## Installation

Requirements:
- python >3.10
- Nvidia GPU with enough ram to do what you need
- python venv
- git



Linux:
```bash
git clone https://github.com/ostris/ai-toolkit.git
cd ai-toolkit
git submodule update --init --recursive
python3 -m venv venv
source venv/bin/activate
# .\venv\Scripts\activate on windows
# install torch first
pip3 install torch
pip3 install -r requirements.txt
```

Windows:
```bash
git clone https://github.com/ostris/ai-toolkit.git
cd ai-toolkit
git submodule update --init --recursive
python -m venv venv
.\venv\Scripts\activate
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

## FLUX.1 Training

### WIP. I am updating docs and optimizing as fast as I can. If there are bugs open a ticket. Not knowing how to get it to work is NOT a bug. Be paitient as I continue to develop it.


### Requirements
You currently need a GPU with **at least 24GB of VRAM** to train FLUX.1. If you are using it as your GPU to control 
your monitors, you probably need to set the flag `low_vram: true` in the config file under `model:`. This will quantize
the model on CPU and should allow it to train with monitors attached. Users have gotten it to work on Windows with WSL,
but there are some reports of a bug when running on windows natively. 
I have only tested on linux for now. This is still extremely experimental
and a lot of quantizing and tricks had to happen to get it to fit on 24GB at all. 

### Model License

Training currently only works with FLUX.1-dev. Which means anything you train will inherit the
non-commercial license. It is also a gated model, so you need to accept the license on HF before using it.
Otherwise, this will fail. Here are the required steps to setup a license.

1. Sign into HF and accept the model access here [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)
2. Make a file named `.env` in the root on this folder
3. [Get a READ key from huggingface](https://huggingface.co/settings/tokens/new?) and add it to the `.env` file like so `HF_TOKEN=your_key_here`

### Training
1. Copy the example config file located at `config/examples/train_lora_flux_24gb.yaml` to the `config` folder and rename it to `whatever_you_want.yml`
2. Edit the file following the comments in the file
3. Run the file like so `python3 run.py config/whatever_you_want.yml`

A folder with the name and the training folder from the config file will be created when you start. It will have all 
checkpoints and images in it. You can stop the training at any time using ctrl+c and when you resume, it will pick back up
from the last checkpoint.

IMPORTANT. If you press crtl+c while it is saving, it will likely corrupt that checkpoint. So wait until it is done saving

### Need help?

Please do not open a bug report unless it is a bug in the code. You are welcome to [Join my Discord](https://discord.gg/SzVB3wYvxF)
and ask for help there. However, please refrain from PMing me directly with general question or support. Ask in the discord
and I will answer when I can.

### Training in the cloud
Coming very soon. Getting base out then will have a notebook that makes all that work. 

---

## Dataset Preparation

Datasets generally need to be a folder containing images and associated text files. Currently, the only supported
formats are jpg, jpeg, and png. Webp currently has issues. The text files should be named the same as the images
but with a `.txt` extension. For example `image2.jpg` and `image2.txt`. The text file should contain only the caption.
You can add the word `[trigger]` in the caption file and if you have `trigger_word` in your config, it will be automatically
replaced. 

Images are never upscaled but they are downscaled and placed in buckets for batching. **You do not need to crop/resize your images**.
The loader will automatically resize them and can handle varying aspect ratios. 

---

## EVERYTHING BELOW THIS LINE IS OUTDATED 

It may still work like that, but I have not tested it in a while.

---

### Batch Image Generation

A image generator that can take frompts from a config file or form a txt file and generate them to a 
folder. I mainly needed this for an SDXL test I am doing but added some polish to it so it can be used
for generat batch image generation.
It all runs off a config file, which you can find an example of in  `config/examples/generate.example.yaml`.
Mere info is in the comments in the example

---

### LoRA (lierla), LoCON (LyCORIS) extractor

It is based on the extractor in the [LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS) tool, but adding some QOL features
and LoRA (lierla) support. It can do multiple types of extractions in one run.
It all runs off a config file, which you can find an example of in  `config/examples/extract.example.yml`.
Just copy that file, into the `config` folder, and rename it to `whatever_you_want.yml`.
Then you can edit the file to your liking. and call it like so:

```bash
python3 run.py config/whatever_you_want.yml
```

You can also put a full path to a config file, if you want to keep it somewhere else.

```bash
python3 run.py "/home/user/whatever_you_want.yml"
```

More notes on how it works are available in the example config file itself. LoRA and LoCON both support
extractions of 'fixed', 'threshold', 'ratio', 'quantile'. I'll update what these do and mean later.
Most people used fixed, which is traditional fixed dimension extraction.

`process` is an array of different processes to run. You can add a few and mix and match. One LoRA, one LyCON, etc.

---

### LoRA Rescale

Change `<lora:my_lora:4.6>` to `<lora:my_lora:1.0>` or whatever you want with the same effect. 
A tool for rescaling a LoRA's weights. Should would with LoCON as well, but I have not tested it.
It all runs off a config file, which you can find an example of in  `config/examples/mod_lora_scale.yml`.
Just copy that file, into the `config` folder, and rename it to `whatever_you_want.yml`.
Then you can edit the file to your liking. and call it like so:

```bash
python3 run.py config/whatever_you_want.yml
```

You can also put a full path to a config file, if you want to keep it somewhere else.

```bash
python3 run.py "/home/user/whatever_you_want.yml"
```

More notes on how it works are available in the example config file itself. This is useful when making 
all LoRAs, as the ideal weight is rarely 1.0, but now you can fix that. For sliders, they can have weird scales form -2 to 2
or even -15 to 15. This will allow you to dile it in so they all have your desired scale

---

### LoRA Slider Trainer

<a target="_blank" href="https://colab.research.google.com/github/ostris/ai-toolkit/blob/main/notebooks/SliderTraining.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

This is how I train most of the recent sliders I have on Civitai, you can check them out in my [Civitai profile](https://civitai.com/user/Ostris/models).
It is based off the work by [p1atdev/LECO](https://github.com/p1atdev/LECO) and [rohitgandikota/erasing](https://github.com/rohitgandikota/erasing)
But has been heavily modified to create sliders rather than erasing concepts. I have a lot more plans on this, but it is
very functional as is. It is also very easy to use. Just copy the example config file in `config/examples/train_slider.example.yml`
to the `config` folder and rename it to `whatever_you_want.yml`. Then you can edit the file to your liking. and call it like so:

```bash
python3 run.py config/whatever_you_want.yml
```

There is a lot more information in that example file. You can even run the example as is without any modifications to see
how it works. It will create a slider that turns all animals into dogs(neg) or cats(pos). Just run it like so:

```bash
python3 run.py config/examples/train_slider.example.yml
```

And you will be able to see how it works without configuring anything. No datasets are required for this method.
I will post an better tutorial soon. 

---

## Extensions!!

You can now make and share custom extensions. That run within this framework and have all the inbuilt tools
available to them. I will probably use this as the primary development method going
forward so I dont keep adding and adding more and more features to this base repo. I will likely migrate a lot
of the existing functionality as well to make everything modular. There is an example extension in the `extensions`
folder that shows how to make a model merger extension. All of the code is heavily documented which is hopefully
enough to get you started. To make an extension, just copy that example and replace all the things you need to.


### Model Merger - Example Extension
It is located in the `extensions` folder. It is a fully finctional model merger that can merge as many models together
as you want. It is a good example of how to make an extension, but is also a pretty useful feature as well since most
mergers can only do one model at a time and this one will take as many as you want to feed it. There is an 
example config file in there, just copy that to your `config` folder and rename it to `whatever_you_want.yml`.
and use it like any other config file.

## WIP Tools


### VAE (Variational Auto Encoder) Trainer

This works, but is not ready for others to use and therefore does not have an example config. 
I am still working on it. I will update this when it is ready.
I am adding a lot of features for criteria that I have used in my image enlargement work. A Critic (discriminator),
content loss, style loss, and a few more. If you don't know, the VAE
for stable diffusion (yes even the MSE one, and SDXL), are horrible at smaller faces and it holds SD back. I will fix this.
I'll post more about this later with better examples later, but here is a quick test of a run through with various VAEs.
Just went in and out. It is much worse on smaller faces than shown here.

<img src="https://raw.githubusercontent.com/ostris/ai-toolkit/main/assets/VAE_test1.jpg" width="768" height="auto"> 

---

## TODO
- [X] Add proper regs on sliders
- [X] Add SDXL support (base model only for now)
- [ ] Add plain erasing
- [ ] Make Textual inversion network trainer (network that spits out TI embeddings)

---

## Change Log

#### 2023-08-05
 - Huge memory rework and slider rework. Slider training is better thant ever with no more
ram spikes. I also made it so all 4 parts of the slider algorythm run in one batch so they share gradient
accumulation. This makes it much faster and more stable. 
 - Updated the example config to be something more practical and more updated to current methods. It is now
a detail slide and shows how to train one without a subject. 512x512 slider training for 1.5 should work on 
6GB gpu now. Will test soon to verify. 


#### 2021-10-20
 - Windows support bug fixes
 - Extensions! Added functionality to make and share custom extensions for training, merging, whatever.
check out the example in the `extensions` folder. Read more about that above.
 - Model Merging, provided via the example extension.

#### 2023-08-03
Another big refactor to make SD more modular.

Made batch image generation script

#### 2023-08-01
Major changes and update. New LoRA rescale tool, look above for details. Added better metadata so
Automatic1111 knows what the base model is. Added some experiments and a ton of updates. This thing is still unstable
at the moment, so hopefully there are not breaking changes. 

Unfortunately, I am too lazy to write a proper changelog with all the changes.

I added SDXL training to sliders... but.. it does not work properly. 
The slider training relies on a model's ability to understand that an unconditional (negative prompt)
means you do not want that concept in the output. SDXL does not understand this for whatever reason, 
which makes separating out
concepts within the model hard. I am sure the community will find a way to fix this 
over time, but for now, it is not 
going to work properly. And if any of you are thinking "Could we maybe fix it by adding 1 or 2 more text
encoders to the model as well as a few more entirely separate diffusion networks?" No. God no. It just needs a little
training without every experimental new paper added to it. The KISS principal. 


#### 2023-07-30
Added "anchors" to the slider trainer. This allows you to set a prompt that will be used as a 
regularizer. You can set the network multiplier to force spread consistency at high weights
