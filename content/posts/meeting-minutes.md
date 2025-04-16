---
title: meeting-minutes
date: 2025-04-16T12:21:13+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1742736839475-2ca610373470?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDQ3NzcyNDl8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1742736839475-2ca610373470?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDQ3NzcyNDl8&ixlib=rb-4.0.3
---

# [Zackriya-Solutions/meeting-minutes](https://github.com/Zackriya-Solutions/meeting-minutes)

<div align="center" style="border-bottom: none">
    <h1>
        <img src="docs/6.png" width="400" style="border-radius: 10px;" />
        <br>
        Meetily - AI-Powered Meeting Assistant
    </h1>
    <br>
    <a href="https://github.com/Zackriya-Solutions/meeting-minutes/releases/tag/v0.0.3"><img src="https://img.shields.io/badge/Pre_Release-v0.0.3-brightgreen" alt="Pre-Release"></a>
    <a href="https://github.com/Zackriya-Solutions/meeting-minutes/releases/tag/v0.0.3"><img src="https://img.shields.io/badge/Stars-1000+-red" alt="Stars"></a>
    <a href="https://github.com/Zackriya-Solutions/meeting-minutes/releases/tag/v0.0.3"><img src="https://img.shields.io/badge/License-MIT-blue" alt="License"></a>
    <a href="https://github.com/Zackriya-Solutions/meeting-minutes/releases/tag/v0.0.3"><img src="https://img.shields.io/badge/Supported_OS-macOS,_Windows-yellow" alt="Supported OS"></a>
    <br>
    <h3>
    <br>
    Open source Ai Assistant for taking meeting notes
    </h3>
    <p align="center">
    <a href="https://meetily.zackriya.com"><b>Website</b></a> •
    <a href="https://in.linkedin.com/company/zackriya-solutions"><b>Author</b></a>
    •
    <a href="https://discord.gg/crRymMQBFH"><b>Discord Channel</b></a>
</p>
    <p align="center">
    
 An AI-Powered Meeting Assistant that captures live meeting audio, transcribes it in real-time, and generates summaries while ensuring user privacy. Perfect for teams who want to focus on discussions while automatically capturing and organizing meeting content without the need for external servers or complex infrastructure. 
</p>

<p align="center">
    <img src="docs/demo_small.gif" width="650" alt="Meetily Demo" />
    <br>
    <a href="https://youtu.be/5k_Q5Wlahuk">View full Demo Video</a>
</p>

</div>


## Overview

An AI-powered meeting assistant that captures live meeting audio, transcribes it in real-time, and generates summaries while ensuring user privacy. Perfect for teams who want to focus on discussions while automatically capturing and organizing meeting content.

### Why?

While there are many meeting transcription tools available, this solution stands out by offering:
- **Privacy First**: All processing happens locally on your device
- **Cost Effective**: Uses open-source AI models instead of expensive APIs
- **Flexible**: Works offline, supports multiple meeting platforms
- **Customizable**: Self-host and modify for your specific needs
- **Intelligent**: Built-in knowledge graph for semantic search across meetings

## Features

✅ Modern, responsive UI with real-time updates

✅ Real-time audio capture (microphone + system audio)

✅ Live transcription using Whisper.cpp

🚧 Speaker diarization

✅ Local processing for privacy

✅ Packaged the app for macOS and Windows

🚧 Export to Markdown/PDF


> **Note**: We have a Rust-based implementation that explores better performance and native integration. It currently implements:
> - ✅ Real-time audio capture from both microphone and system audio
> - ✅ Live transcription using locally-running Whisper
> - ✅ Speaker diarization
> - ✅ Rich text editor for notes
> 
We are currently working on:
> - ✅ Export to Markdown/PDF
> - ✅ Export to HTML


## Release 0.0.3

A new release is available!

