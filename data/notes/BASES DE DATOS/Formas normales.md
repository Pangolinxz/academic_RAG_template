# **Las Cinco Formas Normales en Bases de Datos Relacionales**

La normalización es un proceso que organiza los datos en una base de datos relacional para minimizar redundancias y dependencias. Este proceso se lleva a cabo siguiendo un conjunto de reglas conocidas como formas normales. A continuación, se detallan las primeras cinco formas normales:

---

## **1. Primera Forma Normal (1NF): Eliminar Duplicados y Asegurar la Atomicidad**  

Un esquema está en primera forma normal si:  

1. **Todas las columnas tienen valores atómicos:** Cada celda contiene un único valor, sin listas o conjuntos.  
2. **No hay filas duplicadas:** Cada fila debe ser identificable de forma única, generalmente mediante una clave primaria.  

Ejemplo de violación:  

| Estudiante | Cursos              |  
|------------|---------------------|  
| Juan       | Matemáticas, Física |  

Para llevar esto a 1NF:  

| Estudiante | Curso       |  
|------------|-------------|  
| Juan       | Matemáticas |  
| Juan       | Física      |  

---

## **2. Segunda Forma Normal (2NF): Eliminar Dependencias Parciales**  

Un esquema está en segunda forma normal si:  

1. Está en 1NF.  
2. **No tiene dependencias parciales:** Esto significa que todas las columnas no clave dependen completamente de la clave primaria.  

Ejemplo de violación:  

| ID Curso | Nombre Curso | ID Profesor | Nombre Profesor |  
|----------|--------------|-------------|-----------------|  

Aquí, `Nombre Profesor` depende solo de `ID Profesor`, no de la combinación de `ID Curso` e `ID Profesor`.  

Para llevar esto a 2NF, se divide la tabla:  
**Cursos:**  
| ID Curso | Nombre Curso | ID Profesor |  

**Profesores:**  
| ID Profesor | Nombre Profesor |  

---

## **3. Tercera Forma Normal (3NF): Eliminar Dependencias Transitivas**  

Un esquema está en tercera forma normal si:  

1. Está en 2NF.  
2. **No tiene dependencias transitivas:** Ninguna columna no clave depende de otra columna no clave.  

Ejemplo de violación:  
| ID Curso | Nombre Curso | ID Departamento | Nombre Departamento |  

Aquí, `Nombre Departamento` depende de `ID Departamento`, que no es clave primaria.  

Para llevar esto a 3NF, se crea una nueva tabla para los departamentos:  
**Cursos:**  
| ID Curso | Nombre Curso | ID Departamento |  

**Departamentos:**  
| ID Departamento | Nombre Departamento |  

---

## **4. Cuarta Forma Normal (4NF): Eliminar Dependencias Multivaluadas**  

Un esquema está en cuarta forma normal si:  

1. Está en 3NF.  
2. **No tiene dependencias multivaluadas:** Una dependencia multivaluada ocurre cuando una columna puede tener múltiples valores independientes para una misma clave primaria.  

Ejemplo de violación:  

| ID Proyecto | Tecnologías   | Participantes |  
|-------------|---------------|---------------|  
| 1           | Python        | Ana           |  
| 1           | Python        | Carlos        |  
| 1           | SQL           | Ana           |  
| 1           | SQL           | Carlos        |  

Aquí hay dos dependencias independientes: tecnologías y participantes.  

Para llevar esto a 4NF, se separan en dos tablas:  
**Proyectos-Tecnologías:**  
| ID Proyecto | Tecnología |  

**Proyectos-Participantes:**  
| ID Proyecto | Participante |  

---

## **5. Quinta Forma Normal (5NF): Descomposición para Eliminar Dependencias de Unión**  

Un esquema está en quinta forma normal si:  

1. Está en 4NF.  
2. **No tiene dependencias de unión:** Esto ocurre cuando un conjunto de tablas puede combinarse de múltiples maneras para obtener información redundante.  

Ejemplo de violación:  
Supongamos una relación donde una tabla asocia Proveedores, Productos y Partes. Si cada par (Proveedor-Producto) y (Producto-Parte) es independiente, pero al combinarlos hay redundancia, debemos dividirlas.  

Para llevar esto a 5NF:  
**Proveedor-Producto:**  
| Proveedor | Producto |  

**Producto-Parte:**  
| Producto  | Parte    |  

**Proveedor-Parte:**  
| Proveedor | Parte    |  

---

**Nota:**  
Aunque las cinco formas normales son esenciales para evitar redundancia y anomalías en una base de datos, en la práctica, muchas bases de datos se detienen en la 3NF o 4NF, ya que las normalizaciones avanzadas pueden aumentar la complejidad de las consultas y reducir el rendimiento.
