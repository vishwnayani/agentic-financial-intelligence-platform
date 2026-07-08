from app.rag.vector_store import get_vector_store

vs = get_vector_store()

docs = vs.similarity_search("AI", k=2)

for d in docs:
    print(d.metadata)