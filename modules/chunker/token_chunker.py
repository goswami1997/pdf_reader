from langchain_text_splitters import TokenTextSplitter


def token_chunk(text):

    splitter = TokenTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks