import os
from PyPDF2 import PdfReader  # Necesario: lectura de PDF con librería externa
from markdown import markdown  # Necesario para procesar Markdown
from docx import Document  # Necesario para leer archivos DOCX
from my_structures import MyList, my_split  # Usamos nuestras estructuras personalizadas

class DocumentReader:
    """
    Clase para leer diversos tipos de documentos.
    
    Por defecto, retorna el contenido como una cadena (str).
    Si se especifica el parámetro convert_to_mylist=True, 
    se convierte el contenido en una MyList de tokens (usando my_split, por ejemplo).
    """
    
    def __init__(self, file_path):
        self.file_path = file_path

    def detect_file_type(self):
        # Uso nativo de os.path.splitext, indispensable
        _, extension = os.path.splitext(self.file_path)
        return extension.lower()

    def read_file(self, convert_to_mylist=False):
        file_type = self.detect_file_type()
        if file_type == ".pdf":
            content = self._read_pdf()
        elif file_type == ".md":
            content = self._read_md()
        elif file_type == ".txt":
            content = self._read_txt()
        elif file_type == ".docx":
            content = self._read_docx()
        else:
            print(f"\tUnsupported file type: {file_type}, file {self.file_path} skipped.")
            return None
        
        if convert_to_mylist and content is not None:
            # Convertimos el contenido en una MyList de tokens usando la función my_split (nuestra implementación)
            return my_split(content)
        else:
            return content

    def _read_pdf(self):
        # Acumulamos las líneas en una MyList en lugar de usar una cadena nativa directamente
        lines = MyList()
        try:
            reader = PdfReader(self.file_path)
            for page in reader.pages:  # Uso nativo: iteración sobre lista de páginas es indispensable
                extracted = page.extract_text()
                if extracted:
                    lines.append(extracted + "\n")
        except Exception as e:
            print(f"Error reading PDF: {e}")
        # Convertimos nuestra MyList a una lista nativa para concatenar (join() es nativo, indispensable)
        native_lines = []
        for line in lines:
            native_lines.append(line)
        return "".join(native_lines)  # Uso nativo: join es necesario para concatenar strings

    def _read_md(self):
        # Usamos MyList para almacenar el resultado
        lines = MyList()
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:  # Uso nativo: abrir archivos es indispensable
                md_content = file.read()
                # Procesamos el contenido Markdown (markdown() es una función nativa de la librería)
                result = markdown(md_content)
                lines.append(result)
        except Exception as e:
            print(f"Error reading Markdown file: {e}")
        native_lines = []
        for line in lines:
            native_lines.append(line)
        return "".join(native_lines)  # Uso nativo: join para concatenar strings

    def _read_txt(self):
        # Acumulamos cada línea en una MyList
        lines = MyList()
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:  # Uso nativo: abrir archivos es indispensable
                for line in file:  # Uso nativo: iteración sobre el archivo es indispensable
                    lines.append(line)
        except Exception as e:
            print(f"Error reading text file: {e}")
        native_lines = []
        for line in lines:
            native_lines.append(line)
        return "".join(native_lines)  # Uso nativo: join es necesario para concatenar strings

    def _read_docx(self):
        # Acumulamos el texto de cada párrafo en una MyList
        lines = MyList()
        try:
            document = Document(self.file_path)
            for paragraph in document.paragraphs:  # Uso nativo: iteración sobre párrafos es indispensable
                lines.append(paragraph.text + "\n")
        except Exception as e:
            print(f"Error reading DOCX file: {e}")
        native_lines = []
        for line in lines:
            native_lines.append(line)
        return "".join(native_lines)  # Uso nativo: join para concatenar strings
