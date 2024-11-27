import os
import chromadb as db
from uuid import uuid4
from datetime import datetime
from langchain_text_splitters import RecursiveCharacterTextSplitter
import re
from typeguard import typechecked
from document_reader import DocumentReader
import logging
from nltk.corpus import stopwords
import unicodedata

logging.basicConfig(
    filename="ingest.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)


class Collection:

    @typechecked
    def __init__(self, collection: str):
        try:
            self.client = db.PersistentClient()
        except:
            raise Exception("Error al conectar con la base de datos")

        self.collection = self.client.get_or_create_collection(
            collection, metadata={"hnsw:space": "cosine"}
        )

    @typechecked
    def split(
        self,
        text: str,
        encoding_name: str = "cl100k_base",
        model_name: str = "____",
        chunk_size: int = 120,
        chunk_overlap: int = 20,
    ):
        text_splitter = _______________________.from_tiktoken_encoder(
            encoding_name=encoding_name,
            model_name=model_name,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        return text_splitter.split_text(text)

    def delete_collection(self):
        self.client.delete_collection(self.collection.name)

    def __len__(self):
        return self.collection.count()

    @typechecked
    def query(self, query: str, n_results: int = 3, where=None):        
        cleaned_query = self.clean_text(query)

        return self.collection.____(
            query_texts=cleaned_query, n_results=n_results, where=where
        )

    @typechecked
    def upsert(self, document: str, metadata: dict, id: str = str(uuid4())):
        self.collection.upsert(documents=[document], metadatas=[metadata], ids=id)

    @typechecked
    def clean_text(self, text: str):
        spanish_stopwords = _________.words('spanish')
        
        query = text.lower()
        query = ''.join(c for c in unicodedata.normalize('NFD', query) if unicodedata.category(c) != 'Mn')
        query = re.sub(r'[^\w\s]', '', query)
        tokens = query.split()
        tokens = [word for word in tokens if word not in spanish_stopwords]
        return " ".join(tokens)
    
    @typechecked
    def contains(self, document: str, where: list = []):
        results = self.collection.query(
            query_texts=[document],
            n_results=1,
            where={"$and": where},
        )

        return results["ids"][0] != [], results

    @typechecked
    def ingest(self, folder_path: str = "./data/", split_files: bool = True):
        print(f"Ingesting files in {folder_path}...")
        action = "Agregando"
        items = os.listdir(folder_path)
        for item in items:
            item_path = os.path.join(folder_path, item)
            # Normaliza la ruta para sistemas multiplataforma
            path = os.path.normpath(item_path)

            if os.path.isfile(item_path):
                title = os.path.splitext(item)[0]

                content = _________(item_path).read_file()
                if content is None:
                    continue

                if split_files:
                    split_content = self.split(content)

                    for i, text in enumerate(split_content):
                        is_contained, result = self.contains(
                            text,
                            [
                                {"title": title},
                                {"path": path},
                                {"category": path.split("/")[1]},
                                {"chunk_position": i},
                            ],
                        )

                        if ________:
                            id = str(result["ids"][0])
                            action = "Actualizando"
                            creation_date = result["______"][0][0]["creation_date"]
                            update_date = str(datetime.now())
                        else:
                            id = str(uuid4())
                            action = "Agregando"
                            creation_date = str(datetime.now())
                            update_date = creation_date

                        self.______(
                            text,
                            metadata={
                                "title": title,
                                "path": path,
                                "category": path.split("/")[1],
                                "creation_date": creation_date,
                                "update_date": update_date,
                                "chunk_position": i,
                            },
                            id=id,
                        )
                        ______.info(
                            f"{self.collection.name}: {action} archivo: {title}, ruta: {path}, cantidad de chunks: {len(split_content)}"
                        )
                else:
                    is_contained, result = self.contains(
                        content,
                        [
                            {"title": title},
                            {"path": path},
                            {"category": path.split("/")[1]},
                        ],
                    )

                    if is_contained:
                        id = str(result["ids"][0])
                        action = "Actualizando"
                        creation_date = result["metadatas"][0][0]["creation_date"]
                        update_date = str(datetime.now())
                    else:
                        id = str(uuid4())
                        action = "Agregando"
                        creation_date = str(datetime.now())
                        update_date = creation_date

                    self.upsert(
                        content,
                        {
                            "title": title,
                            "path": path,
                            "category": path.split("/")[1],
                            "creation_date": creation_date,
                            "updated_date": update_date,
                        },
                        id,
                    )
                    logging.info(
                        f"{self.collection.name}: {action} archivo: {title}, ruta: {path}"
                    )
            elif os.path.isdir(item_path):
                self.ingest(item_path, split_files=split_files)


if __name__ == "__main__":
    from pprint import pprint


    notes = ________("notes")
    examples = Collection("examples")

    notes.______(folder_path="data/notes")
    examples.ingest(folder_path="data/examples", split_files=False)

    query = "¿Cómo normalizar una tabla en cuarta forma normal?"
    print("\nQuery:", query)
    print("Notes:")
    pprint(notes._____(query))
    print("-"*140)
    print("Examples:")
    pprint(examples.query(query, 1))
