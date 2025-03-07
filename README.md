# Gemini Agent
Demo Project: Enhance Gemini API Integrations in OSS Agents Tools

![GitHub stars](https://img.shields.io/github/stars/ajitashwathr10/gemini-agent?style=social)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)

## 🚀 Overview

**Gemini Agent** is a light-weight, demo based research assistant AI that leverages Google's Gemini Large Language Model using the LangChain framework. This work illustrates how to construct an intelligent agent that can execute sophisticated research tasks, information extraction, and knowledge synthesis.

## 🔍 Key Features

- **Gemini-Powered Intelligence**: Leverages Google's state-of-the-art Gemini LLM for human-like reasoning
- **Multi-Tool Architecture**: Combines search, summarization, and knowledge tools in a unified agent
- **FastAPI Backend**: Responsive, well-documented API with minimal latency
- **Minimalist Design**: Clean, production-ready code with no unnecessary complexity

## 🛠️ Quick Start

```bash
# Clone the repository
git clone https://github.com/ajitashwathr10/gemini-agent.git
cd gemini-agent

# Install dependencies
pip install -r requirements.txt

# Set your Google API key
echo "GOOGLE_API_KEY = your_api_key_here" .env

# Run the application
python main.py
```

## 📊 Example Usage

```python
import requests

response = requests.post(
    "http://localhost:8000/research",
    json = {"query": "What are the latest advancements in Google Gemini?"}
)

print(response.json()["answer"])
```

## 🧠 How It Works

Gemini operates as a reasoning system that:

1. **Understands** the user's research query
2. **Plans** a strategy to gather relevant information
3. **Executes** actions using specialized tools
4. **Synthesizes** findings into a coherent, insightful response

This project was specifically developed to demonstrate capability and interest in Google DeepMind's GSOC 2025 "Enhance Gemini API Integrations in OSS Agents Tools" initiative.
---
