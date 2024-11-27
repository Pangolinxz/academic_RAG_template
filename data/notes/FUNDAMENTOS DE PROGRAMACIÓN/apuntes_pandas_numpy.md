Claro, aquí tienes las notas detalladas explicando cada concepto nuevo antes de usarlo, para asegurar una comprensión más profunda:

---

# **Curso de Manipulación y Transformación de Datos con Pandas y NumPy**

---

## **NumPy**

NumPy (Numerical Python) es una biblioteca fundamental para realizar cálculos numéricos y científicos en Python. Proporciona soporte para arrays multidimensionales (similares a las listas, pero mucho más eficientes y rápidos) y herramientas para manipular estos arrays.

---

### **Creación y Transformación de Arrays**

Un **array** es una estructura de datos que contiene múltiples valores del mismo tipo organizados en filas y columnas. En NumPy, un array puede ser unidimensional (vector), bidimensional (matriz) o tener más dimensiones (tensor).

#### **Crear un array**
```python
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

#### **Obtener la forma del array**
El método `.shape` devuelve la cantidad de filas y columnas de un array.
```python
print(arr.shape)  # (2, 3): 2 filas y 3 columnas
```

#### **Cambiar la forma de un array**
El método `reshape` reorganiza los elementos de un array sin cambiar su contenido. El parámetro opcional `'C'` indica el orden de lectura de los datos: **por filas (C)**, **por columnas (F)** o **adaptativo (A)**.
```python
reshaped = np.reshape(arr, (3, 2), 'C')
print(reshaped)  
# [[1 2]
#  [3 4]
#  [5 6]]
```

---

### **Funciones para Generar Arrays**

1. **`np.arange`**: Crea un array con valores espaciados uniformemente dentro de un rango definido.
    ```python
    np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
    ```

2. **`np.linspace`**: Crea un array con un número específico de valores entre un rango.
    ```python
    np.linspace(0, 1, 5)  # [0. , 0.25, 0.5 , 0.75, 1.]
    ```

---

### **Estadísticas en Arrays**

NumPy ofrece una amplia variedad de funciones estadísticas básicas que operan sobre arrays.

- **Máximo y mínimo por eje (dimensión):**
    - `axis=0`: Operación por columnas.
    - `axis=1`: Operación por filas.
    ```python
    print(arr.max(axis=0))  # [4, 5, 6]: Máximo por columna
    print(arr.min(axis=1))  # [1, 4]: Mínimo por fila
    ```

- **Índice del mayor o menor valor:**
    ```python
    print(np.argmax(arr))  # Índice del mayor (en el array aplanado)
    ```

- **Funciones estadísticas básicas:**
    - **`np.mean`**: Calcula la media.
    - **`np.median`**: Calcula la mediana.
    - **`np.percentile`**: Calcula un percentil específico.
    ```python
    print(np.mean(arr))        # Promedio
    print(np.median(arr))      # Mediana
    print(np.percentile(arr, 50))  # Percentil 50
    ```

---

### **Máscaras Booleanas**

Una **máscara booleana** es un array de valores `True` o `False` generado mediante una condición. Estas máscaras permiten filtrar elementos en un array según esa condición.

#### **Ejemplo:**
```python
mask = arr > 3  # Genera una máscara con True donde el valor > 3
print(mask)
# [[False False False]
#  [ True  True  True]]
print(arr[mask])  # Aplica la máscara para filtrar
# [4 5 6]
```

---

### **Operaciones entre Arrays**

NumPy permite realizar operaciones aritméticas sobre arrays de manera directa y optimizada.

1. **Multiplicar un array por un escalar:**
    ```python
    print(arr * 2)  # [[ 2  4  6]
                    #  [ 8 10 12]]
    ```

2. **Suma y resta de arrays:**
    Los arrays deben tener el mismo tamaño para estas operaciones.
    ```python
    arr2 = np.array([[7, 8, 9], [10, 11, 12]])
    print(arr + arr2)
    ```

3. **Producto punto (dot product):**
    El **producto punto** es una operación algebraica entre dos matrices o vectores.
    ```python
    print(np.dot(arr, arr.T))
    ```

---

## **Pandas**

Pandas es una biblioteca de Python que proporciona estructuras de datos de alto nivel (Series y DataFrames) para manipular y analizar datos.

---

### **Estructuras Principales**

1. **`Series`**: Un vector unidimensional etiquetado (similar a un array).
    ```python
    import pandas as pd
    s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
    print(s)
    ```

2. **`DataFrame`**: Una tabla bidimensional etiquetada.
    ```python
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data)
    print(df)
    ```

---

### **Carga de Archivos**

Pandas permite cargar datos desde archivos como CSV o Excel.

#### **Leer un archivo CSV:**
```python
df = pd.read_csv('data.csv', sep=',', header=0)
```

- `sep`: Especifica el delimitador (ej., coma o tabulación).
- `header`: Indica qué fila se utiliza como encabezado.
- `names`: Permite asignar nombres personalizados a las columnas.

---

### **Indexación con `loc` e `iloc`**

1. **`loc`**: Permite acceder a los datos utilizando etiquetas (nombres de filas o columnas).
    ```python
    print(df.loc[0, 'col1'])  # Acceso a la fila 0 y columna 'col1'
    ```

2. **`iloc`**: Permite acceder a los datos utilizando índices numéricos.
    ```python
    print(df.iloc[0, 1])  # Acceso a la fila 0 y la columna 1
    ```

---

### **Operaciones en Pandas**

1. **Agregar una columna nueva:**
    ```python
    df['new_col'] = [5, 6]
    ```

2. **Eliminar columnas o filas:**
    ```python
    df.drop('col1', axis=1, inplace=True)  # Eliminar columna
    df.drop([0], axis=0, inplace=True)     # Eliminar fila
    ```

3. **Manejo de valores nulos:**
    - **Rellenar nulos:**
        ```python
        df.fillna(0, inplace=True)
        ```

    - **Eliminar filas con nulos:**
        ```python
        df.dropna(inplace=True)
        ```

---

### **GroupBy y Agregación**

El método `groupby` permite agrupar los datos en base a una o más columnas, y luego realizar operaciones de agregación como suma, promedio, etc.

#### **Ejemplo:**
```python
df.groupby('Category')['Value'].sum()
```

---

### **Pivot y Melt**

1. **Pivot**: Reorganiza los datos en forma de tabla dinámica.
    ```python
    df.pivot_table(index='Genre', columns='Year', values='Rating', aggfunc='sum')
    ```

2. **Melt**: Convierte columnas en filas para facilitar transformaciones.
    ```python
    pd.melt(df, id_vars=['Genre'], value_vars=['Year', 'Rating'])
    ```

---

Con esta explicación detallada, puedes comprender cada concepto introducido antes de usarlo en ejemplos prácticos. ¡Espero que sea útil! 😊
