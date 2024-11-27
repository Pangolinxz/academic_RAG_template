"""Package installer"""

from setuptools import find_packages, setup  # type: ignore

setup(
    name="academic_rag",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
        "docx",
        "nltk",
        "chromadb",
        "python-dotenv",
        "typeguard",
        "langchain_text_splitters",
        "huggingface_hub",
        "streamlit"
    ],
)