---
title: cuda-python
date: 2025-04-11T12:22:31+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1741850826368-12d515927617?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDQzNDUzMDN8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1741850826368-12d515927617?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDQzNDUzMDN8&ixlib=rb-4.0.3
---

# [NVIDIA/cuda-python](https://github.com/NVIDIA/cuda-python)

# cuda-python

CUDA Python is the home for accessing NVIDIA’s CUDA platform from Python. It consists of multiple components:

* [cuda.core](https://nvidia.github.io/cuda-python/cuda-core/latest): Pythonic access to CUDA Runtime and other core functionalities
* [cuda.bindings](https://nvidia.github.io/cuda-python/cuda-bindings/latest): Low-level Python bindings to CUDA C APIs
* [cuda.cooperative](https://nvidia.github.io/cccl/cuda_cooperative/): A Python package providing CCCL's reusable block-wide and warp-wide *device* primitives for use within Numba CUDA kernels
* [cuda.parallel](https://nvidia.github.io/cccl/cuda_parallel/): A Python package for easy access to CCCL's highly efficient and customizable parallel algorithms, like `sort`, `scan`, `reduce`, `transform`, etc, that are callable on the *host*
* [numba.cuda](https://nvidia.github.io/numba-cuda/): Numba's target for CUDA GPU programming by directly compiling a restricted subset of Python code into CUDA kernels and device functions following the CUDA execution model.

For access to NVIDIA CPU & GPU Math Libraries, please refer to [nvmath-python](https://docs.nvidia.com/cuda/nvmath-python/latest).

CUDA Python is currently undergoing an overhaul to improve existing and bring up new components. All of the previously available functionalities from the `cuda-python` package will continue to be available, please refer to the [cuda.bindings](https://nvidia.github.io/cuda-python/cuda-bindings/latest) documentation for installation guide and further detail.

## cuda-python as a metapackage

`cuda-python` is being re-structured to become a metapackage that contains a collection of subpackages. Each subpackage is versioned independently, allowing installation of each component as needed.

### Subpackage: `cuda.core`

The `cuda.core` package offers idiomatic, pythonic access to CUDA Runtime and other functionalities.

The goals are to

1. Provide **idiomatic ("pythonic")** access to CUDA Driver, Runtime, and JIT compiler toolchain
2. Focus on **developer productivity** by ensuring end-to-end CUDA development can be performed quickly and entirely in Python
3. **Avoid homegrown** Python abstractions for CUDA for new Python GPU libraries starting from scratch
4. **Ease** developer **burden of maintaining** and catching up with latest CUDA features
5. **Flatten the learning curve** for current and future generations of CUDA developers

### Subpackage: `cuda.bindings`

The `cuda.bindings` package is a standard set of low-level interfaces, providing full coverage of and access to the CUDA host APIs from Python.

The list of available interfaces are:

* CUDA Driver
* CUDA Runtime
* NVRTC
* nvJitLink
* NVVM
