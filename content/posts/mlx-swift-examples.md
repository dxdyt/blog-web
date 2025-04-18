---
title: mlx-swift-examples
date: 2025-01-25T12:18:55+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1737079282750-5e2580fe5603?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3Mzc3Nzg2ODl8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1737079282750-5e2580fe5603?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3Mzc3Nzg2ODl8&ixlib=rb-4.0.3
---

# [ml-explore/mlx-swift-examples](https://github.com/ml-explore/mlx-swift-examples)

# MLX Swift Examples

Example [MLX Swift](https://github.com/ml-explore/mlx-swift) programs.

- [MNISTTrainer](Applications/MNISTTrainer/README.md): An example that runs on
  both iOS and macOS that downloads MNIST training data and trains a
  [LeNet](https://en.wikipedia.org/wiki/LeNet). 

- [LLMEval](Applications/LLMEval/README.md): An example that runs on both iOS
  and macOS that downloads an LLM and tokenizer from Hugging Face and 
  generates text from a given prompt. 
  
- [VLMEval](Applications/VLMEval/README.md): An example that runs on iOS, macOS and visionOS to download a VLM and tokenizer from Hugging Face and
  analyzes the given image and describe it in text.

- [LinearModelTraining](Tools/LinearModelTraining/README.md): An example that
  trains a simple linear model.

- [StableDiffusionExample](Applications/StableDiffusionExample/README.md): An 
  example that runs on both iOS and macOS that downloads a stable diffusion model
  from Hugging Face and  and generates an image from a given prompt. 

- [llm-tool](Tools/llm-tool/README.md): A command line tool for generating text
  using a variety of LLMs available on the Hugging Face hub.

- [image-tool](Tools/image-tool/README.md): A command line tool for generating images
  using a stable diffusion model from Hugging Face.

- [mnist-tool](Tools/mnist-tool/README.md): A command line tool for training a
  a LeNet on MNIST.
  
## Running

The application and command line tool examples can be run from Xcode or from
the command line:

```
./mlx-run llm-tool --prompt "swift programming language"
```

See also:

- [MLX troubleshooting](https://ml-explore.github.io/mlx-swift/MLX/documentation/mlx/troubleshooting)

## Installation of libraries

The MLXLLM, MLXVLM, MLXLMCommon, MLXMNIST, MLXEmbedders, and StableDiffusion libraries in the example repo are available
as Swift Packages.


Add the following dependency to your Package.swift

```swift  
.package(url: "https://github.com/ml-explore/mlx-swift-examples/", branch: "main"),
```

Then add one or more libraries to the target as a dependency:

```swift
.target(
    name: "YourTargetName",
    dependencies: [
        .product(name: "MLXLLM", package: "mlx-swift-examples")
    ]),
```

Alternatively, add `https://github.com/ml-explore/mlx-swift-examples/` to the `Project Dependencies` and set the `Dependency Rule` to `Branch` and `main` in Xcode. 
