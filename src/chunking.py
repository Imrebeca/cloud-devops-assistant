
def split_text(text, chunk_size=800, overlap=100):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

if __name__ == "__main__":
    sample_text = """
    Terraform State stores information about infrastructure.
    Remote state allows teams to share infrastructure information.
    State locking prevents simultaneous modifications.
    """

    chunks = split_text(sample_text, chunk_size=80, overlap=15)

    for index, chunk in enumerate(chunks, start=1):
        print(f"\nCHUNK {index}:")
        print(chunk)