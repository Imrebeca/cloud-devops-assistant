
from sentence_transformers import SentenceTransformer
import chromadb

# Carrega o mesmo modelo utilizado na criação dos embeddings
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# Conecta ao banco vetorial já criado
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="cloud_devops_knowledge"
)


def search_knowledge(question, top_k=3):
    # Converte a pergunta em embedding
    question_embedding = model.encode([question]).tolist()

    # Busca os chunks mais semelhantes
    results = collection.query(
        query_embeddings=question_embedding,
        n_results=top_k
    )

    return results


if __name__ == "__main__":
    question = "How does Terraform state locking work?"

    results = search_knowledge(question)

    for index, document in enumerate(results["documents"][0], start=1):
        source = results["metadatas"][0][index - 1]["source"]

        print(f"\nResultado {index}")
        print(f"Fonte: {source}")
        print(f"Conteúdo:\n{document}")
