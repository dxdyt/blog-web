---
title: LMCache
date: 2025-06-30T12:34:28+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1749802449762-5e428ccf9a45?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTEyNTc5NTJ8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1749802449762-5e428ccf9a45?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTEyNTc5NTJ8&ixlib=rb-4.1.0
---

# [LMCache/LMCache](https://github.com/LMCache/LMCache)

<div align="center">
<img src="https://github.com/user-attachments/assets/50c58c75-f37a-45e8-bf82-793439480f0f" width="720" alt="lmcache logo">

</a>
</div>

<p align="center">
  <a href="https://join.slack.com/t/lmcacheworkspace/shared_invite/zt-2viziwhue-5Amprc9k5hcIdXT7XevTaQ">
    <img height="40" alt="Join Slack" src="https://img.shields.io/badge/LMCache-Join%20Slack-blue?logo=slack">
  </a>
  <a href="https://docs.lmcache.ai/">
    <img height="40" alt="Documentation" src="https://img.shields.io/badge/docs-blue?logo=readthedocs&logoColor=f0f8ff">
  </a>
</p>
<p align="center">
  <a href="https://deepwiki.com/LMCache/LMCache">
    <img height="30" src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki">
  </a>
  <img height="30" alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/w/LMCache/LMCache">
  <img height="30" alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/LMCache">
  <a href="https://www.youtube.com/channel/UC58zMz55n70rtf1Ak2PULJA">
    <img height="30" alt="YouTube Channel Views" src="https://img.shields.io/youtube/channel/views/UC58zMz55n70rtf1Ak2PULJA">
  </a>
</p>

<h3 align="center">
    Redis for LLMs - Infinite and Ultra-Fast
</h3>

----


LMCache is an **LLM** serving engine extension to **reduce TTFT** and **increase throughput**, especially under long-context scenarios. By storing the KV caches of reusable texts across various locations, including (GPU, CPU DRAM, Local Disk), LMCache reuses the KV caches of **_any_** reused text (not necessarily prefix) in **_any_** serving engine instance. Thus, LMCache saves precious GPU cycles and reduces user response delay.  

By combining LMCache with vLLM, LMCache achieves 3-10x delay savings and GPU cycle reduction in many LLM use cases, including multi-round QA and RAG.

Try LMCache with pre-built vllm docker images [here](https://docs.lmcache.ai/developer_guide/docker_file.html).

# 🚀 Performance snapshot
![performance](https://github.com/user-attachments/assets/86137f17-f216-41a0-96a7-e537764f7a4c)


# 💻 Installation and Quickstart

Please refer to our detailed documentation for [LMCache V1](https://docs.lmcache.ai/getting_started/installation.html#install-from-source-v1) and [LMCache V0](https://docs.lmcache.ai/getting_started/installation.html#install-from-source-v0)

For large-scale deployment, please refer to [vLLM Production Stack](https://github.com/vllm-project/production-stack)!

# Interested in Connecting?
Fill out the [interest form](https://forms.gle/mQfQDUXbKfp2St1z7), [sign up for our newsletter](https://mailchi.mp/tensormesh/lmcache-sign-up-newsletter), or [drop an email](contact@lmcache.ai), and our team will reach out to you!

# 🛣️ News and Milestones

- [x] LMCache V1 with vLLM integration with following features is live 🔥
  * High performance CPU KVCache offloading
  * Disaggregated prefill
  * P2P KVCache sharing
- [x] LMCache is supported in the [vLLM production stack ecosystem](https://github.com/vllm-project/production-stack/tree/main) 
- [x] User and developer documentation
- [x] Stable support for non-prefix KV caches
- [x] Support installation through pip install and integrate with latest vLLM
- [x] First release of LMCache 


# 📖 Blogs and documentations

Our latest [blog posts](https://lmcache.github.io) and the [documentation](https://docs.lmcache.ai/) pages are available online

# Community meeting

The community meeting for LMCache is hosted weekly.
Meeting Details:

- Tuesdays at 9:00 AM PT – [Add to Calendar](https://drive.google.com/file/d/15Xz8-LtpBQ5QgR7KrorOOyfuohCFQmwn/view?usp=drive_link)

- Tuesdays at 6:30 PM PT – [Add to Calendar](https://drive.google.com/file/d/1WMZNFXV24kWzprDjvO-jQ7mOY7whqEdG/view?usp=drive_link)

Meetings **alternate weekly** between the two times. All are welcome to join!

## Contributing

We welcome and value any contributions and collaborations.  Please check out [CONTRIBUTING.md](CONTRIBUTING.md) for how to get involved.


## Citation
If you use LMCache for your research, please cite our papers:

```
@inproceedings{liu2024cachegen,
  title={Cachegen: Kv cache compression and streaming for fast large language model serving},
  author={Liu, Yuhan and Li, Hanchen and Cheng, Yihua and Ray, Siddhant and Huang, Yuyang and Zhang, Qizheng and Du, Kuntai and Yao, Jiayi and Lu, Shan and Ananthanarayanan, Ganesh and others},
  booktitle={Proceedings of the ACM SIGCOMM 2024 Conference},
  pages={38--56},
  year={2024}
}

@article{cheng2024large,
  title={Do Large Language Models Need a Content Delivery Network?},
  author={Cheng, Yihua and Du, Kuntai and Yao, Jiayi and Jiang, Junchen},
  journal={arXiv preprint arXiv:2409.13761},
  year={2024}
}

@inproceedings{10.1145/3689031.3696098,
  author = {Yao, Jiayi and Li, Hanchen and Liu, Yuhan and Ray, Siddhant and Cheng, Yihua and Zhang, Qizheng and Du, Kuntai and Lu, Shan and Jiang, Junchen},
  title = {CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion},
  year = {2025},
  url = {https://doi.org/10.1145/3689031.3696098},
  doi = {10.1145/3689031.3696098},
  booktitle = {Proceedings of the Twentieth European Conference on Computer Systems},
  pages = {94–109},
}

  
```

## License

This project is licensed under Apache License 2.0. See the [LICENSE](LICENSE) file for details.

