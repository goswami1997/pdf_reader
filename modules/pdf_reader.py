from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Reads a PDF and returns all text as a single string.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        # Some pages may not contain extractable text
        if page_text:
            text += page_text + "\n"

    return text