from langchain_text_splitters import CharacterTextSplitter


def fixed_size_chunk(text):

    splitter = CharacterTextSplitter(
        separator="",
        chunk_size=1000,
        chunk_overlap=0
    )

    chunks = splitter.split_text(text)

    return chunks