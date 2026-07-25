from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text_into_chunks(text):
    """
    Splits extracted text into overlapping chunks. It uses the RecursiveCharacterTextSplitter
    from langchain_text_splitters to create chunks of text with a specified size and overlap. 
    The function returns a list of text chunks. 
    The parameters are as follows:
    - chunk_size: The maximum size of each chunk (default is 1000 characters).
    - chunk_overlap: The number of characters that overlap between consecutive chunks  
                (default is 200).
    - length_function: A function to determine the length of the text (default is len).
    - separators: A list of separators to use when splitting the text 
                (default is ["\n\n", "\n", " ", ""]).
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = text_splitter.split_text(text)

    return chunks