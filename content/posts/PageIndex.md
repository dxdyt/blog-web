---
title: PageIndex
date: 2025-11-04T12:23:02+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1761872936185-4ece7c1128ab?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjIyMzAwOTN8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1761872936185-4ece7c1128ab?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NjIyMzAwOTN8&ixlib=rb-4.1.0
---

# [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)

<div align="center">
  
<a href="https://vectify.ai/pageindex" target="_blank">
  <img src="https://github.com/user-attachments/assets/46201e72-675b-43bc-bfbd-081cc6b65a1d" alt="PageIndex Banner" />
</a>

<br/>
<br/>

<p align="center">
  <a href="https://trendshift.io/repositories/14736" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14736" alt="VectifyAI%2FPageIndex | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center"><i>Reasoning-based RAG&nbsp; ◦ &nbsp;No Vector DB&nbsp; ◦ &nbsp;No Chunking&nbsp; ◦ &nbsp;Human-like Retrieval</i></p>

<h4 align="center">
  <a href="https://vectify.ai">🏠 Homepage</a>&nbsp; • &nbsp;
  <a href="https://chat.pageindex.ai">🚀 Agent</a>&nbsp; • &nbsp;
  <a href="https://pageindex.ai/mcp">🔌 MCP</a>&nbsp; • &nbsp;
  <a href="https://dash.pageindex.ai">🖥️ Dashboard</a>&nbsp; • &nbsp;
  <a href="https://docs.pageindex.ai/quickstart">📚 API</a>&nbsp; • &nbsp;
  <a href="https://discord.com/invite/VuXuf29EUj">💬 Discord</a>&nbsp; • &nbsp;
  <a href="https://ii2abc2jejf.typeform.com/to/tK3AXl8T">✉️ Contact</a>&nbsp;
</h4>
  
</div>

---

