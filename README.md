# Cloud & DevOps Knowledge Assistant

An AI-powered knowledge assistant designed to answer Cloud and DevOps questions using Retrieval-Augmented Generation (RAG).

The application retrieves relevant information from a technical knowledge base and uses Anthropic Claude to generate contextual, accurate answers.

## Features

- Retrieval-Augmented Generation (RAG) architecture.
- Semantic search using Sentence Transformers.
- Vector storage and retrieval with ChromaDB.
- AI-powered responses using Anthropic Claude.
- Multilingual support: English documentation and Portuguese questions.
- Token usage tracking to monitor API consumption.
- Docker support for containerized execution.

## Technologies

- Python
- Anthropic Claude API
- Sentence Transformers
- ChromaDB
- PyTorch
- Docker
- GitHub Actions

## Knowledge Base

The knowledge base contains technical documentation covering:

- **AWS:** S3 and IAM.
- **Kubernetes:** Pods and Deployments.
- **Terraform:** Providers and State.
- **Docker:** Containers and Images.

## Architecture

1. The user submits a question.
2. Sentence Transformers converts the question into an embedding.
3. ChromaDB retrieves the most relevant documentation chunks.
4. The retrieved context is sent to Anthropic Claude.
5. Claude generates a contextual response.
6. Input and output token usage is displayed.

## Project Structure

```text
cloud-devops-assistant/
├── knowledge_base/
│   ├── aws/
│   ├── kubernetes/
│   ├── terraform/
│   └── docker/
├── src/
│   ├── chunking.py
│   ├── ingest.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── main.py
├── .gitignore
├── Dockerfile
└── requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Imrebeca/cloud-devops-assistant.git
cd cloud-devops-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Anthropic API key

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

### 5. Generate the vector database

```bash
python -m src.vector_store
```

### 6. Run the assistant

```bash
python -m src.main
```

## Token Optimization

The application uses context retrieval to reduce unnecessary information sent to the language model.

The retrieval configuration and prompt were optimized to balance response quality and token consumption.

## Future Improvements

- Expand the technical knowledge base.
- Improve retrieval relevance.
- Implement automated testing and CI workflows.

## Author

**Rebeca Souza**

GitHub: [@Imrebeca](https://github.com/Imrebeca)