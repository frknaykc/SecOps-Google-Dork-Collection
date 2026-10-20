# AI, LLM & MLOps Google Dorks

A curated collection of Google Dork queries for discovering exposed Artificial Intelligence (AI) platforms, Large Language Model (LLM) endpoints, inference servers (NVIDIA Triton, TGI, Ollama), image generation engines (ComfyUI, Stable Diffusion), MLOps tracking servers, Vector Databases, and leaked AI API credentials.

## Summary

| Risk Level | Count |
|---|---:|
| Critical | 27 |
| High | 22 |
| Medium | 4 |
| Low | 51 |

**Total: 104 dorks**

Risk levels prioritize search leads; a matching result is not proof of a vulnerability or unauthorized access.

## Coverage

| Platform / Area | Description |
|-----------------|-------------|
| **LLM Inference Engines & Serving** | NVIDIA Triton, HuggingFace TGI, Ollama, vLLM, LocalAI, LM Studio, LiteLLM |
| **AI Web UIs & Chat Platforms** | LibreChat, Open WebUI, Text Generation WebUI, AnythingLLM, FastGPT |
| **Image & Multimodal Generators** | ComfyUI, Automatic1111 Stable Diffusion WebUI, Fooocus |
| **Agent & Workflow Builders** | Flowise, Dify, LangFlow, and A2A Agent Card discovery |
| **MLOps & Orchestration** | MLflow, Ray Dashboard, Kubeflow, Weights & Biases, JupyterLab |
| **Vector Databases (RAG Storage)** | Qdrant Web UI & API, ChromaDB, Milvus Attu, Weaviate Console |
| **Leaked AI API Keys** | DeepSeek, OpenAI (`sk-proj-`), Claude, Together AI, OpenRouter, HuggingFace, Groq, Voyage AI, Pinecone |

## Query Reference

### Local & Cloud LLM Inference Engines

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `inurl:":11434/api/tags"` | Exposed Ollama API endpoints listing installed local models | Critical |
| `inurl:":11434/api/version"` | Exposed Ollama server instances and version information | High |
| `inurl:":11434/api/generate"` | Exposed Ollama text generation API endpoints without authentication | Critical |
| `inurl:":8000/v1/models" "openai"` | Exposed vLLM, LocalAI, or LiteLLM OpenAI-compatible model endpoints | Critical |
| `inurl:":8000/v2/health/ready" "triton"` | NVIDIA Triton Inference Server health and model serving endpoint | Critical |
| `inurl:":8002/metrics" "nv_inference"` | Triton Prometheus metrics leaking model names and execution parameters | High |
| `inurl:":8080/info" "text-generation-inference"` | HuggingFace TGI (Text Generation Inference) production server metadata | High |
| `inurl:":1234/v1/models"` | LM Studio local model inference server exposed API ports | Critical |
| `intitle:"LocalAI" (inurl:":8080" \| inurl:":5000")` | Self-hosted LocalAI inference engines accessible without authentication | Critical |

### AI Web Interfaces & Multimodal Generators

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `intitle:"Open WebUI" (inurl:":8080" \| inurl:":3000")` | Self-hosted Open WebUI frontend instances for LLMs | High |
| `intitle:"LibreChat" inurl:":3080"` | Enterprise LibreChat multi-model AI chat platform instances | High |
| `intitle:"ComfyUI" inurl:":8188"` | ComfyUI node-based generative AI workflow engine dashboards | Critical |
| `intitle:"Stable Diffusion" inurl:":7860"` | Automatic1111 Stable Diffusion WebUI image generation interfaces | High |
| `intitle:"Fooocus" inurl:":7865"` | Fooocus image generation engine web panels | High |
| `intitle:"Text generation web UI" inurl:":7860"` | Exposed Oobabooga Text Generation WebUI instances | High |
| `intitle:"AnythingLLM" inurl:":3001"` | Exposed AnythingLLM enterprise document chatbot instances | High |
| `intitle:"FastGPT" inurl:":3000"` | Exposed FastGPT knowledge base Q&A system instances | High |

