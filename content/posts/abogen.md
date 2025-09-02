---
title: abogen
date: 2025-09-02T12:23:38+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1736536475480-8f4e8bafeddd?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTY3ODY5MTN8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1736536475480-8f4e8bafeddd?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTY3ODY5MTN8&ixlib=rb-4.1.0
---

# [denizsafak/abogen](https://github.com/denizsafak/abogen)

# abogen <img width="40px" title="abogen icon" src="https://raw.githubusercontent.com/denizsafak/abogen/refs/heads/main/abogen/assets/icon.ico" align="right" style="padding-left: 10px; padding-top:5px;">

[![Build Status](https://github.com/denizsafak/abogen/actions/workflows/test_pip.yml/badge.svg)](https://github.com/denizsafak/abogen/actions)
[![GitHub Release](https://img.shields.io/github/v/release/denizsafak/abogen)](https://github.com/denizsafak/abogen/releases/latest)
[![Abogen PyPi Python Versions](https://img.shields.io/pypi/pyversions/abogen)](https://pypi.org/project/abogen/)
[![Operating Systems](https://img.shields.io/badge/os-windows%20%7C%20linux%20%7C%20macos%20-blue)](https://github.com/denizsafak/abogen/releases/latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-maroon.svg)](https://opensource.org/licenses/MIT)

Abogen is a powerful text-to-speech conversion tool that makes it easy to turn ePub, PDF, or text files into high-quality audio with matching subtitles in seconds. Use it for audiobooks, voiceovers for Instagram, YouTube, TikTok, or any project that needs natural-sounding text-to-speech, using [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M).

<img title="Abogen Main" src='https://raw.githubusercontent.com/denizsafak/abogen/refs/heads/main/demo/abogen.png' width="380"> <img title="Abogen Processing" src='https://raw.githubusercontent.com/denizsafak/abogen/refs/heads/main/demo/abogen2.png' width="380">

## Demo

https://github.com/user-attachments/assets/094ba3df-7d66-494a-bc31-0e4b41d0b865

> This demo was generated in just 5 seconds, producing ∼1 minute of audio with perfectly synced subtitles. To create a similar video, see [the demo guide](https://github.com/denizsafak/abogen/tree/main/demo).

## `How to install?` <a href="https://pypi.org/project/abogen/" target="_blank"><img src="https://img.shields.io/pypi/pyversions/abogen" alt="Abogen Compatible PyPi Python Versions" align="right" style="margin-top:6px;"></a>

### Windows
Go to [espeak-ng latest release](https://github.com/espeak-ng/espeak-ng/releases/latest) download and run the *.msi file.

#### OPTION 1: Install using script
1. [Download](https://github.com/denizsafak/abogen/archive/refs/heads/main.zip) the repository
2. Extract the ZIP file
3. Run `WINDOWS_INSTALL.bat` by double-clicking it

This method handles everything automatically - installing all dependencies including CUDA in a self-contained environment without requiring a separate Python installation. (You still need to install [espeak-ng](https://github.com/espeak-ng/espeak-ng/releases/latest).)

> [!NOTE]
> You don't need to install Python separately. The script will install Python automatically.

#### OPTION 2: Install using pip
```bash
# Create a virtual environment (optional)
mkdir abogen && cd abogen
python -m venv venv
venv\Scripts\activate

# For NVIDIA GPUs:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

# For AMD GPUs:
# Not supported yet, because ROCm is not available on Windows. Use Linux if you have AMD GPU.

# Install abogen
pip install abogen
```

### Mac
```bash
# Install espeak-ng
brew install espeak-ng

# Create a virtual environment (recommended)
mkdir abogen && cd abogen
python3 -m venv venv
source venv/bin/activate

# Install abogen
pip3 install abogen

# For Silicon Mac (M1, M2 etc.)
# After installing abogen, we need to install Kokoro's development version which includes MPS support.
pip3 install git+https://github.com/hexgrad/kokoro.git
```
### Linux
```bash
# Install espeak-ng
sudo apt install espeak-ng # Ubuntu/Debian
sudo pacman -S espeak-ng # Arch Linux
sudo dnf install espeak-ng # Fedora

# Create a virtual environment (recommended)
mkdir abogen && cd abogen
python3 -m venv venv
source venv/bin/activate

# Install abogen
pip3 install abogen

# For NVIDIA GPUs:
# Already supported, no need to install CUDA separately.

# For AMD GPUs:
# After installing abogen, we need to uninstall the existing torch package
pip3 uninstall torch 
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.4
```
> [!TIP]
> If you get `WARNING: The script abogen-cli is installed in '/home/username/.local/bin' which is not on PATH.` error, run the following command to add it to your PATH:
>```bash
>echo "export PATH=\"/home/$USER/.local/bin:\$PATH\"" >> ~/.bashrc && source ~/.bashrc
>```

> [!TIP]
> If you get "No matching distribution found" error, try installing it on supported Python (3.10 to 3.12). You can use [pyenv](https://github.com/pyenv/pyenv) to manage multiple Python versions easily in Linux. Watch this [video](https://www.youtube.com/watch?v=MVyb-nI4KyI) by NetworkChuck for a quick guide.

> Special thanks to [@hg000125](https://github.com/hg000125) for his contribution in [#23](https://github.com/denizsafak/abogen/issues/23). AMD GPU support is possible thanks to his work.

## `How to run?`
If you installed using pip, you can simply run the following command to start Abogen:

```bash
abogen
```
> [!TIP]
> If you installed using the Windows installer `(WINDOWS_INSTALL.bat)`, It should have created a shortcut in the same folder, or your desktop. You can run it from there. If you lost the shortcut, Abogen is located in `python_embedded/Scripts/abogen.exe`. You can run it from there directly.

## `How to use?`
1) Drag and drop any ePub, PDF, or text file (or use the built-in text editor)
2) Configure the settings:
    - Set speech speed
    - Select a voice (or create a custom voice using voice mixer)
    - Select subtitle generation style (by sentence, word, etc.)
    - Select output format
    - Select where to save the output
3) Hit Start

## `In action`
<img title="Abogen in action" src='https://raw.githubusercontent.com/denizsafak/abogen/refs/heads/main/demo/abogen.gif'> 

Here’s Abogen in action: in this demo, it processes ∼3,000 characters of text in just 11 seconds and turns it into 3 minutes and 28 seconds of audio, and I have a low-end **RTX 2060 Mobile laptop GPU**. Your results may vary depending on your hardware.

## `Configuration`

| Options | Description |
|---------|-------------|
| **Input Box** | Drag and drop `ePub`, `PDF`, or `.TXT` files (or use built-in text editor) |
| **Queue options** | Add multiple files to a queue and process them in batch, with individual settings for each file. See [Queue mode](#queue-mode) for more details. |
| **Speed** | Adjust speech rate from `0.1x` to `2.0x` |
| **Select Voice** | First letter of the language code (e.g., `a` for American English, `b` for British English, etc.), second letter is for `m` for male and `f` for female. |
| **Voice mixer** | Create custom voices by mixing different voice models with a profile system. See [Voice Mixer](#voice-mixer) for more details. |
| **Voice preview** | Listen to the selected voice before processing. |
| **Generate subtitles** | `Disabled`, `Sentence`, `Sentence + Comma`, `Sentence + Highlighting`, `1 word`, `2 words`, `3 words`, etc. (Represents the number of words in each subtitle entry) |
| **Output voice format** | `.WAV`, `.FLAC`, `.MP3`, `.OPUS (best compression)` and `M4B (with chapters)` (Special thanks to [@jborza](https://github.com/jborza) for chapter support in PR [#10](https://github.com/denizsafak/abogen/pull/10)) |
| **Output subtitle format** | Configures the subtitle format as `SRT (standard)`, `ASS (wide)`, `ASS (narrow)`, `ASS (centered wide)`, or `ASS (centered narrow)`. |
| **Replace single newlines with spaces** | Replaces single newlines with spaces in the text. This is useful for texts that have imaginary line breaks. |
| **Save location** | `Save next to input file`, `Save to desktop`, or `Choose output folder` |

| Book handler options | Description |
|---------|-------------|
| **Chapter Control** | Select specific `chapters` from ePUBs or `chapters + pages` from PDFs. |
| **Save each chapter separately** | Save each chapter in e-books as a separate audio file. |
| **Create a merged version** | Create a single audio file that combines all chapters. (If `Save each chapter separately` is disabled, this option will be the default behavior.) |
| **Save in a project folder with metadata** | Save the converted items in a project folder with available metadata files. |

| Menu options | Description |
|---------|-------------|
| **Theme** | Change the application's theme using `System`, `Light`, or `Dark` options. |
| **Configure max words per subtitle** | Configures the maximum number of words per subtitle entry. |
| **Configure max lines in log window** | Configures the maximum number of lines to display in the log window. |
| **Separate chapters audio format** | Configures the audio format for separate chapters as `wav`, `flac`, `mp3`, or `opus`. |
| **Create desktop shortcut** | Creates a shortcut on your desktop for easy access. |
| **Open config directory** | Opens the directory where the configuration file is stored. |
| **Open cache directory** | Opens the cache directory where converted text files are stored. |
| **Clear cache files** | Deletes cache files created during the conversion or preview. |
| **Check for updates at startup** | Automatically checks for updates when the program starts. |
| **Disable Kokoro's internet access** | Prevents Kokoro from downloading models or voices from HuggingFace Hub, useful for offline use. |
| **Reset to default settings** | Resets all settings to their default values. |

> Special thanks to [@robmckinnon](https://github.com/robmckinnon) for adding Sentence + Highlighting feature in PR [#65](https://github.com/denizsafak/abogen/pull/65)

## `Voice Mixer`
<img title="Abogen Voice Mixer" src='https://raw.githubusercontent.com/denizsafak/abogen/refs/heads/main/demo/voice_mixer.png'>

With voice mixer, you can create custom voices by mixing different voice models. You can adjust the weight of each voice and save your custom voice as a profile for future use. The voice mixer allows you to create unique and personalized voices. (Huge thanks to [@jborza](https://github.com/jborza) for making this possible through his contributions in [#5](https://github.com/denizsafak/abogen/pull/5))

## `Queue Mode`
<img title="Abogen queue mode" src='https://raw.githubusercontent.com/denizsafak/abogen/refs/heads/main/demo/queue.png'>

Abogen supports **queue mode**, allowing you to add multiple files to a processing queue. This is useful if you want to convert several files in one batch.

- You can add text files (`.txt`) directly using the **Add files** button in the Queue Manager. To add PDF or EPUB files, use the input box in the main window and click the **Add to Queue** button.
- Each file in the queue keeps the configuration settings that were active when it was added. Changing the main window configuration afterward does **not** affect files already in the queue.
- You can view each file's configuration by hovering over them.

Abogen will process each item in the queue automatically, saving outputs as configured.
> Special thanks to [@jborza](https://github.com/jborza) for adding queue mode in PR [#35](https://github.com/denizsafak/abogen/pull/35)

## `About Chapter Markers`
When you process ePUB or PDF files, Abogen converts them into text files stored in your cache directory. When you click "Edit," you're actually modifying these converted text files. In these text files, you'll notice tags that look like this:

```
<<CHAPTER_MARKER:Chapter Title>>
```
These are chapter markers. They are automatically added when you process ePUB or PDF files, based on the chapters you select. They serve an important purpose:
-  Allow you to split the text into separate audio files for each chapter
-  Save time by letting you reprocess only specific chapters if errors occur, rather than the entire file

You can manually add these markers to plain text files for the same benefits. Simply include them in your text like this:

```
<<CHAPTER_MARKER:Introduction>>
This is the beginning of my text...  

<<CHAPTER_MARKER:Main Content>> 
Here's another part...  
```
When you process the text file, Abogen will detect these markers automatically and ask if you want to save each chapter separately and create a merged version.

![Abogen Chapter Marker](https://raw.githubusercontent.com/denizsafak/abogen/refs/heads/main/demo/chapter_marker.png)

## `About Metadata Tags`
Similar to chapter markers, it is possible to add metadata tags for `M4B` files. This is useful for audiobook players that support metadata, allowing you to add information like title, author, year, etc. Abogen automatically adds these tags when you process ePUB or PDF files, but you can also add them manually to your text files. Add metadata tags **at the beginning of your text file** like this:
```
<<METADATA_TITLE:Title>>
<<METADATA_ARTIST:Author>>
<<METADATA_ALBUM:Album Title>>
<<METADATA_YEAR:Year>>
<<METADATA_ALBUM_ARTIST:Album Artist>>
<<METADATA_COMPOSER:Narrator>>
<<METADATA_GENRE:Audiobook>>
```

## `Supported Languages`
```
# 🇺🇸 'a' => American English, 🇬🇧 'b' => British English
# 🇪🇸 'e' => Spanish es
# 🇫🇷 'f' => French fr-fr
# 🇮🇳 'h' => Hindi hi
# 🇮🇹 'i' => Italian it
# 🇯🇵 'j' => Japanese: pip install misaki[ja]
# 🇧🇷 'p' => Brazilian Portuguese pt-br
# 🇨🇳 'z' => Mandarin Chinese: pip install misaki[zh]
```
For a complete list of supported languages and voices, refer to Kokoro's [VOICES.md](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md). To listen to sample audio outputs, see [SAMPLES.md](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/SAMPLES.md).

> [!NOTE]
> Japanese audio may require additional configuration. Please check [#56](https://github.com/denizsafak/abogen/issues/56) for more information.

## `MPV Config`
I highly recommend using [MPV](https://mpv.io/installation/) to play your audio files, as it supports displaying subtitles even without a video track. Here's my `mpv.conf`:
```
# --- MPV Settings ---
save-position-on-quit
keep-open=yes
# --- Subtitle ---
sub-ass-override=no
sub-margin-y=50
sub-margin-x=50
# --- Audio Quality ---
audio-spdif=ac3,dts,eac3,truehd,dts-hd
audio-channels=auto
audio-samplerate=48000
volume-max=200
```

## `Docker Guide`
If you want to run Abogen in a Docker container:
1) [Download the repository](https://github.com/denizsafak/abogen/archive/refs/heads/main.zip) and extract, or clone it using git.
2) Go to `abogen` folder. You should see `Dockerfile` there.
3) Open your termminal in that directory and run the following commands:

```bash
# Build the Docker image:
docker build --progress plain -t abogen .

# Note that building the image may take a while.
# After building is complete, run the Docker container:

# Windows
docker run --name abogen -v %cd%:/shared -p 5800:5800 -p 5900:5900 --gpus all abogen

# Linux
docker run --name abogen -v $(pwd):/shared -p 5800:5800 -p 5900:5900 --gpus all abogen

# MacOS
docker run --name abogen -v $(pwd):/shared -p 5800:5800 -p 5900:5900 abogen

# We expose port 5800 for use by a web browser, 5900 if you want to connect with a VNC client.
```

Abogen launches automatically inside the container. 
- You can access it via a web browser at [http://localhost:5800](http://localhost:5800) or connect to it using a VNC client at `localhost:5900`.
- You can use `/shared` directory to share files between your host and the container.
- For later use, start it with `docker start abogen` and stop it with `docker stop abogen`.

Known issues:
- Audio preview is not working inside container (ALSA error).
- `Open cache directory` and `Open configuration directory` options in settings not working. (Tried pcmanfm, did not work with Abogen).

(Special thanks to [@geo38](https://www.reddit.com/user/geo38/) from Reddit, who provided the Dockerfile and instructions in [this comment](https://www.reddit.com/r/selfhosted/comments/1k8x1yo/comment/mpe0bz8/).)

## `Similar Projects`
Abogen is a standalone project, but it is inspired by and shares some similarities with other projects. Here are a few:
- [audiblez](https://github.com/santinic/audiblez): Generate audiobooks from e-books. **(Has CLI and GUI support)**
- [autiobooks](https://github.com/plusuncold/autiobooks): Automatically convert epubs to audiobooks
- [pdf-narrator](https://github.com/mateogon/pdf-narrator): Convert your PDFs and EPUBs into audiobooks effortlessly.
- [epub_to_audiobook](https://github.com/p0n1/epub_to_audiobook): EPUB to audiobook converter, optimized for Audiobookshelf
- [ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook): Convert ebooks to audiobooks with chapters and metadata using dynamic AI models and voice cloning

## `Roadmap`
- [ ] Add OCR scan feature for PDF files using docling/teserract.
- [x] Add chapter metadata for .m4a files. (Issue [#9](https://github.com/denizsafak/abogen/issues/9), PR [#10](https://github.com/denizsafak/abogen/pull/10))
- [ ] Add support for different languages in GUI.
- [x] Add voice formula feature that enables mixing different voice models. (Issue [#1](https://github.com/denizsafak/abogen/issues/1), PR [#5](https://github.com/denizsafak/abogen/pull/5))
- [ ] Add support for kokoro-onnx (If it's necessary).
- [x] Add dark mode.

## `Troubleshooting`
If you encounter any issues while running Abogen, try launching it from the command line with:
```
abogen-cli
```
This will start Abogen in command-line mode and display detailed error messages. Please open a new issue on the [Issues](https://github.com/denizsafak/abogen/issues) page with the error message and a description of your problem.

## `Contributing`
I welcome contributions! If you have ideas for new features, improvements, or bug fixes, please fork the repository and submit a pull request.
### For developers and contributors
If you'd like to modify the code and contribute to development, you can [download the repository](https://github.com/denizsafak/abogen/archive/refs/heads/main.zip), extract it and run the following commands to build **or** install the package:
```bash
# Go to the directory where you extracted the repository and run:
pip install -e .      # Installs the package in editable mode
pip install build     # Install the build package
python -m build       # Builds the package in dist folder (optional)
abogen                # Opens the GUI
```
Feel free to explore the code and make any changes you like.

## `Credits`
- Abogen uses [Kokoro](https://github.com/hexgrad/kokoro) for its high-quality, natural-sounding text-to-speech synthesis. Huge thanks to the Kokoro team for making this possible.
- Thanks to [@wojiushixiaobai](https://github.com/wojiushixiaobai) for [Embedded Python](https://github.com/wojiushixiaobai/Python-Embed-Win64) packages. These modified packages include pip pre-installed, enabling Abogen to function as a standalone application without requiring users to separately install Python in Windows.
- Thanks to creators of [EbookLib](https://github.com/aerkalov/ebooklib), a Python library for reading and writing ePub files, which is used for extracting text from ePub files.
- Special thanks to the [PyQt](https://www.riverbankcomputing.com/software/pyqt/) team for providing the cross-platform GUI toolkit that powers Abogen's interface.
- Icons: [US](https://icons8.com/icon/aRiu1GGi6Aoe/usa), [Great Britain](https://icons8.com/icon/t3NE3BsOAQwq/great-britain), [Spain](https://icons8.com/icon/ly7tzANRt33n/spain), [France](https://icons8.com/icon/3muzEmi4dpD5/france), [India](https://icons8.com/icon/esGVrxg9VCJ1/india), [Italy](https://icons8.com/icon/PW8KZnP7qXzO/italy), [Japan](https://icons8.com/icon/McQbrq9qaQye/japan), [Brazil](https://icons8.com/icon/zHmH8HpOmM90/brazil), [China](https://icons8.com/icon/Ej50Oe3crXwF/china), [Female](https://icons8.com/icon/uI49hxbpxTkp/female), [Male](https://icons8.com/icon/12351/male), [Adjust](https://icons8.com/icon/21698/adjust) and [Voice Id](https://icons8.com/icon/GskSeVoroQ7u/voice-id) icons by [Icons8](https://icons8.com/).

## `License`
This project is available under the MIT License - see the [LICENSE](https://github.com/denizsafak/abogen/blob/main/LICENSE) file for details.
[Kokoro](https://github.com/hexgrad/kokoro) is licensed under [Apache-2.0](https://github.com/hexgrad/kokoro/blob/main/LICENSE) which allows commercial use, modification, distribution, and private use.

> [!IMPORTANT]
> Subtitle generation currently works only for English. This is because Kokoro provides timestamp tokens only for English text. If you want subtitles in other languages, please request this feature in the [Kokoro project](https://github.com/hexgrad/kokoro). For more technical details, see [this line](https://github.com/hexgrad/kokoro/blob/6d87f4ae7abc2d14dbc4b3ef2e5f19852e861ac2/kokoro/pipeline.py#L383) in the Kokoro's code.

> Tags: audiobook, kokoro, text-to-speech, TTS, audiobook generator, audiobooks, text to speech, audiobook maker, audiobook creator, audiobook generator, voice-synthesis, text to audio, text to audio converter, text to speech converter, text to speech generator, text to speech software, text to speech app, epub to audio, pdf to audio, content-creation, media-generation
