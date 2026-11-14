
from pathlib import Path
from src.chunking import split_text

PROJECT_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_BASE = PROJECT_ROOT / "knowledge_base"

documents = list(KNOWLEDGE_BASE.rglob("*.md"))

all_chunks = []

for document in documents:
    content = document.read_text(encoding="utf-8")

    chunks = split_text(content)

    for index, chunk in enumerate(chunks):
        all_chunks.append({
            "source": str(document.relative_to(KNOWLEDGE_BASE)),
            "chunk_id": index,
            "content": chunk
        })

print(f"Documentos encontrados: {len(documents)}")
print(f"Total de chunks gerados: {len(all_chunks)}")

for chunk in all_chunks:
    print(f"\nArquivo: {chunk['source']}")
    print(f"Chunk: {chunk['chunk_id']}")
    print(f"Conteúdo: {chunk['content'][:100]}...")
