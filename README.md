# RAG_pdf

## Project Overview

`RAG_pdf` is a Python project for extracting text from PDF files and splitting that text into chunks for retrieval augmented generation (RAG) workflows. The project includes several chunking strategies and a PDF reader utility. It is designed as a starting point for building a full document retrieval pipeline with embeddings, vector stores, and LLM-based retrieval.

## What the Project Does

- Reads PDF documents and extracts text using `pypdf`.
- Supports multiple text chunking approaches:
  - fixed-size chunking
  - overlapping character chunking
  - token-based chunking
  - recursive character chunking
  - semantic chunking using embeddings
- Includes test scripts that demonstrate each chunking strategy.

## Project Structure

```
app.py
config.py
requirements.txt
README.md

data/
modules/
    pdf_reader.py
    chunker/
        chunker.py
        fixed_chunker.py
        overlap_chunker.py
        token_chunker.py
        semantic_chunker.py
tests/
    chunk_comparison.py
    fixed_sized_chunker_test.py
    overlap_chunker_test.py
    pdf_reader_test.py
    recusive_chunker_test.py
    semantic_chunker_test.py
    token_chunker_test.py
```

### Key Files

- `app.py` - currently an empty application entry point placeholder.
- `config.py` - currently an empty configuration placeholder.
- `requirements.txt` - dependency manifest used to install required Python packages.
- `modules/pdf_reader.py` - contains the PDF text extraction helper.
- `modules/chunker/` - contains chunking implementations for different strategies.
- `tests/` - example scripts that read a sample PDF and exercise chunking functions.

## Module Details

### `modules/pdf_reader.py`

- Function: `extract_text_from_pdf(pdf_path)`
- Reads a PDF file using `PdfReader` from `pypdf`.
- Returns the extracted text as a single string.

### `modules/chunker/fixed_chunker.py`

- Function: `fixed_size_chunk(text)`
- Splits text into fixed-size chunks of 1000 characters with no overlap.

### `modules/chunker/overlap_chunker.py`

- Function: `overlap_chunk(text)`
- Splits text into 1000-character chunks with 200-character overlap.

### `modules/chunker/token_chunker.py`

- Function: `token_chunk(text)`
- Uses `TokenTextSplitter` to split text into chunks of 300 tokens with 50-token overlap.

### `modules/chunker/chunker.py`

- Function: `split_text_into_chunks(text)`
- Uses `RecursiveCharacterTextSplitter` to split text into chunks of 1000 characters with 200-character overlap.

### `modules/chunker/semantic_chunker.py`

- Function: `semantic_chunk(text)`
- Uses `SemanticChunker` and `HuggingFaceEmbeddings` to create semantically grouped `Document` objects.
- Embeddings model: `sentence-transformers/all-MiniLM-L6-v2`.

## Installation

1. Create and activate a Python virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies.

```powershell
pip install -r requirements.txt
```

## Usage

The project currently provides module-level functions rather than a complete runnable app. Example usage in a Python script:

```python
from modules.pdf_reader import extract_text_from_pdf
from modules.chunker.fixed_chunker import fixed_size_chunk
from modules.chunker.overlap_chunker import overlap_chunk
from modules.chunker.token_chunker import token_chunk
from modules.chunker.chunker import split_text_into_chunks
from modules.chunker.semantic_chunker import semantic_chunk

pdf_path = "data/sample.pdf"
text = extract_text_from_pdf(pdf_path)

fixed_chunks = fixed_size_chunk(text)
overlap_chunks = overlap_chunk(text)
token_chunks = token_chunk(text)
recursive_chunks = split_text_into_chunks(text)
semantic_docs = semantic_chunk(text)

print("Fixed chunks:", len(fixed_chunks))
print("Overlap chunks:", len(overlap_chunks))
print("Token chunks:", len(token_chunks))
print("Recursive chunks:", len(recursive_chunks))
print("Semantic chunks:", len(semantic_docs))
```