Please check out the release [here](https://github.com/Zackriya-Solutions/meeting-minutes/releases/tag/v0.0.3).

### What's New
- **Windows Support**: Fixed audio capture issues on Windows
- **Improved Error Handling**: Better error handling and logging for audio devices
- **Enhanced Device Detection**: More robust audio device detection across platforms
- **Windows Installers**: Added both .exe and .msi installers for Windows
- Transcription quality is improved
- Bug fixes and improvements for frontend
- Better backend app build process
- Improved documentation

### What would be next?
- Database connection to save meeting minutes
- Improve summarization quality for smaller LLM models
- Add download options for meeting transcriptions 
- Add download option for summary

### Known issues
- Smaller LLMs can hallucinate, making summarization quality poor; Please use model above 32B parameter size
- Backend build process requires CMake, C++ compiler, etc. Making it harder to build
- Backend build process requires Python 3.10 or newer
- Frontend build process requires Node.js

## LLM Integration

The backend supports multiple LLM providers through a unified interface. Current implementations include:

### Supported Providers
- **Anthropic** (Claude models)
- **Groq** (Llama3.2 90 B)
- **Ollama** (Local models that supports function calling)

### Configuration
Create `.env` file with your API keys:
```env
# Required for Anthropic
ANTHROPIC_API_KEY=your_key_here  

# Required for Groq 
GROQ_API_KEY=your_key_here

```

## System Architecture

![High Level Architecture](docs/HighLevel.jpg)

### Core Components

1. **Audio Capture Service**
   - Real-time microphone/system audio capture
   - Audio preprocessing pipeline
   - Built with Rust (experimental) and Python

2. **Transcription Engine**
   - Whisper.cpp for local transcription
   - Supports multiple model sizes (tiny->large)
   - GPU-accelerated processing

3. **LLM Orchestrator**
   - Unified interface for multiple providers
   - Automatic fallback handling
   - Chunk processing with overlap
   - Model configuration:

4. **Data Services**
   - **ChromaDB**: Vector store for transcript embeddings
   - **SQLite**: Process tracking and metadata storage

5. **API Layer**
   - FastAPI endpoints:
     - POST /upload
     - POST /process
     - GET /summary/{id}
     - DELETE /summary/{id}

### Deployment Architecture

- **Frontend**: Tauri app + Next.js (packaged executables)
- **Backend**: Python FastAPI:
  - Transcript workers
  - LLM inference

## Prerequisites

- Node.js 18+
- Python 3.10+
- FFmpeg
- Rust 1.65+ (for experimental features)
- Cmake 3.22+ (for building the frontend)
- For Windows: Visual Studio Build Tools with C++ development workload

## Setup Instructions

### 1. Frontend Setup

#### Run packaged version

Go to the [releases page](https://github.com/Zackriya-Solutions/meeting-minutes/releases) and download the latest version.

**For Windows:**
- Download either the `.exe` installer or `.msi` package
- Once the installer is downloaded, double-click the executable file to run it
- Windows will ask if you want to run untrusted apps, click "More info" and choose "Run anyway"
- Follow the installation wizard to complete the setup
- The application will be installed and available on your desktop

**For macOS:**
- Download the `dmg_darwin_arch64.zip` file
- Extract the file
- Double-click the `.dmg` file inside the extracted folder
- Drag the application to your Applications folder
- Execute the following command in terminal to remove the quarantine attribute:
  ```
  xattr -c /Applications/meeting-minutes-frontend.app
  ```

Provide necessary permissions for audio capture and microphone access.

#### Dev run

```bash
# Navigate to frontend directory
cd frontend

# Give execute permissions to clean_build.sh
chmod +x clean_build.sh

# run clean_build.sh
./clean_build.sh
```

### 2. Backend Setup

```bash
# Clone the repository
git clone https://github.com/Zackriya-Solutions/meeting-minutes.git
cd meeting-minutes/backend

# Create and activate virtual environment
# On macOS/Linux:
python -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add environment file with API keys
# On macOS/Linux:
echo -e "ANTHROPIC_API_KEY=your_api_key\nGROQ_API_KEY=your_api_key" | tee .env

# On Windows (PowerShell):
"ANTHROPIC_API_KEY=your_api_key`nGROQ_API_KEY=your_api_key" | Out-File -FilePath .env -Encoding utf8

# Configure environment variables for Groq
# On macOS/Linux:
export GROQ_API_KEY=your_groq_api_key

# On Windows (PowerShell):
$env:GROQ_API_KEY="your_groq_api_key"

# Build dependencies
# On macOS/Linux:
chmod +x build_whisper.sh
./build_whisper.sh

# On Windows:
.\build_whisper.bat

# Start backend servers
# On macOS/Linux:
./clean_start_backend.sh

# On Windows:
.\start_with_output.ps1
```

## Development Guidelines

- Follow the established project structure
- Write tests for new features
- Document API changes
- Use type hints in Python code
- Follow ESLint configuration for JavaScript/TypeScript

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License - Feel free to use this project for your own purposes.

## Introducing Subscription

We are planning to add a subscription option so that you don't have to run the backend on your own server. This will help you scale better and run the service 24/7. This is based on a few requests we received. If you are interested, please fill out the form [here](http://zackriya.com/aimeeting/).

Last updated: March 3, 2025

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Zackriya-Solutions/meeting-minutes&type=Date)](https://star-history.com/#Zackriya-Solutions/meeting-minutes&Date)
