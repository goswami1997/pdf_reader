from langchain_text_splitters import TokenTextSplitter


def token_chunk(text):
    """
    Splits extracted text into token-based chunks. It uses the TokenTextSplitter
    from langchain_text_splitters to create chunks of text with a specified size and overlap.
    The function returns a list of text chunks.
    The parameters are as follows:
    - chunk_size: The maximum size of each chunk (default is 300 tokens).
    - chunk_overlap: The number of tokens that overlap between consecutive chunks
                (default is 50).
    """
    
    splitter = TokenTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks