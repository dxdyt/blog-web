---
title: WhisperLiveKit
date: 2025-08-28T12:21:40+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1754317377241-1267a73431fe?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTYzNTQ4NzR8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1754317377241-1267a73431fe?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTYzNTQ4NzR8&ixlib=rb-4.1.0
---

# [QuentinFuxa/WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit)

<h1 align="center">WhisperLiveKit</h1>

<p align="center">
<img src="https://raw.githubusercontent.com/QuentinFuxa/WhisperLiveKit/refs/heads/main/demo.png" alt="WhisperLiveKit Demo" width="730">
</p>

<p align="center"><b>Real-time, Fully Local Speech-to-Text with Speaker Identification</b></p>

<p align="center">
<a href="https://pypi.org/project/whisperlivekit/"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/whisperlivekit?color=g"></a>
<a href="https://pepy.tech/project/whisperlivekit"><img alt="PyPI Downloads" src="https://static.pepy.tech/personalized-badge/whisperlivekit?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=installations"></a>
<a href="https://pypi.org/project/whisperlivekit/"><img alt="Python Versions" src="https://img.shields.io/badge/python-3.9--3.13-dark_green"></a>
<a href="https://github.com/QuentinFuxa/WhisperLiveKit/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT/Dual Licensed-dark_green"></a>
</p>


Real-time speech transcription directly to your browser, with a ready-to-use backend+server and a simple frontend. ✨

#### Powered by Leading Research:

