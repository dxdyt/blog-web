---
title: mcp
date: 2025-08-31T12:20:39+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1754231304863-dac7fcbe86dd?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTY2MTQwMTh8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1754231304863-dac7fcbe86dd?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTY2MTQwMTh8&ixlib=rb-4.1.0
---

# [microsoft/mcp](https://github.com/microsoft/mcp)

# Microsoft Model Context Protocol (MCP) Servers

This repository catalogs various Microsoft implementations of the Model Context Protocol (MCP), an open standard that facilitates seamless integration between AI applications and external data sources and tools. MCP enables AI models to access the context they need to perform tasks effectively.

---

## 📘 What is MCP?

**Model Context Protocol (MCP)** is an open protocol that standardizes how applications provide context to large language models (LLMs). It allows AI applications to connect with various data sources and tools in a consistent manner, enhancing their capabilities and flexibility. MCP follows a client-server architecture where:

- **MCP Hosts**: Applications like AI assistants or integrated development environments (IDEs) that initiate connections.
- **MCP Clients**: Connectors within the host application that maintain 1:1 connections with servers.
- **MCP Servers**: Services that provide context and capabilities through the standardized MCP.

For more details, visit the [official MCP website](https://modelcontextprotocol.io).

---

## 📂 Microsoft MCP Servers

Below are Microsoft's official MCP server implementations:

### 📅 Azure DevOps MCP Server

- **Repository**: [Azure DevOps MCP Server - Public Preview](https://github.com/microsoft/azure-devops-mcp)
- **Description**: The MCP Server for Azure DevOps enables you to bring context into AI workflows and interact with Azure DevOps artifacts such as work items, test plans, builds, releases, and pull requests.

---

### 🔷 Azure MCP Server

- **Repository**: [microsoft/mcp](https://github.com/microsoft/mcp/tree/main/servers/Azure.Mcp.Server#readme)
- **Description**: Implements the MCP standard to manage Azure resources, enabling declarative provisioning and integration with AI workflows.

---

### ✨ Azure AI Foundry MCP Server

- **Repository**: [azure-ai-foundry/mcp-foundry](https://github.com/azure-ai-foundry/mcp-foundry)
- **Description**: An experimental MCP server implementation for Azure AI Foundry that exposes unified tools for models, knowledge, evaluation and deployment.

---

### 📊 Clarity MCP Server

- **Repository**: [@microsoft/clarity-mcp-server](https://www.npmjs.com/package/@microsoft/clarity-mcp-server)
- **Description**: An MCP server for Microsoft Clarity analytics integration. Enables AI models to access web analytics data, heatmaps, and session recordings to understand user behavior and site performance.

---

### 🗃️ Dataverse MCP Server

- **Documentation**: [Microsoft Dataverse](https://go.microsoft.com/fwlink/?linkid=2320176)
- **Description**: Chat over your business data using NL - Discover tables, run queries, retrieve data, insert or update records, and execute custom prompts grounded in business knowledge and context.
---

### 📁 Files MCP Server

- **Repository**: [microsoft/files-mcp-server](https://github.com/microsoft/files-mcp-server)
- **Description**: Provides a declarative control plane for managing file-based resources, supporting AI workflows that involve static files and documentation synchronization.

---

### 📝 Markitdown MCP Server

- **Repository**: [microsoft/markitdown](https://github.com/microsoft/markitdown)
- **Description**: A specialized MCP server for Markdown processing and manipulation. Enables AI models to read, write, and transform Markdown content with robust parsing and formatting capabilities.

---

### 💻 Microsoft Dev Box MCP

- **Package**: [@microsoft/devbox-mcp](https://www.npmjs.com/package/@microsoft/devbox-mcp)
- **Description**: An MCP server for [Microsoft Dev Box](https://azure.microsoft.com/products/dev-box). Enables natural language interactions for developer-focused operations like managing Dev Boxes, configuring environments, and handling pools. Check out the [README](https://www.npmjs.com/package/@microsoft/devbox-mcp?activeTab=readme) for more details. Use this [one-click link](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fdevbox-mcp%40latest%22%5D%7D) to install Dev Box MCP in your VS Code.

---

### 🛢️Microsoft Fabric Real-Time Intelligence MCP Server

- **Repository**: [RTI MCP Server](https://aka.ms/rti.mcp.repo)
- **Description**: Chat with your real-time data the new agentic way using natural language and AI. MCP server for [Fabric Real-Time Intelligence](https://aka.ms/fabricrti) supporting tools for [Eventhouse](https://aka.ms/eventhouse), [Azure Data Explorer](https://aka.ms/adx), and other RTI services (coming soon)

---

### 📚 Microsoft Learn Docs MCP Server

- **Repository**: [microsoftdocs/mcp](https://github.com/microsoftdocs/mcp)
- **Description**: A remote MCP server that provides structured access to official Microsoft Learn documentation. Enables AI models to retrieve accurate, authoritative, and context-aware technical content for code generation, question answering, and workflow grounding.

---

### 🛢️Microsoft SQL MCP Server

- **Repository**: [MSSQL MCP Server](https://aka.ms/MssqlMcp)
- **Description**: Chat with your business data the new agentic way using natural language and AI. Connect to any SQL database—from ground (on-premises) to Azure cloud to Microsoft Fabric via a simple connection string. Discover and define table schemas, manage tables, and perform CRUD operations through conversational prompts.

---

### 🎭 Playwright MCP

- **Repository**: [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)
- **Description**: An MCP server for browsing the internet. Enables LLMs to interact with web pages through structured accessibility snapshots. Useful for web navigation and form-filling, data extraction from structured content, automated testing driven by LLMs, and general-purpose browser interaction for agents.

---

### ☸️ Azure Kubernetes Service (AKS) MCP Server

- **Repository**: [Azure/aks-mcp](https://github.com/Azure/aks-mcp)
- **Description**: An MCP server that enables AI assistants to interact with Azure Kubernetes Service (AKS) clusters. It serves as a bridge between AI tools and AKS, translating natural language requests into AKS operations and returning the results in a format the AI tools can understand.

---

### 📚 Microsoft 365 Agents Toolkit MCP

- **Repository**: [M365 Agents Toolkit MCP](https://aka.ms/m365agentstoolkit-mcp)
- **Description**: An MCP server that provides a seamless connection between AI agents and developers for building apps and agents for Microsoft 365 and Microsoft 365 Copilot.

---

## 📎 Related Resources

- [Microsoft MCP Resources](https://github.com/microsoft/mcp/tree/main/Resources)
- [MCP Pattern Overview](https://modelcontextprotocol.io/introduction)
- [MCP SDKs and Building Blocks](https://modelcontextprotocol.io/sdk)
- [MCP Specification](https://spec.modelcontextprotocol.io/specification/2025-03-26/)

---

## 🏗️ Templates

Looking for starter templates that use MCP? Check out the [Azure Developer CLI (azd) templates](https://azure.github.io/awesome-azd/?tags=mcp) tagged with MCP.

---

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
