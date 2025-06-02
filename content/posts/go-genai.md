---
title: go-genai
date: 2025-06-02T12:31:17+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1747807112079-7ac448e26968?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDg4Mzg1NTZ8&ixlib=rb-4.1.0
featuredImagePreview: https://images.unsplash.com/photo-1747807112079-7ac448e26968?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NDg4Mzg1NTZ8&ixlib=rb-4.1.0
---

# [googleapis/go-genai](https://github.com/googleapis/go-genai)

![GitHub go.mod Go version](https://img.shields.io/github/go-mod/go-version/googleapis/go-genai)
[![Go Reference](https://pkg.go.dev/badge/google.golang.org/genai.svg)](https://pkg.go.dev/google.golang.org/genai)

## ✨ NEW ✨

### Google Gemini Multimodal Live support

Introducing support for the Gemini Multimodal Live feature. Here's an example
Multimodal Live server showing realtime conversation and video streaming:
[code](./examples/live/live_streaming_server.go)

# Google Gen AI Go SDK

The Google Gen AI Go SDK provides an interface for developers to integrate
Google's generative models into their Go applications. It supports the
[Gemini Developer API](https://ai.google.dev/gemini-api/docs) and
[Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
APIs.

The Google Gen AI Go SDK enables developers to use Google's state-of-the-art
generative AI models (like Gemini) to build AI-powered features and applications.
This SDK supports use cases like:
- Generate text from text-only input
- Generate text from text-and-images input (multimodal)
- ...

For example, with just a few lines of code, you can access Gemini's multimodal
capabilities to generate text from text-and-image input.

```go
parts := []*genai.Part{
  {Text: "What's this image about?"},
  {InlineData: &genai.Blob{Data: imageBytes, MIMEType: "image/jpeg"}},
}
result, err := client.Models.GenerateContent(ctx, "gemini-2.0-flash", []*genai.Content{{Parts: parts}}, nil)
```

## Installation and usage

Add the SDK to your module with `go get google.golang.org/genai`.

## Create Clients

### Imports
```go
import "google.golang.org/genai"
```

### Gemini API Client:
```go
client, err := genai.NewClient(ctx, &genai.ClientConfig{
	APIKey:   apiKey,
	Backend:  genai.BackendGeminiAPI,
})
```

### Vertex AI Client:
```go
client, err := genai.NewClient(ctx, &genai.ClientConfig{
	Project:  project,
	Location: location,
	Backend:  genai.BackendVertexAI,
})
```

## License

The contents of this repository are licensed under the
[Apache License, version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
