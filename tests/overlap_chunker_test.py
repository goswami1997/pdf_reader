from modules.pdf_reader import extract_text_from_pdf
from modules.chunker.overlap_chunker import overlap_chunk

text = extract_text_from_pdf("data/sample.pdf")

chunks = overlap_chunk(text)

print(chunks[0])

print("="*100)

print(chunks[1])