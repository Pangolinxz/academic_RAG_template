import os
from PyPDF2 import PdfReader
from markdown import markdown
from docx import Document

class DocumentReader:
    """A class to read various document types."""

    def __init__(self, file_path):
        self.file_path = file_path

    def detect_file_type(self):
        """Detect the file type based on its extension."""
        _, extension = os.path.splitext(self.file_path)
        return extension.lower()

    def read_file(self):
        """Read the file based on its detected type."""
        file_type = self.detect_file_type()

        if file_type == ".pdf":
            return self._read_pdf()
        elif file_type == ".md":
            return self._read_md()
        elif file_type == ".txt":
            return self._read_txt()
        elif file_type == ".docx":
            return self._read_docx()
        else:
            print(f"\tUnsupported file type: {file_type}, file {self.file_path} skipped.")
            return None

    def _read_pdf(self):
        """Read a PDF file and return its text."""
        text = ""
        try:
            reader = PdfReader(self.file_path)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        except Exception as e:
            print(f"Error reading PDF: {e}")
        return text

    def _read_md(self):
        """Read a Markdown file and return its text."""
        text = ""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                md_content = file.read()
                text = markdown(md_content)
        except Exception as e:
            print(f"Error reading Markdown file: {e}")
        return text

    def _read_txt(self):
        """Read a plain text file and return its text."""
        text = ""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except Exception as e:
            print(f"Error reading text file: {e}")
        return text

    def _read_docx(self):
        """Read a DOCX file and return its text."""
        text = ""
        try:
            document = Document(self.file_path)
            for paragraph in document.paragraphs:
                text += paragraph.text + "\n"
        except Exception as e:
            print(f"Error reading DOCX file: {e}")
        return text
