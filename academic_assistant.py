import logging
from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

# Importamos nuestra implementación de Collection (que utiliza nuestras propias estructuras)
from my_structures import Collection

# Función auxiliar para convertir nuestra estructura de lista personalizada (MyList) a una lista nativa de Python.
def custom_list_to_native(my_list):
    native_list = []
    for item in my_list:
        native_list.append(item)
    return native_list

class AcademicAssistant:
    def __init__(self):
        self.base_path = os.path.abspath(os.path.dirname(__file__))
        load_dotenv(os.path.join(self.base_path, ".env"))

        self.HF_API_KEY = os.getenv("HF_API_KEY")
        self.MODEL = "microsoft/Phi-3.5-mini-instruct"
        self.client = InferenceClient(api_key=self.HF_API_KEY)

        # Inicializamos las colecciones usando nuestra implementación personalizada (Collection)
        self.notes = self.initialize_collection("notes")
        self.examples = self.initialize_collection("examples")

        self.logger = self.configure_logger()

    def configure_logger(self):
        log_file = os.path.join(self.base_path, 'academic_assistant.log')
        if not os.path.exists(log_file):
            open(log_file, 'w').close()

        logger = logging.getLogger('AcademicAssistantLogger')
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger

    def initialize_collection(self, collection_name):
        return Collection(collection_name)

    def get_notes(self, query):
        # Obtenemos la respuesta de la consulta usando nuestra colección personalizada
        response = self.notes.query(query)
        # 'response' es un objeto MyDict; extraemos el valor asociado a "documents", que es un MyList
        custom_docs = response.get("documents")
        # Convertimos nuestra MyList a una lista nativa para poder unir los strings
        docs = custom_list_to_native(custom_docs)
        retrieved_notes = "\n".join(docs)
        self.logger.info(f"Notas recuperadas: {retrieved_notes}")
        return retrieved_notes

    def get_examples(self, query):
        response = self.examples.query(query)
        custom_docs = response.get("documents")
        docs = custom_list_to_native(custom_docs)
        retrieved_examples = "\n".join(docs)
        self.logger.info(f"Ejemplos recuperados: {retrieved_examples}")
        return retrieved_examples

    def read_template(self, template_name):
        template_path = os.path.join(self.base_path, "data", "templates", template_name, "prompt_template.txt")
        with open(template_path, "r") as template_file:
            template = template_file.read()
        self.logger.info(f"Plantilla leída: {template_name}")
        return template

    def select_prompt_template(self, prompt_selection):
        if prompt_selection == "repaso":
            return self.read_template("summary")
        else:
            return self.read_template("test_preparation")

    def generate_response(self, user_input, prompt_template):
        self.logger.info(f"Entrada del usuario: {user_input}")
        retrieved_notes = self.get_notes(user_input)
        retrieved_examples = self.get_examples(user_input)
        response = self.client.chat_completion(
            model=self.MODEL,
            messages=[
                {"role": "system", "content": prompt_template.format(
                    retrieved_notes=retrieved_notes,
                    retrieved_examples=retrieved_examples,
                    user_input=user_input
                )},
                {"role": "user", "content": user_input}
            ],
            temperature=0.0,
            max_tokens=1800
        )
        response_content = response["choices"][0]["message"]["content"]
        self.logger.info(f"Respuesta generada: {response_content}")
        return response_content

    def run(self):
        print("Bienvenido al asistente académico.")
        prompt_template = self.select_prompt_template("repaso")
        if prompt_template:
            print("¡Listo! Puedes empezar a hacer preguntas.")
            try:
                while True:
                    user_input = input("Introduce tu pregunta: ")
                    print("Procesando...")
                    response_content = self.generate_response(user_input, prompt_template)
                    print(f"Aquí está la respuesta: \n{response_content}")
            except KeyboardInterrupt:
                self.logger.info("Programa terminado por el usuario.")
                print("¡Hasta luego!")
                exit()
            except Exception as e:
                self.logger.error(f"Error en la llamada al modelo: {str(e)}")
                print(f"Error en la llamada al modelo: {str(e)}")
                exit()
        else:
            self.logger.error("Error al cargar el template.")
            print("Error al cargar el template.")
            exit()

if __name__ == "__main__":
    assistant = AcademicAssistant()
    assistant.run()