- [SimulStreaming](https://github.com/ufal/SimulStreaming) (SOTA 2025) - Ultra-low latency transcription with AlignAtt policy
- [WhisperStreaming](https://github.com/ufal/whisper_streaming) (SOTA 2023) - Low latency transcription with LocalAgreement policy
- [Streaming Sortformer](https://arxiv.org/abs/2507.18446) (SOTA 2025) - Advanced real-time speaker diarization
- [Diart](https://github.com/juanmc2005/diart) (SOTA 2021) - Real-time speaker diarization
- [Silero VAD](https://github.com/snakers4/silero-vad) (2024) - Enterprise-grade Voice Activity Detection


> **Why not just run a simple Whisper model on every audio batch?** Whisper is designed for complete utterances, not real-time chunks. Processing small segments loses context, cuts off words mid-syllable, and produces poor transcription. WhisperLiveKit uses state-of-the-art simultaneous speech research for intelligent buffering and incremental processing.


### Architecture

<img alt="Architecture" src="https://raw.githubusercontent.com/QuentinFuxa/WhisperLiveKit/refs/heads/main/architecture.png" />

*The backend supports multiple concurrent users. Voice Activity Detection reduces overhead when no voice is detected.*

### Installation & Quick Start

```bash
pip install whisperlivekit
```

>  **FFmpeg is required** and must be installed before using WhisperLiveKit
> 
> | OS | How to install |
> |-----------|-------------|
>  | Ubuntu/Debian | `sudo apt install ffmpeg` |
> | MacOS | `brew install ffmpeg` |
> | Windows | Download .exe from https://ffmpeg.org/download.html and add to PATH |

#### Quick Start
1. **Start the transcription server:**
   ```bash
   whisperlivekit-server --model base --language en
   ```

2. **Open your browser** and navigate to `http://localhost:8000`. Start speaking and watch your words appear in real-time!


> - See [tokenizer.py](https://github.com/QuentinFuxa/WhisperLiveKit/blob/main/whisperlivekit/simul_whisper/whisper/tokenizer.py) for the list of all available languages.
> - For HTTPS requirements, see the **Parameters** section for SSL configuration options.

 

#### Optional Dependencies

| Optional | `pip install` |
|-----------|-------------|
| **Speaker diarization with Sortformer** | `git+https://github.com/NVIDIA/NeMo.git@main#egg=nemo_toolkit[asr]` |
| Speaker diarization with Diart | `diart` |
| Original Whisper backend | `whisper` |
| Improved timestamps backend | `whisper-timestamped` |
| Apple Silicon optimization backend | `mlx-whisper` |
| OpenAI API backend | `openai` |

See  **Parameters & Configuration** below on how to use them.



### Usage Examples

**Command-line Interface**: Start the transcription server with various options:

```bash
# Use better model than default (small)
whisperlivekit-server --model large-v3

# Advanced configuration with diarization and language
whisperlivekit-server --host 0.0.0.0 --port 8000 --model medium --diarization --language fr
```


**Python API Integration**: Check [basic_server](https://github.com/QuentinFuxa/WhisperLiveKit/blob/main/whisperlivekit/basic_server.py) for a more complete example of how to use the functions and classes.

```python
from whisperlivekit import TranscriptionEngine, AudioProcessor, parse_args
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
import asyncio

transcription_engine = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global transcription_engine
    transcription_engine = TranscriptionEngine(model="medium", diarization=True, lan="en")
    yield

app = FastAPI(lifespan=lifespan)

async def handle_websocket_results(websocket: WebSocket, results_generator):
    async for response in results_generator:
        await websocket.send_json(response)
    await websocket.send_json({"type": "ready_to_stop"})

@app.websocket("/asr")
async def websocket_endpoint(websocket: WebSocket):
    global transcription_engine

    # Create a new AudioProcessor for each connection, passing the shared engine
    audio_processor = AudioProcessor(transcription_engine=transcription_engine)    
    results_generator = await audio_processor.create_tasks()
    results_task = asyncio.create_task(handle_websocket_results(websocket, results_generator))
    await websocket.accept()
    while True:
        message = await websocket.receive_bytes()
        await audio_processor.process_audio(message)        
```

**Frontend Implementation**: The package includes an HTML/JavaScript implementation [here](https://github.com/QuentinFuxa/WhisperLiveKit/blob/main/whisperlivekit/web/live_transcription.html). You can also import it using `from whisperlivekit import get_web_interface_html` & `page = get_web_interface_html()`


## Parameters & Configuration

An important list of parameters can be changed. But what *should* you change?
- the `--model` size. List and recommandations [here](https://github.com/QuentinFuxa/WhisperLiveKit/blob/main/available_models.md)
- the `--language`.  List [here](https://github.com/QuentinFuxa/WhisperLiveKit/blob/main/whisperlivekit/simul_whisper/whisper/tokenizer.py). If you use `auto`, the model attempts to detect the language automatically, but it tends to bias towards English.
- the `--backend` ? you can switch to `--backend faster-whisper` if  `simulstreaming` does not work correctly or if you prefer to avoid the dual-license requirements.
- `--warmup-file`, if you have one
- `--host`, `--port`, `--ssl-certfile`, `--ssl-keyfile`, if you set up a server
- `--diarization`, if you want to use it.

The rest I don't recommend. But below are your options.

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--model` | Whisper model size. | `small` |
| `--language` | Source language code or `auto` | `auto` |
| `--task` | `transcribe` or `translate` | `transcribe` |
| `--backend` | Processing backend | `simulstreaming` |
| `--min-chunk-size` | Minimum audio chunk size (seconds) | `1.0` |
| `--no-vac` | Disable Voice Activity Controller | `False` |
| `--no-vad` | Disable Voice Activity Detection | `False` |
| `--warmup-file` | Audio file path for model warmup | `jfk.wav` |
| `--host` | Server host address | `localhost` |
| `--port` | Server port | `8000` |
| `--ssl-certfile` | Path to the SSL certificate file (for HTTPS support) | `None` |
| `--ssl-keyfile` | Path to the SSL private key file (for HTTPS support) | `None` |


| WhisperStreaming backend options | Description | Default |
|-----------|-------------|---------|
| `--confidence-validation` | Use confidence scores for faster validation | `False` |
| `--buffer_trimming` | Buffer trimming strategy (`sentence` or `segment`) | `segment` |


| SimulStreaming backend options | Description | Default |
|-----------|-------------|---------|
| `--frame-threshold` | AlignAtt frame threshold (lower = faster, higher = more accurate) | `25` |
| `--beams` | Number of beams for beam search (1 = greedy decoding) | `1` |
| `--decoder` | Force decoder type (`beam` or `greedy`) | `auto` |
| `--audio-max-len` | Maximum audio buffer length (seconds) | `30.0` |
| `--audio-min-len` | Minimum audio length to process (seconds) | `0.0` |
| `--cif-ckpt-path` | Path to CIF model for word boundary detection | `None` |
| `--never-fire` | Never truncate incomplete words | `False` |
| `--init-prompt` | Initial prompt for the model | `None` |
| `--static-init-prompt` | Static prompt that doesn't scroll | `None` |
| `--max-context-tokens` | Maximum context tokens | `None` |
| `--model-path` | Direct path to .pt model file. Download it if not found | `./base.pt` |
| `--preloaded-model-count` | Optional. Number of models to preload in memory to speed up loading (set up to the expected number of concurrent users) | `1` |

| Diarization options | Description | Default |
|-----------|-------------|---------|
| `--diarization` | Enable speaker identification | `False` |
| `--diarization-backend` |  `diart` or `sortformer` | `sortformer` |
| `--segmentation-model` | Hugging Face model ID for Diart segmentation model. [Available models](https://github.com/juanmc2005/diart/tree/main?tab=readme-ov-file#pre-trained-models) | `pyannote/segmentation-3.0` |
| `--embedding-model` | Hugging Face model ID for Diart embedding model. [Available models](https://github.com/juanmc2005/diart/tree/main?tab=readme-ov-file#pre-trained-models) | `speechbrain/spkrec-ecapa-voxceleb` |


> For diarization using Diart, you need access to pyannote.audio models:
> 1. [Accept user conditions](https://huggingface.co/pyannote/segmentation) for the `pyannote/segmentation` model
> 2. [Accept user conditions](https://huggingface.co/pyannote/segmentation-3.0) for the `pyannote/segmentation-3.0` model
> 3. [Accept user conditions](https://huggingface.co/pyannote/embedding) for the `pyannote/embedding` model
>4. Login with HuggingFace: `huggingface-cli login`

### 🚀 Deployment Guide

To deploy WhisperLiveKit in production:
 
1. **Server Setup**: Install production ASGI server & launch with multiple workers
   ```bash
   pip install uvicorn gunicorn
   gunicorn -k uvicorn.workers.UvicornWorker -w 4 your_app:app
   ```

2. **Frontend**: Host your customized version of the `html` example & ensure WebSocket connection points correctly

3. **Nginx Configuration** (recommended for production):
    ```nginx    
   server {
       listen 80;
       server_name your-domain.com;
        location / {
            proxy_pass http://localhost:8000;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
    }}
    ```

4. **HTTPS Support**: For secure deployments, use "wss://" instead of "ws://" in WebSocket URL

## 🐋 Docker

Deploy the application easily using Docker with GPU or CPU support.

### Prerequisites
- Docker installed on your system
- For GPU support: NVIDIA Docker runtime installed

### Quick Start

**With GPU acceleration (recommended):**
```bash
docker build -t wlk .
docker run --gpus all -p 8000:8000 --name wlk wlk
```

**CPU only:**
```bash
docker build -f Dockerfile.cpu -t wlk .
docker run -p 8000:8000 --name wlk wlk
```

### Advanced Usage

**Custom configuration:**
```bash
# Example with custom model and language
docker run --gpus all -p 8000:8000 --name wlk wlk --model large-v3 --language fr
```

### Memory Requirements
- **Large models**: Ensure your Docker runtime has sufficient memory allocated


#### Customization

- `--build-arg` Options:
  - `EXTRAS="whisper-timestamped"` - Add extras to the image's installation (no spaces). Remember to set necessary container options!
  - `HF_PRECACHE_DIR="./.cache/"` - Pre-load a model cache for faster first-time start
  - `HF_TKN_FILE="./token"` - Add your Hugging Face Hub access token to download gated models

## 🔮 Use Cases
Capture discussions in real-time for meeting transcription, help hearing-impaired users follow conversations through accessibility tools, transcribe podcasts or videos automatically for content creation, transcribe support calls with speaker identification for customer service...
