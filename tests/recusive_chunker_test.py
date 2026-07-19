from modules.pdf_reader import extract_text_from_pdf
from modules.chunker.chunker import split_text_into_chunks

pdf_path = "data/sample.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = split_text_into_chunks(text)

print(f"Total Chunks: {len(chunks)}")

# print("-" * 80)
# print("-" * 80)


for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {len(chunk)} characters")