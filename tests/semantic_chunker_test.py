from modules.pdf_reader import extract_text_from_pdf
from modules.chunker.semantic_chunker import semantic_chunk

text = extract_text_from_pdf("data/sample.pdf")

documents = semantic_chunk(text)

print(f"Total Chunks: {len(documents)}")

for i, doc in enumerate(documents[:5]):
    print("=" * 80)
    print(f"Chunk {i+1}")
    print("=" * 80)
    print(doc.page_content)