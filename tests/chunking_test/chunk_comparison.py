from modules.pdf_reader import extract_text_from_pdf
from modules.chunker.fixed_chunker import fixed_size_chunk
from modules.chunker.overlap_chunker import overlap_chunk
from modules.chunker.token_chunker import token_chunk
from modules.chunker.chunker import split_text_into_chunks
from modules.chunker.semantic_chunker import semantic_chunk

# Read PDF
pdf_path = "data/sample.pdf"
text = extract_text_from_pdf(pdf_path)

# Generate chunks
fixed_chunks = fixed_size_chunk(text)
overlap_chunks = overlap_chunk(text)
token_chunks = token_chunk(text)
recursive_chunks = split_text_into_chunks(text)
semantic_chunks = semantic_chunk(text)

# Summary
print("=" * 100)
print("SUMMARY")
print("=" * 100)

print(f"Fixed Chunking      : {len(fixed_chunks)} chunks")
print(f"Overlap Chunking    : {len(overlap_chunks)} chunks")
print(f"Token Chunking      : {len(token_chunks)} chunks")
print(f"Recursive Chunking  : {len(recursive_chunks)} chunks")
print(f"Semantic Chunking   : {len(semantic_chunks)} chunks")

print("\n")

# Helper function
def display_chunk(name, chunks):
    print("=" * 100)
    print(name)
    print("=" * 100)

    first_chunk = chunks[0]

    # SemanticChunker returns Document objects
    if hasattr(first_chunk, "page_content"):
        content = first_chunk.page_content
    else:
        content = first_chunk

    print(f"Length : {len(content)}")
    print("\nFirst 300 Characters\n")
    print(content[:300])
    print("\nLast 300 Characters\n")
    print(content[-300:])
    print("\n")


display_chunk("Fixed Size Chunking", fixed_chunks)
display_chunk("Overlap Chunking", overlap_chunks)
display_chunk("Token Chunking", token_chunks)
display_chunk("Recursive Chunking", recursive_chunks)
display_chunk("Semantic Chunking", semantic_chunks)