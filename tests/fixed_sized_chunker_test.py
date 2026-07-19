from modules.pdf_reader import extract_text_from_pdf
from modules.chunker.fixed_chunker import fixed_size_chunk

text = extract_text_from_pdf("data/sample.pdf")

chunks = fixed_size_chunk(text)

print(f"Total Chunks : {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print("="*80)
    print(f"Chunk {i+1}")
    print(chunk)