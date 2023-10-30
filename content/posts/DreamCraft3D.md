---
title: DreamCraft3D
date: 2023-10-30T12:16:40+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1697228428285-8c442346434a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTg2MzkzMTZ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1697228428285-8c442346434a?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2OTg2MzkzMTZ8&ixlib=rb-4.0.3
---

# [deepseek-ai/DreamCraft3D](https://github.com/deepseek-ai/DreamCraft3D)

# DreamCraft3D

[**Paper**](https://arxiv.org/abs/2310.16818) | [**Project Page**](https://mrtornado24.github.io/DreamCraft3D/) | [**Youtube video**](https://www.youtube.com/watch?v=0FazXENkQms)

Official implementation of DreamCraft3D: Hierarchical 3D Generation with Bootstrapped Diffusion Prior

[Jingxiang Sun](https://mrtornado24.github.io/), [Bo Zhang](https://bo-zhang.me/), [Ruizhi Shao](https://dsaurus.github.io/saurus/), [Lizhen Wang](https://lizhenwangt.github.io/), [Wen Liu](https://github.com/StevenLiuWen), [Zhenda Xie](https://zdaxie.github.io/), [Yebin Liu](https://liuyebin.com/)

**Code will come soon.**

Abstract: *We present DreamCraft3D, a hierarchical 3D content generation method that produces high-fidelity and coherent 3D objects. We tackle the problem by leveraging a 2D reference image to guide the stages of geometry sculpting and texture boosting. A central focus of this work is to address the consistency issue that existing
works encounter. To sculpt geometries that render coherently, we perform score
distillation sampling via a view-dependent diffusion model. This 3D prior, alongside several training strategies, prioritizes the geometry consistency but compromises the texture fidelity. We further propose **Bootstrapped Score Distillation** to
specifically boost the texture. We train a personalized diffusion model, Dreambooth, on the augmented renderings of the scene, imbuing it with 3D knowledge
of the scene being optimized. The score distillation from this 3D-aware diffusion prior provides view-consistent guidance for the scene. Notably, through an
alternating optimization of the diffusion prior and 3D scene representation, we
achieve mutually reinforcing improvements: the optimized 3D scene aids in training the scene-specific diffusion model, which offers increasingly view-consistent
guidance for 3D optimization. The optimization is thus bootstrapped and leads
to substantial texture boosting. With tailored 3D priors throughout the hierarchical generation, DreamCraft3D generates coherent 3D objects with photorealistic
renderings, advancing the state-of-the-art in 3D content generation.*

<p align="center">
    <img src="assets/repo_static_v2.png">
</p>


## Method Overview
<p align="center">
    <img src="assets/diagram-1.png">
</p>


<!-- https://github.com/MrTornado24/DreamCraft3D/assets/45503891/8e70610c-d812-4544-86bf-7f8764e41067



https://github.com/MrTornado24/DreamCraft3D/assets/45503891/b1e8ae54-1afd-4e0f-88f7-9bd5b70fd44d



https://github.com/MrTornado24/DreamCraft3D/assets/45503891/ead40f9b-d7ee-4ee8-8d98-dbd0b8fbab97 -->


## BibTeX

```bibtex
@misc{sun2023dreamcraft3d,
      title={DreamCraft3D: Hierarchical 3D Generation with Bootstrapped Diffusion Prior}, 
      author={Jingxiang Sun and Bo Zhang and Ruizhi Shao and Lizhen Wang and Wen Liu and Zhenda Xie and Yebin Liu},
      year={2023},
      eprint={2310.16818},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
