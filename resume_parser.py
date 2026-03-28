import PyPDF2
import docx


def extract_pdf(file):
    """Extract text from a PDF file object."""
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text.strip()


def extract_docx(file):
    """Extract text from a .docx file object."""
    text = ""
    try:
        doc = docx.Document(file)
        for para in doc.paragraphs:
            if para.text.strip():
                text += para.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX: {e}")
    return text.strip()


def extract_resume(file):
    """Detect file type and extract text accordingly."""
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return extract_pdf(file)
    elif filename.endswith(".docx"):
        return extract_docx(file)
    else:
        print(f"Unsupported file type: {filename}")
        return ""