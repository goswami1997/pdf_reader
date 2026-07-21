from langchain_huggingface import HuggingFaceEmbeddings


def load_embedding_model():

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model


def generate_document_embeddings(chunks):

    model = load_embedding_model()

    embeddings = model.embed_documents(chunks)

    return embeddings