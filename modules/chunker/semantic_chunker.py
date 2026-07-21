from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings


def semantic_chunk(text):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    splitter = SemanticChunker(
        embeddings=embeddings
    )

    documents = splitter.create_documents([text])

    chunks = [
    doc.page_content
    for doc in documents
    ]

    return chunks