
import os
from dotenv import load_dotenv
from anthropic import Anthropic

from src.retriever import search_knowledge

# Carrega as variáveis do arquivo .env
load_dotenv()

# Inicializa o cliente Claude
client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)


def ask_assistant(question):
    # Recupera os trechos relevantes da documentação
    results = search_knowledge(question, top_k=2)

    context = "\n\n".join(results["documents"][0])

    # Envia a pergunta e o contexto para o Claude
    response = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=600,
        system=(
            "You are a Cloud and DevOps assistant. "
            "Answer using only the provided context. "
            "If information is missing, state that clearly. "
            "Be concise, accurate, and answer in the user's language."
),
        messages=[
            {
                "role": "user",
                "content": (
                    f"Documentation context:\n{context}\n\n"
                    f"Question: {question}"
                )
            }
        ]
    )

    return response


if __name__ == "__main__":
    question = input("\nDigite sua pergunta: ")

    answer = ask_assistant(question)

    print("\nResposta:")

for block in answer.content:
    if block.type == "text":
        print(block.text)

    print(f"\nTokens de entrada: {answer.usage.input_tokens}")
    print(f"Tokens de saída: {answer.usage.output_tokens}")
