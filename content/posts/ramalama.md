---
title: ramalama
date: 2025-02-02T12:18:59+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1736402854452-7278e43f0a53?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3Mzg0Njk4NTN8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1736402854452-7278e43f0a53?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3Mzg0Njk4NTN8&ixlib=rb-4.0.3
---

# [containers/ramalama](https://github.com/containers/ramalama)

![RAMALAMA logo](logos/PNG/ramalama-logo-full-vertical-added-bg.png)

# RamaLama

The RamaLama project's goal is to make working with AI boring
through the use of OCI containers.

RamaLama tool facilitates local management and serving of AI Models.

On first run RamaLama inspects your system for GPU support, falling back to CPU support if no GPUs are present.

RamaLama uses container engines like Podman or Docker to pull the appropriate OCI image with all of the software necessary to run an AI Model for your systems setup.

Running in containers eliminates the need for users to configure the host system for AI. After the initialization, RamaLama runs the AI Models within a container based on the OCI image.

RamaLama then pulls AI Models from model registries. Starting a chatbot or a rest API service from a simple single command. Models are treated similarly to how Podman and Docker treat container images.

When both Podman and Docker are installed, RamaLama defaults to Podman, The `RAMALAMA_CONTAINER_ENGINE=docker` environment variable can override this behaviour. When neither are installed RamaLama will attempt to run the model with software on the local system.

RamaLama supports multiple AI model registries types called transports.
Supported transports:


## TRANSPORTS