### 🚨 **New Releases:** 
- 📑 [PageIndex Chat](https://chat.pageindex.ai): The world's first human-like document analyst agent, designed for professional long documents.
- 🔌 [PageIndex MCP](https://github.com/VectifyAI/pageindex-mcp): Bring PageIndex into Claude, Cursor, or any MCP-enabled agents. Chat to long PDFs the human-like, reasoning-based way 📖

# 📄 Introduction to PageIndex

Are you frustrated with vector database retrieval accuracy for long professional documents? Traditional vector-based RAG relies on semantic *similarity* rather than true *relevance*. But **similarity ≠ relevance** — what we truly need in retrieval is **relevance**, and that requires **reasoning**. When working with professional documents that demand domain expertise and multi-step reasoning, similarity search often falls short.

Inspired by AlphaGo, we propose **[PageIndex](https://vectify.ai/pageindex)**, a **reasoning-based RAG** system that builds a tree index over long documents and reasons over that index for retrieval. It simulates how **human experts** navigate and extract knowledge from long documents through **tree search**, enabling LLMs to *think* and *reason* their way to the most relevant document sections. It performs retrieval in two steps:

1. Generate a "Table-of-Contents" **tree structure index** of documents
2. Perform reasoning-based retrieval through **tree search**

<div align="center">
    <img src="https://docs.pageindex.ai/images/cookbook/vectorless-rag.png" width="90%">
</div>

### 💡 Features 

Compared to traditional vector-based RAG, PageIndex features:
- **No Vectors Needed**: Uses document structure and LLM reasoning for retrieval.
- **No Chunking Needed**: Documents are organized into natural sections, not artificial chunks.
- **Human-like Retrieval**: Simulates how human experts navigate and extract knowledge from complex documents.
- **Transparent Retrieval Process**: Retrieval based on reasoning — say goodbye to approximate vector search ("vibe retrieval").

PageIndex powers a reasoning-based RAG system that achieved [98.7% accuracy](https://github.com/VectifyAI/Mafin2.5-FinanceBench) on FinanceBench, showing state-of-the-art performance in professional document analysis (see our [blog post](https://vectify.ai/blog/Mafin2.5) for details).

### ⚙️ Deployment Options
- 🛠️ Self-host — run locally with this open-source repo
- ☁️ **[Cloud Service](https://dash.pageindex.ai/)** — try instantly with our 🚀 [Agent](https://chat.pageindex.ai/), 🖥️ [Dashboard](https://dash.pageindex.ai/) or 🔌 [API](https://docs.pageindex.ai/quickstart), no setup required

### ⚡ Quick Hands-on

Check out this simple [*Vectorless RAG Notebook*](https://github.com/VectifyAI/PageIndex/blob/main/cookbook/pageindex_RAG_simple.ipynb) — a minimal, hands-on, reasoning-based RAG pipeline using **PageIndex**.
<p align="center">
<a href="https://colab.research.google.com/github/VectifyAI/PageIndex/blob/main/cookbook/pageindex_RAG_simple.ipynb">
    <img src="https://img.shields.io/badge/Open_In_Colab-Vectorless_RAG_With_PageIndex-orange?style=for-the-badge&logo=googlecolab" alt="Open in Colab"/>
  </a>
</p>

---

# 📦 PageIndex Tree Structure
PageIndex can transform lengthy PDF documents into a semantic **tree structure**, similar to a _"table of contents"_ but optimized for use with Large Language Models (LLMs). It's ideal for: financial reports, regulatory filings, academic textbooks, legal or technical manuals, and any document that exceeds LLM context limits.

Here is an example output. See more [example documents](https://github.com/VectifyAI/PageIndex/tree/main/tests/pdfs) and [generated trees](https://github.com/VectifyAI/PageIndex/tree/main/tests/results).

```
...
{
  "title": "Financial Stability",
  "node_id": "0006",
  "start_index": 21,
  "end_index": 22,
  "summary": "The Federal Reserve ...",
  "nodes": [
    {
      "title": "Monitoring Financial Vulnerabilities",
      "node_id": "0007",
      "start_index": 22,
      "end_index": 28,
      "summary": "The Federal Reserve's monitoring ..."
    },
    {
      "title": "Domestic and International Cooperation and Coordination",
      "node_id": "0008",
      "start_index": 28,
      "end_index": 31,
      "summary": "In 2023, the Federal Reserve collaborated ..."
    }
  ]
}
...
```

 You can either generate the PageIndex tree structure with this open-source repo or try our ☁️ **[Cloud Service](https://dash.pageindex.ai/)** — instantly accessible via our 🚀 [Agent](https://chat.pageindex.ai/), 🖥️ [Dashboard](https://dash.pageindex.ai/) or 🔌 [API](https://docs.pageindex.ai/quickstart), with no setup required.

---

# Package Usage

You can follow these steps to generate a PageIndex tree from a PDF document.

### 1. Install dependencies

```bash
pip3 install --upgrade -r requirements.txt
```

### 2. Set your OpenAI API key

Create a `.env` file in the root directory and add your API key:

```bash
CHATGPT_API_KEY=your_openai_key_here
```

### 3. Run PageIndex on your PDF

```bash
python3 run_pageindex.py --pdf_path /path/to/your/document.pdf
```

<details>
<summary><strong>Optional parameters</strong></summary>
<br>
You can customize the processing with additional optional arguments:

```
--model                 OpenAI model to use (default: gpt-4o-2024-11-20)
--toc-check-pages       Pages to check for table of contents (default: 20)
--max-pages-per-node    Max pages per node (default: 10)
--max-tokens-per-node   Max tokens per node (default: 20000)
--if-add-node-id        Add node ID (yes/no, default: yes)
--if-add-node-summary   Add node summary (yes/no, default: yes)
--if-add-doc-description Add doc description (yes/no, default: yes)
```
</details>

<details>
<summary><strong>Markdown support</strong></summary>
<br>
We also provide a markdown support for PageIndex. You can use the `-md` flag to generate a tree structure for a markdown file.

```bash
python3 run_pageindex.py --md_path /path/to/your/document.md
```

> Notice: in this function, we use "#" to determine node heading and their levels. For example, "##" is level 2, "###" is level 3, etc. Make sure your markdown file is formatted correctly. If your Markdown file was converted from a PDF or HTML, we don’t recommend using this function, since most existing conversion tools cannot preserve the original hierarchy. Instead, use our [PageIndex OCR](https://pageindex.ai/blog/ocr), which is designed to preserve the original hierarchy, to convert the PDF to a markdown file and then use this function.
</details>

---

# ☁️ Improved Tree Generation with PageIndex OCR

This repo is designed for generating PageIndex tree structure for simple PDFs, but many real-world use cases involve complex PDFs that are hard to parsed by classic python tools. However, extracting high-quality text from PDF documents remains a non-trivial challenge. Most OCR tools only extract page-level content, losing the broader document context and hierarchy.

To address this, we introduced PageIndex OCR — the first long-context OCR model designed to preserve the global structure of documents. PageIndex OCR significantly outperforms other leading OCR tools, such as those from Mistral and Contextual AI, in recognizing true hierarchy and semantic relationships across document pages.

- Experience next-level OCR quality with PageIndex OCR at our [Dashboard](https://dash.pageindex.ai/).
- Integrate seamlessly PageIndex OCR into your stack via our [API](https://docs.pageindex.ai/quickstart).

<p align="center">
  <img src="https://github.com/user-attachments/assets/eb35d8ae-865c-4e60-a33b-ebbd00c41732" width="90%">
</p>

---

# 📈 Case Study: Mafin 2.5 on FinanceBench

[Mafin 2.5](https://vectify.ai/mafin) is a state-of-the-art reasoning-based RAG model designed specifically for financial document analysis. Powered by **PageIndex**, it achieved a market-leading [**98.7% accuracy**](https://vectify.ai/blog/Mafin2.5) on the [FinanceBench](https://arxiv.org/abs/2311.11944) benchmark — significantly outperforming traditional vector-based RAG systems.

PageIndex's hierarchical indexing enabled precise navigation and extraction of relevant content from complex financial reports, such as SEC filings and earnings disclosures.

👉 See the full [benchmark results](https://github.com/VectifyAI/Mafin2.5-FinanceBench) and our [blog post](https://vectify.ai/blog/Mafin2.5) for detailed comparisons and performance metrics.

<div align="center">
  <a href="https://github.com/VectifyAI/Mafin2.5-FinanceBench">
    <img src="https://github.com/user-attachments/assets/571aa074-d803-43c7-80c4-a04254b782a3" width="90%">
  </a>
</div>

---

# 🔎 Learn More about PageIndex

### Resources & Guides

- 📖 Explore our [Tutorials](https://docs.pageindex.ai/doc-search) for practical guides and strategies, including *Document Search* and *Tree Search*.  
- 🧪 Browse the [Cookbook](https://docs.pageindex.ai/cookbook/vectorless-rag-pageindex) for practical recipes and advanced use cases.  
- ⚙️ Refer to the [API Documentation](https://docs.pageindex.ai/quickstart) for integration details and configuration options.

### ⭐ Support Us

Leave a star if you like our project. Thank you!  

<p>
  <img src="https://github.com/user-attachments/assets/eae4ff38-48ae-4a7c-b19f-eab81201d794" width="60%">
</p>

### Connect with Us

[![Twitter](https://img.shields.io/badge/Twitter-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/VectifyAI)&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/vectify-ai/)&nbsp;
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/VuXuf29EUj)&nbsp;
[![Contact Us](https://img.shields.io/badge/Contact_Us-3B82F6?style=for-the-badge&logo=envelope&logoColor=white)](https://ii2abc2jejf.typeform.com/to/tK3AXl8T)

---

© 2025 [Vectify AI](https://vectify.ai)
