import chromadb
from sentence_transformers import SentenceTransformer
from hashlib import sha256
from time import time

_client = None
_collection = None
_embed_model = None


def _init_memory():
    global _client, _collection, _embed_model
    if _client is None:
        _client = chromadb.Client(
            settings=chromadb.config.Settings(persist_directory="./memory_db")
        )
    if _collection is None:
        _collection = _client.get_or_create_collection("jarvis_memory")
    if _embed_model is None:
        _embed_model = SentenceTransformer("all-MiniLM-L6-v2")


def store_memory(text: str):
    _init_memory()
    embedding = _embed_model.encode(text).tolist()
    unique = f"{sha256(text.encode('utf-8')).hexdigest()}-{int(time() * 1000)}"
    _collection.add(documents=[text], embeddings=[embedding], ids=[unique])
    _client.persist()


def retrieve_memory(query: str, n_results=3):
    _init_memory()
    embedding = _embed_model.encode(query).tolist()
    results = _collection.query(query_embeddings=[embedding], n_results=n_results)
    return results.get("documents", [])