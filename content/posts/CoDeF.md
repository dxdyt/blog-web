---
title: CoDeF
date: 2023-08-21T12:14:46+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1690940822379-43068cdaf9be?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTI1OTEyNzR8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1690940822379-43068cdaf9be?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTI1OTEyNzR8&ixlib=rb-4.0.3
---

# [qiuyu96/CoDeF](https://github.com/qiuyu96/CoDeF)

﻿# CoDeF: Content Deformation Fields for Temporally Consistent Video Processing

<img src='docs/teaser.gif'></img>

[Hao Ouyang](https://ken-ouyang.github.io/)\*, [Qiuyu Wang](https://github.com/qiuyu96/)\*, [Yuxi Xiao](https://henry123-boy.github.io/)\*, [Qingyan Bai](https://scholar.google.com/citations?user=xUMjxi4AAAAJ&hl=en), [Juntao Zhang](https://github.com/JordanZh), [Kecheng Zheng](https://scholar.google.com/citations?user=hMDQifQAAAAJ), [Xiaowei Zhou](https://xzhou.me/),
[Qifeng Chen](https://cqf.io/)&#8224;, [Yujun Shen](https://shenyujun.github.io/)&#8224; (*equal contribution, &#8224;corresponding author)

#### [Project Page](https://qiuyu96.github.io/CoDeF/) | [Paper](https://arxiv.org/abs/2308.07926) | [High-Res Translation Demo](https://ezioby.github.io/CoDeF_Demo/)

<!-- Abstract: *This work presents the content deformation field **CoDeF** as a new type of video representation, which consists of a canonical content field aggregating the static contents in the entire video and a temporal deformation field recording the transformations from the canonical image (i.e., rendered from the canonical content field) to each individual frame along the time axis. Given a target video, these two fields are jointly optimized to reconstruct it through a carefully tailored rendering pipeline. We also introduce some decent regularizations into the optimization process, urging the canonical content field to inherit semantics (e.g., the object shape) from the video. With such a design, **CoDeF** naturally supports lifting image algorithms to videos, in the sense that one can apply an image algorithm to the canonical image and effortlessly propagate the outcomes to the entire video with the aid of the temporal deformation field. We experimentally show that **CoDeF** is able to lift image-to-image translation to video-to-video translation and lift keypoint detection to keypoint tracking without any training. More importantly, thanks to our lifting strategy that deploys the algorithms on only one image, we achieve superior cross-frame consistency in translated videos compared to existing video-to-video translation approaches, and even manage to track non-rigid objects like water and smog.* -->

## Requirements
The codebase is tested on
* Ubuntu 20.04
* Python 3.10
* [PyTorch](https://pytorch.org/) 2.0.0
* [PyTorch Lightning](https://www.pytorchlightning.ai/index.html) 2.0.2
* 1 Nvidia GPU (RTX A6000 48GB) with CUDA version 11.7 
(Other GPUs are also suitable, and 10GB of GPU memory is sufficient to run our code.)

To use video visualizer, please install `ffmpeg` by:

```
sudo apt-get install ffmpeg
```

For additional Python libraries, please install by:

```
pip install -r requirements.txt
```

Our code also depends on [tiny-cuda-nn](https://github.com/NVlabs/tiny-cuda-nn).
See [this](https://github.com/NVlabs/tiny-cuda-nn#pytorch-extension)
for Pytorch extension install instructions.


## Data
### Our data
Download our data from [this URL](https://drive.google.com/file/d/1cKZF6ILeokCjsSAGBmummcQh0uRGaC_F/view?usp=sharing), unzip the file and put it in the current directory. Some additional data can be downloaded from [here](https://rec.ustc.edu.cn/share/5d1e0bb0-31d7-11ee-aa60-d1fd6c62dfb4).
### Customize your own data
*To be released.*

And organize files as follows:
```
CoDeF
│
└─── all_sequences
    │
    └─── NAME1
           └─ NAME1
           └─ NAME1_masks_0 (optional)
           └─ NAME1_masks_1 (optional)
           └─ NAME1_flow (optional)
           └─ NAME1_flow_confidence (optional)
    │
    └─── NAME2
           └─ NAME2
           └─ NAME2_masks_0 (optional)
           └─ NAME2_masks_1 (optional)
           └─ NAME2_flow (optional)
           └─ NAME2_flow_confidence (optional)
    │
    └─── ...
```
## Pretrained checkpoints
You can download the pre-trained checkpoints trained with the current codebase as follows:
| Sequence Name | Config |                           Download                           |
| :-------- | :----: | :----------------------------------------------------------: |
| beauty_0 | configs/beauty_0/base.yaml |  [Google drive link](https://drive.google.com/file/d/11SWfnfDct8bE16802PyqYJqsU4x6ACn8/view?usp=sharing) |
| beauty_1 | configs/beauty_1/base.yaml |  [Google drive link](https://drive.google.com/file/d/1bSK0ChbPdURWGLdtc9CPLkN4Tfnng51k/view?usp=sharing) |
| white_smoke      | configs/white_smoke/base.yaml |  [Google drive link](https://drive.google.com/file/d/1QOBCDGV2hHwxq4eL1E_45z5zhZ-wTJR7/view?usp=sharing) |
| lemon_hit      | configs/lemon_hit/base.yaml |  [Google drive link](https://drive.google.com/file/d/140ctcLbv7JTIiy53MuCYtI4_zpIvRXzq/view?usp=sharing) |
| scene_0      | configs/scene_0/base.yaml |  [Google drive link](https://drive.google.com/file/d/1abOdREarfw1DGscahOJd2gZf1Xn_zN-F/view?usp=sharing) |

And organize files as follows:
```
CoDeF
│
└─── ckpts/all_sequences
    │
    └─── NAME1
        │
        └─── EXP_NAME (base)
            │
            └─── NAME1.ckpt
    │
    └─── NAME2
        │
        └─── EXP_NAME (base)
            │
            └─── NAME2.ckpt
    |
    └─── ...
```

## Train a new model
```bash
./scripts/train_multi.sh
```
where:
* `GPU`: Decide which GPU to train on;
* `NAME`: Name of the video sequence;
* `EXP_NAME`: Name of the experiment;
* `ROOT_DIRECTORY`: Directory of the input video sequence;
* `MODEL_SAVE_PATH`: Path to save the checkpoints;
* `LOG_SAVE_PATH`: Path to save the logs;
* `MASK_DIRECTORY`: Directory of the preprocessed masks (optional);
* `FLOW_DIRECTORY`: Directory of the preprocessed optical flows (optional);

Please check configuration files in ``configs/``, and you can always add your own model config.

## Test reconstruction <a id="anchor"></a>
```bash
./scripts/test_multi.sh
```
After running the script, the reconstructed videos can be found in `results/all_sequences/{NAME}/{EXP_NAME}`, along with the canonical image.

## Test video translation
After obtaining the canonical image through [this step](#anchor), use your preferred text prompts to transfer it using [ControlNet](https://github.com/lllyasviel/ControlNet).
Once you have the transferred canonical image, place it in `all_sequences/${NAME}/${EXP_NAME}_control` (i.e. `CANONICAL_DIR` in `scripts/test_canonical.sh`). 

Then run:
```bash
./scripts/test_canonical.sh
```
The transferred results can be seen in `results/all_sequences/{NAME}/{EXP_NAME}_transformed`.

*Note*: The `canonical_wh` option in the configuration file should be set with caution, usually a little larger than `img_wh`, as it determines the field of view of the canonical image.

### BibTeX

```bibtex
@article{ouyang2023codef,
      title={CoDeF: Content Deformation Fields for Temporally Consistent Video Processing}, 
      author={Hao Ouyang and Qiuyu Wang and Yuxi Xiao and Qingyan Bai and Juntao Zhang and Kecheng Zheng and Xiaowei Zhou and Qifeng Chen and Yujun Shen},
      journal={arXiv preprint arXiv:2308.07926},
      year={2023}
}
```




