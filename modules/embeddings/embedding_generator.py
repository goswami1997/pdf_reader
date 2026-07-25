from langchain_huggingface import HuggingFaceEmbeddings


def load_embedding_model():
    """HuggingFaceEmbeddings model for loading embeddings.
    Returns:
        HuggingFaceEmbeddings: The HuggingFaceEmbeddings model.
    It is used to generate embeddings for text chunks, 
    which can be used for semantic similarity and other NLP tasks.
    """
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model


def generate_document_embeddings(chunks):
    """
    Generates embeddings for a list of text chunks using the HuggingFaceEmbeddings model.
    Returns:
        list: A list of embedding vectors.
    It takes a list of text chunks as input and returns their corresponding embeddings."""
    model = load_embedding_model()

    embeddings = model.embed_documents(chunks)

    return embeddings