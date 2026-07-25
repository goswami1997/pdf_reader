from langchain_text_splitters import CharacterTextSplitter


def overlap_chunk(text):
    """
    Splits extracted text into overlapping chunks. It uses the CharacterTextSplitter
    from langchain_text_splitters to create chunks of text with a specified size and overlap.
    The function returns a list of text chunks.
    The parameters are as follows:
    - chunk_size: The maximum size of each chunk (default is 1000 characters).
    - chunk_overlap: The number of characters that overlap between consecutive chunks
                (default is 200).
    - separator: The separator to use when splitting the text (default is "").
    """
    splitter = CharacterTextSplitter(
        separator="",
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks