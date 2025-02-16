import os
import re
import unicodedata
from uuid import uuid4
from datetime import datetime
import logging
from nltk.corpus import stopwords

# Importamos nuestras estructuras personalizadas desde el archivo "my_structures.py"
# Se supone que en "my_structures.py" están definidas: MyList, MyDict, MySet, sort_mylist, my_split
from my_structures import MyList, MyDict, MySet, sort_mylist, my_split
from document_reader import DocumentReader  

logging.basicConfig(
    filename="ingest.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)

class Collection:
    def __init__(self, collection: str):
        # Usamos nuestro MyDict para almacenar los documentos
        self.name = collection
        self.documents = MyDict()  # Cada documento se guardará con un ID y un valor (otro MyDict)

    def split(self, text: str, chunk_size: int = 120, chunk_overlap: int = 20):
        """
        Divide el texto en fragmentos (chunks) utilizando nuestra estructura personalizada MyList.
        Se implementa desde cero, sin usar métodos nativos para listas.
        """
        chunks = MyList()
        # Calcular la longitud del texto sin usar len() nativo
        text_length = 0
        for _ in text:
            text_length += 1

        start = 0
        while start < text_length:
            end = start + chunk_size
            chunk = ""
            index = 0
            # Recorremos el string manualmente
            for char in text:
                if index >= start and index < end:
                    chunk += char
                index += 1
            chunks.append(chunk)
            if end >= text_length:
                break
            start += (chunk_size - chunk_overlap)
        return chunks

    def delete_collection(self):
        """
        Elimina todos los documentos de la colección.
        """
        self.documents = MyDict()

    def __len__(self):
        """
        Retorna el número de documentos en la colección.
        """
        count = 0
        for _ in self.documents.items_iter():
            count += 1
        return count

    def clean_text(self, text: str):
        """
        Normaliza el texto: lo convierte a minúsculas, elimina acentos y signos de puntuación,
        y remueve las stopwords en español.
        """
        spanish_stopwords = stopwords.words('spanish')
        # Uso de métodos nativos de str es indispensable (por ejemplo, lower())
        text = text.lower()  # Uso nativo: es necesario para convertir a minúsculas
        text = ''.join(c for c in unicodedata.normalize('NFD', text)
                       if unicodedata.category(c) != 'Mn')
        text = re.sub(r'[^\w\s]', '', text)
        # En lugar de usar el split nativo, utilizamos nuestra función personalizada my_split
        tokens = my_split(text)  # my_split retorna una MyList de tokens
        # Filtramos usando nuestras estructuras personalizadas:
        filtered_tokens = MyList()
        for token in tokens:
            # Para comprobar si un token está en las stopwords (lista nativa), usamos 'in'
            if token not in spanish_stopwords:  # Uso nativo: stopwords es una lista nativa
                filtered_tokens.append(token)
        # Convertimos nuestra MyList a una secuencia nativa para poder usar join (necesario para str)
        native_tokens = []  # Uso nativo: join requiere una lista de str
        for token in filtered_tokens:
            native_tokens.append(token)
        return " ".join(native_tokens)  # Uso nativo: join, imprescindible para concatenar strings

    def simple_similarity(self, query: str, doc_text: str) -> int:
        """
        Calcula una similitud simple basada en la cantidad de palabras en común,
        utilizando nuestras estructuras personalizadas MySet para representar conjuntos.
        """
        cleaned_query = self.clean_text(query)
        cleaned_doc = self.clean_text(doc_text)
        set_query = MySet()
        # Utilizamos my_split para tokenizar, en lugar de str.split()
        tokens_query = my_split(cleaned_query)
        for token in tokens_query:
            set_query.add(token)
        set_doc = MySet()
        tokens_doc = my_split(cleaned_doc)
        for token in tokens_doc:
            set_doc.add(token)
        inter = set_query.intersection(set_doc)
        count = 0
        for _ in inter:
            count += 1
        return count

    def query(self, query_text: str, n_results: int = 3, where=None):
        """
        Realiza una búsqueda en la colección utilizando la similitud simple.
        Se recorre la estructura MyDict y se seleccionan los mejores candidatos.
        El parámetro 'where' es opcional y permite filtrar usando un diccionario con la clave "$and".
        """
        cleaned_query = self.clean_text(query_text)
        candidates = MyList()  # Cada candidato se representará como una tupla: (score, doc_id, entry)
        
        # Iteramos sobre los elementos de nuestro MyDict usando items_iter()
        for pair in self.documents.items_iter():
            doc_id = pair.key
            entry = pair.value  # entry es un MyDict con las claves "document" y "metadata"
            
            # Si se especifica un filtro 'where', verificamos cada condición.
            if where:
                match = True
                if isinstance(where, dict) and "$and" in where:
                    conditions = where["$and"]
                    for cond in conditions:
                        for key, value in cond.items():
                            if entry.get(key) != value:
                                match = False
                                break
                        if not match:
                            break
                elif isinstance(where, dict):
                    for key, value in where.items():
                        if entry.get(key) != value:
                            match = False
                            break
                elif isinstance(where, list):
                    for cond in where:
                        for key, value in cond.items():
                            if entry.get(key) != value:
                                match = False
                                break
                        if not match:
                            break
                if not match:
                    continue

            doc_text = entry.get("document")
            score = self.simple_similarity(query_text, doc_text)
            candidate = (score, doc_id, entry)  # Usamos una tupla; aquí es indispensable usar tuplas nativas
            candidates.append(candidate)
        
        # Ordenamos los candidatos usando nuestra función personalizada sort_mylist
        sort_mylist(candidates, key_func=lambda c: c[0], reverse=True)
        top_candidates = MyList()
        count = 0
        for candidate in candidates:
            if count >= n_results:
                break
            top_candidates.append(candidate)
            count += 1

        docs = MyList()
        ids = MyList()
        metadatas = MyList()
        for candidate in top_candidates:
            docs.append(candidate[2].get("document"))
            ids.append(candidate[1])
            metadatas.append(candidate[2].get("metadata"))
        result = MyDict()
        result.set("documents", docs)
        result.set("ids", ids)
        result.set("metadatas", metadatas)
        return result

    def upsert(self, document: str, metadata: dict, id: str = None):
        """
        Inserta o actualiza un documento en la colección.
        Se genera un nuevo ID si no se proporciona.
        """
        if id is None:
            id = str(uuid4())
        # Creamos un MyDict para almacenar el documento y su metadata
        entry = MyDict()
        entry.set("document", document)
        entry.set("metadata", metadata)
        self.documents.set(id, entry)

    def contains(self, document: str, where: list = []):
        """
        Verifica si un documento ya existe en la colección, aplicando (opcionalmente) un filtro.
        Retorna una tupla: (bool, resultado de query).
        """
        result = self.query(document, n_results=1, where={"$and": where})
        ids_list = result.get("ids")
        count = 0
        for _ in ids_list:
            count += 1
        found = (count > 0)
        return found, result

    def ingest(self, folder_path: str = "./data/", split_files: bool = True):
        """
        Lee archivos desde una carpeta (y subcarpetas) e ingiere su contenido en la colección.
        Utiliza DocumentReader para leer cada archivo.
        Si split_files es True, el contenido se divide en fragmentos (chunks) usando nuestro método split.
        """
        print(f"Ingesting files in {folder_path}...")
        action = "Agregando"
        items = os.listdir(folder_path)  # Uso nativo: os.listdir() es indispensable
        for item in items:
            item_path = os.path.join(folder_path, item)
            path = os.path.normpath(item_path)  # Uso nativo: normpath() es indispensable
            if os.path.isfile(item_path):  # Uso nativo: es necesario para chequear archivos
                title = os.path.splitext(item)[0]  # Uso nativo: os.path.splitext()
                content = DocumentReader(item_path).read_file()
                if content is None:
                    continue
                if split_files:
                    split_content = self.split(content)
                    i = 0
                    for text in split_content:
                        is_contained, result = self.contains(
                            text,
                            [
                                {"title": title},
                                {"path": path},
                                {"category": path.split("\\")[2]},  # Uso nativo: split() en string
                                {"chunk_position": i},
                            ]
                        )
                        if is_contained:
                            id = str(result.get("ids").get(0))  # Uso nativo para conversión a str
                            action = "Actualizando"
                            creation_date = result.get("metadatas").get(0).get("creation_date")
                            update_date = str(datetime.now())
                        else:
                            id = str(uuid4())
                            action = "Agregando"
                            creation_date = str(datetime.now())
                            update_date = creation_date
                        self.upsert(
                            text,
                            metadata={
                                "title": title,
                                "path": path,
                                "category": path.split("\\")[2],  # Uso nativo
                                "creation_date": creation_date,
                                "update_date": update_date,
                                "chunk_position": i,
                            },
                            id=id,
                        )
                        logging.info(
                            f"{self.name}: {action} archivo: {title}, ruta: {path}, cantidad de chunks: {len(split_content)}"
                        )
                        i += 1
                else:
                    is_contained, result = self.contains(
                        content,
                        [
                            {"title": title},
                            {"path": path},
                            {"category": path.split("\\")[2]},  # Uso nativo
                        ]
                    )
                    if is_contained:
                        id = str(result.get("ids").get(0))
                        action = "Actualizando"
                        creation_date = result.get("metadatas").get(0).get("creation_date")
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
                            "category": path.split("\\")[2],  # Uso nativo
                            "creation_date": creation_date,
                            "updated_date": update_date,
                        },
                        id,
                    )
                    logging.info(
                        f"{self.name}: {action} archivo: {title}, ruta: {path}"
                    )
            elif os.path.isdir(item_path):  # Uso nativo: es indispensable para iterar directorios
                self.ingest(item_path, split_files=split_files)

if __name__ == "__main__":
    from pprint import pprint

    notes = Collection("notes")
    examples = Collection("examples")

    notes.ingest(folder_path="data/redes_sociales")
    examples.ingest(folder_path="data/examples", split_files=False)

    query = "¿Cómo normalizar una tabla en cuarta forma normal?"
    print("\nQuery:", query)
    print("Notes:")
    pprint(notes.query(query))
    print("-" * 140)
    print("Examples:")
    # pprint(examples.query(query, 1))

    ### Esto es un comentario y ya
