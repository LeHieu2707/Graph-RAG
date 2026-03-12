# Graph RAG Project – Technology Stack

## 1. Overview

This project implements a **Graph Retrieval-Augmented Generation (Graph RAG)** system.

The system combines:

* Vector similarity search
* Graph relationship retrieval
* Reranking models
* Large Language Models (LLM)

Goal:

Improve **context retrieval quality** compared to traditional vector RAG.

---

# 2. Core Technologies

## Programming Language

Python 3.11+

Main reasons:

* Rich AI ecosystem
* Mature ML libraries
* Large community support

---

# 3. Data Processing Layer

### Document Loader

Responsible for ingesting data sources.

Supported formats:

* PDF
* HTML
* Markdown
* TXT
* JSON

Libraries used:

* pypdf
* beautifulsoup4
* unstructured

---

### Text Chunking

Split long documents into smaller chunks.

Techniques used:

* Fixed token chunking
* Sliding window chunking
* Semantic chunking

Example configuration:

chunk_size: 512 tokens
chunk_overlap: 100 tokens

---

# 4. Embedding Layer

Embedding models convert text into vectors.

Supported models:

Open-source:

* BGE-large
* Instructor-xl
* E5-large

API-based:

* OpenAI text-embedding-3-large

Embedding dimension examples:

BGE-large → 1024
OpenAI → 3072

---

# 5. Vector Database

Purpose:

Store embeddings and perform similarity search.

Supported vector databases:

* Qdrant
* Weaviate
* Pinecone
* FAISS

Default choice:

Qdrant

Reasons:

* Fast ANN search
* Open source
* Hybrid search support

---

# 6. Graph Database

Used to store **relationships between entities**.

Database:

Neo4j

Graph schema example:

Node types:

* Document
* Chunk
* Entity
* Topic

Relationships:

Document -> Chunk
Chunk -> Entity
Entity -> Entity

Example:

"Tesla" -> founded_by -> "Elon Musk"

---

# 7. Retrieval Layer

Retrieval strategy includes:

Vector Retrieval

cosine similarity search

Graph Retrieval

entity expansion
neighbor traversal

Hybrid Retrieval

vector + graph context merging

---

# 8. Reranking

Reranker models improve retrieval relevance.

Examples:

* bge-reranker-large
* cross-encoder-ms-marco
* cohere-rerank

Function:

Reorder retrieved documents by semantic relevance.

---

# 9. Large Language Model

LLM generates final answers.

Supported models:

OpenAI GPT models
Llama models
Mistral models

Example:

temperature: 0.2
max_tokens: 1024

---

# 10. Evaluation

Evaluation metrics:

Context Recall
Context Precision
Answer Faithfulness
Answer Relevance

Libraries used:

RAGAS
TruLens

---

# 11. Experiment Tracking

Experiment tracking platform:

Weights & Biases

Tracked parameters:

embedding model
chunk size
retriever type
reranker model
LLM model

---

# 12. Deployment

Deployment options:

Docker
Kubernetes
Cloud GPU instances

API layer:

FastAPI

---

# 13. Folder Structure

Example project structure:

project/

src/
ingestion/
embedding/
retrieval/
graph/
rerank/
llm/

data/

docs/

configs/

---

# 14. Future Improvements

Possible improvements:

* Multi-hop graph reasoning
* Adaptive retrieval
* Query decomposition
* Agent-based retrieval
