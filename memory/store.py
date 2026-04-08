import chromadb
from sentence_transformers import SentenceTransformer

# Persistent DB (saved to disk)
client = chromadb.Client(
    settings=chromadb.config.Settings(
        persist_directory="./memory_db"
    )
)

collection = client.get_or_create_collection("jarvis_memory")

embed_model = SentenceTransformer("all-MiniLM-L6-v2")


def store_memory(text: str):
    embedding = embed_model.encode(text).tolist()

    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[str(hash(text))]
    )

    client.persist()  # 🔥 persists to disk


def retrieve_memory(query: str, n_results=3):
    embedding = embed_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )

    return results["documents"]