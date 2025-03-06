
# --- Implementación de MyList (lista enlazada) ---
class MyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyList:
    def __init__(self):
        self.head = None
        self._length = 0

    def append(self, item):
        new_node = MyNode(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._length += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __len__(self):
        return self._length

    def get(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Índice fuera de rango")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

# --- Implementación de MyDict (diccionario básico) ---
class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyDict:
    def __init__(self):
        self.items = MyList()  # Almacenaremos KeyValuePair en una lista enlazada

    def set(self, key, value):
        for pair in self.items:
            if pair.key == key:
                pair.value = value
                return
        self.items.append(KeyValuePair(key, value))

    def get(self, key, default=None):
        for pair in self.items:
            if pair.key == key:
                return pair.value
        return default

    def contains(self, key):
        for pair in self.items:
            if pair.key == key:
                return True
        return False

    def keys(self):
        keys_list = MyList()
        for pair in self.items:
            keys_list.append(pair.key)
        return keys_list

    def items_iter(self):
        return iter(self.items)

# --- Implementación de MySet (conjunto básico) ---
class MySet:
    def __init__(self):
        self._dict = MyDict()  # Usamos MyDict para almacenar elementos, donde la clave es el elemento

    def add(self, element):
        if not self.contains(element):
            self._dict.set(element, True)

    def contains(self, element):
        return self._dict.contains(element)

    def intersection(self, other):
        result = MySet()
        for pair in self._dict.items_iter():
            if other.contains(pair.key):
                result.add(pair.key)
        return result

    def __iter__(self):
        return iter(self._dict.keys())

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count

# --- Función auxiliar: ordenar MyList (bubble sort) ---
def sort_mylist(mylist, key_func, reverse=False):
    if len(mylist) < 2:
        return
    changed = True
    while changed:
        changed = False
        current = mylist.head
        while current is not None and current.next is not None:
            a = key_func(current.data)
            b = key_func(current.next.data)
            if (a < b and reverse) or (a > b and not reverse):
                current.data, current.next.data = current.next.data, current.data
                changed = True
            current = current.next

# --- Función para dividir un string en tokens y retornar un MyList ---
def my_split(text):
    tokens = MyList()
    token = ""
    for char in text:
        if char.isspace():
            if token:
                tokens.append(token)
                token = ""
        else:
            token += char
    if token:
        tokens.append(token)
    return tokens

# --- Clase para empaquetar resultados en queries ---
class Candidate:
    def __init__(self, score, doc_id, entry):
        self.score = score
        self.doc_id = doc_id
        self.entry = entry
class MyHash:
    def __init__(self, capacity=101):
        """
        Inicializa la tabla hash con un número fijo de cubetas.
        capacity: número de cubetas (preferiblemente un número primo).
        """
        self.capacity = capacity
        # Uso nativo: Se utiliza una lista nativa para almacenar las cubetas (indispensable para indexar).
        self.buckets = [MyList() for _ in range(capacity)]
    
    def _hash(self, key):
        """
        Calcula el índice para la clave.
        - Si la clave es un entero, usa key % capacity.
        - Si la clave es una cadena, usa una función hash simple que combina los caracteres.
        """
        if isinstance(key, int):
            return key % self.capacity
        elif isinstance(key, str):
            h = 0
            for ch in key:
                h = (h * 31 + ord(ch)) % self.capacity  # 31 es un número primo típico para hash.
            return h
        else:
            raise TypeError("Unsupported key type: " + str(type(key)))
    
    def set(self, key, value):
        """
        Inserta o actualiza el par (clave, valor) en la tabla hash.
        Se calcula el índice y se inserta el par en la cubeta correspondiente.
        Si la clave ya existe, se actualiza el valor.
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        # Iterar sobre la cubeta (MyList) para ver si ya existe la clave.
        for pair in bucket:
            if pair.key == key:
                pair.value = value
                return
        # Si la clave no se encuentra, se agrega un nuevo KeyValuePair a la cubeta.
        bucket.append(KeyValuePair(key, value))
    
    def get(self, key, default=None):
        """
        Retorna el valor asociado a la clave. Si la clave no existe, retorna default.
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                return pair.value
        return default
    
    def contains(self, key):
        """
        Retorna True si la clave existe en la tabla hash, o False en caso contrario.
        """
        return self.get(key) is not None
