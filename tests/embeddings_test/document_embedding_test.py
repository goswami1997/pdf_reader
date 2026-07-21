from modules.pdf_reader import extract_text_from_pdf
from modules.chunker.semantic_chunker import semantic_chunk
from modules.embeddings.embedding_generator import generate_document_embeddings

pdf_path = "data/sample.pdf"

text = extract_text_from_pdf(pdf_path)

semantic_chunks = semantic_chunk(text)

semantic_chunk_texts = [
    doc.page_content
    for doc in semantic_chunks
]

embeddings = generate_document_embeddings(
    semantic_chunk_texts
)

print("Chunks :", len(semantic_chunk_texts))
print("Embeddings :", len(embeddings))
print("Dimension :", len(embeddings[0]))