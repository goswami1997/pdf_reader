from modules.pdf_reader import extract_text_from_pdf
from modules.chunker.chunker import split_text_into_chunks


pdf_path = "data/sample.pdf"

text = extract_text_from_pdf(pdf_path)

print("=" * 80)
print(text[:2000])      # Print only the first 2000 characters
print("=" * 80)

print(f"\nTotal Characters: {len(text)}")



