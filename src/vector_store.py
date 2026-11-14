
from sentence_transformers import SentenceTransformer
import chromadb

from src.ingest import all_chunks

import os

os.environ["HF_HOME"] = "/app/huggingface"

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# Inicializa o banco vetorial
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="cloud_devops_knowledge"
)

# Gera os embeddings dos documentos
documents = [chunk["content"] for chunk in all_chunks]
ids = [
    f"{chunk['source']}_{chunk['chunk_id']}"
    for chunk in all_chunks
]
metadatas = [
    {"source": chunk["source"]}
    for chunk in all_chunks
]

import time

print("Iniciando geração dos embeddings...", flush=True)

start = time.time()

embeddings = model.encode(
    documents,
    batch_size=8,
    show_progress_bar=True
).tolist()

print(f"Embeddings gerados em {time.time() - start:.2f} segundos", flush=True)

# Armazena os documentos e seus embeddings
collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings
)

print(f"Chunks armazenados no ChromaDB: {collection.count()}")