### Agent & Workflow Builders

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `intitle:"Flowise" (inurl:":3000" \| inurl:"/canvas")` | Exposed Flowise AI workflow and agent builder canvas interfaces | Critical |
| `intitle:"Dify" (inurl:":3000/signin" \| inurl:"/apps")` | Exposed Dify LLM application development platforms | High |
| `intitle:"Langflow" inurl:":7860"` | Exposed Langflow visual prototyping UIs for LangChain | High |

### MLOps & Experiment Tracking

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `intitle:"MLflow" inurl:":5000/#/experiments"` | Exposed MLflow tracking servers leaking runs, parameters, and models | Critical |
| `intitle:"Ray Dashboard" inurl:":8265"` | Exposed Ray distributed compute cluster dashboards (RCE risk) | Critical |
| `intitle:"Kubeflow Central Dashboard"` | Exposed Kubeflow enterprise MLOps platform dashboards | Critical |
| `intitle:"Weights & Biases" inurl:":8080"` | Local/on-premise Weights & Biases (W&B) experiment tracking | High |
| `intitle:"Jupyter Notebook" "Token Authentication"` | Exposed Jupyter Notebook servers prompting for authentication | High |
| `intitle:"JupyterLab" inurl:"/lab"` | Exposed JupyterLab development environments | High |

### Vector Databases (RAG Storage)

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `intitle:"Qdrant Web UI" inurl:":6333/dashboard"` | Exposed Qdrant vector database web UI dashboards | Critical |
| `inurl:":6333/collections" "qdrant"` | Qdrant vector collection listing API endpoints leaking collection names | High |
| `inurl:":8000/api/v1/heartbeat" "chromadb"` | Exposed ChromaDB vector database API endpoints | High |
| `intitle:"Attu" (inurl:":8000" \| inurl:":3000")` | Exposed Attu management dashboards for Milvus vector DB | Critical |
| `intitle:"Weaviate Console" inurl:":8080"` | Exposed Weaviate vector database web management consoles | High |
| `inurl:":8080/v1/meta" "weaviate"` | Exposed Weaviate vector search engine meta endpoints | High |

### Leaked AI Tokens & Secrets

| Query | What It Finds | Risk Level |
|-------|---------------|------------|
| `filetype:env "DEEPSEEK_API_KEY"` | DeepSeek LLM API secret keys exposed in .env files | Critical |
| `filetype:env "TOGETHER_API_KEY"` | Together AI serverless model inference API keys in .env files | Critical |
| `filetype:env "OPENROUTER_API_KEY"` | OpenRouter unified LLM routing API keys in .env files | Critical |
| `filetype:env "VOYAGE_API_KEY"` | Voyage AI embedding and vector model API keys in .env files | Critical |
| `filetype:env "CHROMA_SERVER_AUTH_CREDENTIALS"` | ChromaDB vector database server credentials in .env files | Critical |
| `filetype:env "OPENAI_API_KEY=sk-proj-"` | Modern OpenAI Project API keys in .env files | Critical |
| `filetype:env "ANTHROPIC_API_KEY=sk-ant-"` | Anthropic Claude API keys in .env files | Critical |
| `filetype:env "HF_TOKEN=hf_"` | HuggingFace write/read access tokens in .env files | Critical |
| `filetype:env "PINECONE_API_KEY"` | Pinecone vector database API keys in .env files | Critical |
| `filetype:env "LANGCHAIN_API_KEY"` | LangSmith / LangChain tracing API keys in .env files | Critical |
| `filetype:env "GROQ_API_KEY=gsk_"` | Groq LPUs high-speed API keys in .env files | Critical |
| `filetype:env "MISTRAL_API_KEY"` | Mistral AI API keys in .env files | Critical |
| `filetype:env "COHERE_API_KEY"` | Cohere API keys in .env files | Critical |
| `filetype:env "PERPLEXITY_API_KEY"` | Perplexity AI API keys in .env files | Critical |

## Data Source

CSV file: [`GoogleDork-AI-MLOps.csv`](GoogleDork-AI-MLOps.csv)
