from modules.embeddings.embedding_generator import load_embedding_model

model = load_embedding_model()

query = "What is Apache Spark?"

query_embedding = model.embed_query(query)

print("Type:", type(query_embedding))
print("Length:", len(query_embedding))
print("First 10 values:")
print(query_embedding[:10])