## Expected Behavior

- The PDF reader should extract readable text from the PDF pages.
- Fixed chunking returns equal-sized segments.
- Overlapping chunking preserves context across boundaries by repeating part of the previous chunk.
- Token chunking uses token counts instead of raw character length.
- Recursive chunking uses a hierarchical separator strategy to produce logical chunks.
- Semantic chunking groups text with semantic similarity using an embedding model.

## Notes and Expectations

- `app.py` and `config.py` are currently placeholders and do not contain implementation logic.
- `modules/embeddings/`, `modules/LLMs/`, `modules/retriever/`, and `modules/vectorstore/` are present but currently empty; these are intended for future RAG components.
- The project expects a sample PDF at `data/sample.pdf` for the provided test scripts.
- If you want to build a full RAG pipeline, add:
  - a vector store implementation
  - a retriever interface
  - an LLM query layer
  - application entry point logic in `app.py`

## Running Tests

The test files currently act as example runners. Run them with Python:

```powershell
python tests/pdf_reader_test.py
python tests/fixed_sized_chunker_test.py
python tests/overlap_chunker_test.py
python tests/token_chunker_test.py
python tests/semantic_chunker_test.py
python tests/chunk_comparison.py
```

## Dependencies

The main dependencies include:

- `langchain`
- `pypdf`
- `langchain-text-splitters`
- `huggingface_hub`
- `sentence-transformers`
- `torch`
- `faiss-cpu`
- `streamlit` (installed but not currently used in the code)

## Future Improvements

- Add a complete application workflow in `app.py`.
- Implement configuration options in `config.py`.
- Populate the empty service folders for embeddings, retriever, vector store, and LLM orchestration.
- Add automated unit tests using a test framework such as `pytest`.
- Document expected input and output formats for the RAG pipeline.

## Future PDF Question-Answering Flow

This project can evolve into a full PDF QA reader where users upload a PDF, ask questions about its contents, and receive answers grounded in the source document.

### Future end-to-end flow

1. User uploads a PDF file to the application.
2. The PDF reader extracts text from every page using `modules/pdf_reader.py`.
3. The extracted text is passed through a chunking pipeline:
   - fixed-size chunking for baseline segmentation
   - overlapping chunking for context continuity
   - token chunking for better compatibility with LLM token limits
   - semantic chunking for meaning-aware document segments
4. Chunks are converted into embeddings using an embeddings service from `modules/embeddings/`.
5. Embeddings are stored in a vector store implementation under `modules/vectorstore/`.
6. A retriever in `modules/retriever/` searches the vector store for the most relevant text chunks given a user query.
7. The top relevant chunks are passed to an LLM in `modules/LLMs/` along with the original question.
8. The LLM generates a concise, accurate answer referencing the PDF content.
9. The application returns the answer and optionally highlights the source text chunks or pages used to support it.

### User experience expectations

- Users provide a PDF and a natural-language question.
- The system responds with an answer based on the document, not generic or unrelated text.
- The answer should cite or link to relevant sections of the PDF content.
- If a query cannot be answered from the document, the app should be transparent and say the information is unavailable.

### Where this maps in the current project

- `modules/pdf_reader.py` becomes the document ingestion layer.
- `modules/chunker/` remains the text segmentation engine.
- `modules/embeddings/` will house the embedding model wrapper.
- `modules/vectorstore/` will house storage and retrieval logic.
- `modules/retriever/` will implement query-to-vector search.
- `modules/LLMs/` will handle prompt construction and answer generation.
- `app.py` will orchestrate file upload, chunking, storage, retrieval, and answer display.

### Optional additional enhancements

- Add a web UI with `Streamlit` or FastAPI + frontend for interactive PDF upload and QA.
- Cache embeddings for previously uploaded PDFs to reuse document knowledge.
- Add PDF metadata extraction and page-aware source citations.
- Provide a fallback retrieval explanation for low-confidence queries.
