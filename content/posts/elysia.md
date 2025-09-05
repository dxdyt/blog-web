---
title: elysia
date: 2025-09-05T12:22:09+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1756786605292-f6b83d2157aa?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTcwNDYwNDh8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1756786605292-f6b83d2157aa?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTcwNDYwNDh8&ixlib=rb-4.1.0
---

# [weaviate/elysia](https://github.com/weaviate/elysia)

# Elysia: Agentic Framework Powered by Decision Trees

> **⚠️ Elysia is in beta!**
>
> If you encounter any issues, please [open an issue on GitHub](https://github.com/weaviate/elysia/issues).

[![PyPI Downloads](https://static.pepy.tech/badge/elysia-ai)](https://pepy.tech/projects/elysia-ai) [![Demo](https://img.shields.io/badge/Check%20out%20the%20demo!-yellow?&style=flat-square&logo=react&logoColor=white)](https://elysia.weaviate.io/)

Elysia is an agentic platform designed to use tools in a decision tree. A decision agent decides which tools to use dynamically based on its environment and context. You can use custom tools or use the pre-built tools designed to retrieve your data in a Weaviate cluster.

[Read the docs!](https://weaviate.github.io/elysia/)

Installation is as simple as:
```bash
pip install elysia-ai
```

## Get started (App)

Run the app via

```bash
elysia start
```
Then navigate to the settings page, add your required API keys, Weaviate cloud cluster details and specify your models.

Don't forget to check out [the Github Repository for the Frontend](https://github.com/weaviate/elysia-frontend)!

Alternatively, we have created a demo version of Elysia (rate-limited, fixed datasets) to experiment with. Find it at: https://elysia.weaviate.io/

## Get Started (Python)

To use Elysia, you need to either set up your models and API keys in your `.env` file, or specify them in the config. [See the setup page to get started.](https://weaviate.github.io/elysia/setting_up/)

Elysia can be used very simply:
```python
from elysia import tool, Tree

tree = Tree()

@tool(tree=tree)
async def add(x: int, y: int) -> int:
    return x + y

tree("What is the sum of 9009 and 6006?")
```

Elysia is pre-configured to be capable of connecting to and interacting with your [Weaviate](https://weaviate.io/deployment/serverless) clusters!
```python
import elysia
tree = elysia.Tree()
response, objects = tree(
    "What are the 10 most expensive items in the Ecommerce collection?",
    collection_names = ["Ecommerce"]
)
```
This will use the built-in open source _query_ tool or _aggregate_ tool to interact with your Weaviate collections. To get started connecting to Weaviate, [see the setting up page in the docs](https://weaviate.github.io/elysia/setting_up/).

## Installation (bash) (Linux/MacOS)

### PyPi (Recommended)

Elysia requires Python 3.12:
- [Installation via brew (macOS)](https://formulae.brew.sh/formula/python@3.12)
- [Installation via installer (Windows)](https://www.python.org/downloads/release/python-3120/)
- [Installation (Ubuntu)](https://ubuntuhandbook.org/index.php/2023/05/install-python-3-12-ubuntu/)

Optionally create a virtual environment via
```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Then simply run 
```bash
pip install elysia-ai
```
to install straight away!

### GitHub

To get the latest development version, you can clone the github repo by running
```bash
git clone https://github.com/weaviate/elysia
```
move to the working directory via
```bash
cd elysia
```
Create a virtual environment with Python (version 3.10 - 3.12)
```bash
python3.12 -m venv .venv
source .venv/bin/activate
```
and then install Elysia via pip
```bash
pip install -e .
```
Done! You can now use the Elysia python package


### Configuring Settings

To use Elysia with Weaviate, i.e. for agentic searching and retrieval, you need a Weaviate cluster api key and URL. This can be specific in the app directly, or by creating a `.env` file with
```
WCD_URL=...
WCD_API_KEY=...
```
Elysia will automatically detect these when running locally, and this will be the default Weaviate cluster for all users logging into the Elysia app. But these can be configured on a user-by-user basis through the config.

Whichever vectoriser you use for your Weaviate collection you will need to specify your corresponding API key, e.g.
```
OPENAI_API_KEY=...
```
These will automatically be added to the headers for the Weaviate client.

Same for whichever model you choose for the LLM in Elysia, so if you are using GPT-4o, for example, specify an `OPENAI_API_KEY`.

Elysia's recommended config is to use [OpenRouter](https://openrouter.ai/) to give easy access to a variety of models. So this requires
```
OPENROUTER_API_KEY=...
```

## FAQ

<details>
<summary><b>How do I use Elysia with my own data?</b></summary>

You can connect to your own Weaviate cloud cluster, which will automatically identify any collections that exist in the cluster.

Collections require being _preprocessed_ for Elysia. In the app, you just click the 'analyze' button in the Data tab. In Python you can do:

```python
from elysia.preprocessing.collection import preprocess

preprocess(collection_names=["YourCollectionName"])
```

</details>

<details>
<summary><b>Can I use a locally running version of Weaviate such as with Docker?</b></summary>
Locally running versions of Weaviate are currently not implemented in the current version of the app but this is planned for a future release. Stay tuned!
</details>


<details>
<summary><b>How do I clear all my Elysia data?</b></summary>

Everything Elysia doesn't store locally will be a collection in your Weaviate cluster. You can delete any collections that start with `ELYSIA_` to reset all your Elysia data.

For example, in Python:
```python
from elysia.util.client import ClientManager()
with ClientManager().connect_to_client() as client:
    for collection_name in client.collections.list_all():
        if collection_name.startswith("ELYSIA_"):
            client.collections.delete(collection_name)
```
</details>


<details>

<summary><b>Can I contribute to Elysia?</b></summary>

Elysia is **fully open source**, so yes of course you can! Clone and create a new branch of Elysia via
```bash
git clone https://github.com/weaviate/elysia
git checkout -b <branch_name>
```
Make your changes, push them to your branch, go to GitHub and submit a pull request.

</details>


<details>
<summary><b>Where is the best place I can start contributing?</b></summary>

There are no 'huge' new features we are planning for Elysia (for the moment). You could start with creating a new tool, or multiple new tools to create a custom workflow for something specific. Look for pain points you experience from your user journey and find what exactly is causing these. Then try to fix them or create an alternative way of doing things!

</details>