| Transports    | Web Site                                            |
| ------------- | --------------------------------------------------- |
| HuggingFace   | [`huggingface.co`](https://www.huggingface.co)      |
| Ollama        | [`ollama.com`](https://www.ollama.com)              |
| OCI Container Registries | [`opencontainers.org`](https://opencontainers.org)|
||Examples: [`quay.io`](https://quay.io),  [`Docker Hub`](https://docker.io), and [`Artifactory`](https://artifactory.com)|

RamaLama uses the Ollama registry transport by default. Use the RAMALAMA_TRANSPORTS environment variable to modify the default. `export RAMALAMA_TRANSPORT=huggingface` Changes RamaLama to use huggingface transport.

Individual model transports can be modifies when specifying a model via the `huggingface://`, `oci://`, or `ollama://` prefix.

`ramalama pull huggingface://afrideva/Tiny-Vicuna-1B-GGUF/tiny-vicuna-1b.q2_k.gguf`

To make it easier for users, RamaLama uses shortname files, which container
alias names for fully specified AI Models allowing users to specify the shorter
names when referring to models. RamaLama reads shortnames.conf files if they
exist . These files contain a list of name value pairs for specification of
the model. The following table specifies the order which RamaLama reads the files
. Any duplicate names that exist override previously defined shortnames.

| Shortnames type | Path                                            |
| --------------- | ---------------------------------------- |
| Distribution    | /usr/share/ramalama/shortnames.conf      |
| Administrators  | /etc/ramamala/shortnames.conf            |
| Users           | $HOME/.config/ramalama/shortnames.conf   |

```code
$ cat /usr/share/ramalama/shortnames.conf
[shortnames]
  "tiny" = "ollama://tinyllama"
  "granite" = "huggingface://instructlab/granite-7b-lab-GGUF/granite-7b-lab-Q4_K_M.gguf"
  "granite:7b" = "huggingface://instructlab/granite-7b-lab-GGUF/granite-7b-lab-Q4_K_M.gguf"
  "ibm/granite" = "huggingface://instructlab/granite-7b-lab-GGUF/granite-7b-lab-Q4_K_M.gguf"
  "merlinite" = "huggingface://instructlab/merlinite-7b-lab-GGUF/merlinite-7b-lab-Q4_K_M.gguf"
  "merlinite:7b" = "huggingface://instructlab/merlinite-7b-lab-GGUF/merlinite-7b-lab-Q4_K_M.gguf"
...
```

## Install

## Install via PyPi

RamaLama is available via PyPi [https://pypi.org/project/ramalama](https://pypi.org/project/ramalama)

```
pip install ramalama
```

## Install by script
> [!TIP]
> If you are a macOS user, this is the preferred method.


Install RamaLama by running this one-liner:

```
curl -fsSL https://raw.githubusercontent.com/containers/ramalama/s/install.sh | bash
```

## Hardware Support

| Hardware                           | Enabled |
| ---------------------------------- | ------- |
| CPU                                | :white_check_mark: |
| Apple Silicon GPU (Linux / Asahi)  | :white_check_mark: |
| Apple Silicon GPU (macOS)          | :white_check_mark: |
| Apple Silicon GPU (podman-machine) | :white_check_mark: |
| Nvidia GPU (cuda)                  | :white_check_mark: |
| AMD GPU (rocm)                     | :white_check_mark: |

## COMMANDS

| Command                                                | Description                                                |
| ------------------------------------------------------ | ---------------------------------------------------------- |
| [ramalama(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama.1.md)                      | primary RamaLama man page                                  |
| [ramalama-containers(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-containers.1.md)| list all RamaLama containers                               |
| [ramalama-info(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-info.1.md)                 | display RamaLama configuration information                 |
| [ramalama-list(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-list.1.md)            | list all downloaded AI Models                              |
| [ramalama-login(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-login.1.md)          | login to remote registry                                   |
| [ramalama-logout(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-logout.1.md)        | logout from remote registry                                |
| [ramalama-pull(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-pull.1.md)            | pull AI Model from Model registry to local storage         |
| [ramalama-push(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-push.1.md)            | push AI Model from local storage to remote registry        |
| [ramalama-rm(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-rm.1.md)                | remove AI Model from local storage                         |
| [ramalama-run(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-run.1.md)              | run specified AI Model as a chatbot                        |
| [ramalama-serve(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-serve.1.md)          | serve REST API on specified AI Model                       |
| [ramalama-stop(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-stop.1.md)            | stop named container that is running AI Model              |
| [ramalama-version(1)](https://github.com/containers/ramalama/blob/main/docs/ramalama-version.1.md)      | display version of AI Model                                |

## Usage

### Running Models

You can `run` a chatbot on a model using the `run` command. By default, it pulls from the Ollama registry.

Note: RamaLama will inspect your machine for native GPU support and then will
use a container engine like Podman to pull an OCI container image with the
appropriate code and libraries to run the AI Model. This can take a long time to setup, but only on the first run.
```
$ ramalama run instructlab/merlinite-7b-lab
Copying blob 5448ec8c0696 [--------------------------------------] 0.0b / 63.6MiB (skipped: 0.0b = 0.00%)
Copying blob cbd7e392a514 [--------------------------------------] 0.0b / 65.3MiB (skipped: 0.0b = 0.00%)
Copying blob 5d6c72bcd967 done  208.5MiB / 208.5MiB (skipped: 0.0b = 0.00%)
Copying blob 9ccfa45da380 [--------------------------------------] 0.0b / 7.6MiB (skipped: 0.0b = 0.00%)
Copying blob 4472627772b1 [--------------------------------------] 0.0b / 120.0b (skipped: 0.0b = 0.00%)
>
```

After the initial container image has been downloaded, you can interact with
different models, using the container image.
```
$ ramalama run granite3-moe
> Write a hello world application in python

print("Hello World")
```

In a different terminal window see the running podman container.
```
$ podman ps
CONTAINER ID  IMAGE                             COMMAND               CREATED        STATUS        PORTS       NAMES
91df4a39a360  quay.io/ramalama/ramalama:latest  /home/dwalsh/rama...  4 minutes ago  Up 4 minutes              gifted_volhard
```

### Listing Models

You can `list` all models pulled into local storage.

```
$ ramalama list
NAME                                                                MODIFIED     SIZE
ollama://smollm:135m                                                16 hours ago 5.5M
huggingface://afrideva/Tiny-Vicuna-1B-GGUF/tiny-vicuna-1b.q2_k.gguf 14 hours ago 460M
ollama://moondream:latest                                           6 days ago   791M
ollama://phi4:latest                                                6 days ago   8.43 GB
ollama://tinyllama:latest                                           1 week ago   608.16 MB
ollama://granite3-moe:3b                                            1 week ago   1.92 GB
ollama://granite3-moe:latest                                        3 months ago 1.92 GB
ollama://llama3.1:8b                                                2 months ago 4.34 GB
ollama://llama3.1:latest                                            2 months ago 4.34 GB
```
### Pulling Models

You can `pull` a model using the `pull` command. By default, it pulls from the Ollama registry.

```
$ ramalama pull granite3-moe
 31% |████████                    |  250.11 MB/ 783.77 MB  36.95 MB/s       14s
```

### Serving Models

You can `serve` multiple models using the `serve` command. By default, it pulls from the Ollama registry.

```
$ ramalama serve --name mylama llama3
```

### Stopping servers

You can stop a running model if it is running in a container.

```
$ ramalama stop mylama
```

### UI support

To use a UI, run a `ramalama serve` command, then connect via your browser at:

127.0.0.1:8080

## Diagram

```
+---------------------------+
|                           |
| ramalama run granite3-moe |
|                           |
+-------+-------------------+
	|
	|
        |           +------------------+           +------------------+
        |           | Pull inferencing |           | Pull model layer |
        +-----------| runtime (cuda)   |---------->| granite3-moe     |
                    +------------------+           +------------------+
						   | Repo options:    |
						   +-+-------+------+-+
						     |       |      |
						     v       v      v
					     +---------+ +------+ +----------+
					     | Hugging | | OCI  | | Ollama   |
					     | Face    | |      | | Registry |
					     +-------+-+ +---+--+ +-+--------+
						     |       |      |
						     v       v      v
						   +------------------+
						   | Start with       |
						   | cuda runtime     |
						   | and              |
						   | granite3-moe     |
						   +------------------+
```

## In development

Regard this alpha, everything is under development, so expect breaking changes, luckily it's easy to reset everything and re-install:

```
rm -rf /var/lib/ramalama # only required if running as root user
rm -rf $HOME/.local/share/ramalama
```

and install again.

## Credit where credit is due

This project wouldn't be possible without the help of other projects like:

llama.cpp  
whisper.cpp  
vllm  
podman   
huggingface  

so if you like this tool, give some of these repos a :star:, and hey, give us a :star: too while you are at it.

## Community

[`Matrix`](https://matrix.to/#/#ramalama:fedoraproject.org)

## Contributors

Open to contributors

<a href="https://github.com/containers/ramalama/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=containers/ramalama" />
</a>
