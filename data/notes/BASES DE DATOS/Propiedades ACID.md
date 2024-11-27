# **Transacciones en Bases de Datos: Conceptos Clave y Propiedades ACID**

Las transacciones son una característica fundamental en las bases de datos, especialmente en las relacionales. Una transacción es una unidad lógica de trabajo que agrupa una o más operaciones sobre la base de datos. Estas operaciones deben ser ejecutadas como un conjunto indivisible, asegurando la integridad de los datos incluso en presencia de fallos o errores.

---

## **¿Qué es una Transacción?**  

Una transacción en bases de datos es una secuencia de operaciones (como insertar, actualizar o eliminar) que se ejecutan como una sola unidad. Por ejemplo, en un sistema bancario, transferir dinero de una cuenta a otra implica dos operaciones:  

1. Restar el monto de la cuenta de origen.  
2. Sumar el monto a la cuenta de destino.  

Ambas operaciones deben ejecutarse juntas para garantizar que no haya inconsistencias en los datos. Si una falla, la transacción completa se deshace.

---

## **Propiedades ACID**  

Las transacciones deben cumplir con las propiedades **ACID**, un conjunto de reglas que garantizan la integridad y confiabilidad de los datos:  

1. **Atomicidad (Atomicity):**  
   - Una transacción debe ejecutarse completamente o no ejecutarse en absoluto. Si ocurre un fallo, todos los cambios realizados durante la transacción deben revertirse.  
   - Ejemplo: En una transferencia bancaria, si se resta dinero de una cuenta pero no se acredita en la otra, la transacción debe revertirse.  

2. **Consistencia (Consistency):**  
   - Una transacción debe llevar la base de datos de un estado válido a otro también válido, cumpliendo todas las reglas de integridad definidas.  
   - Ejemplo: La suma total de dinero en todas las cuentas debe ser igual antes y después de una transferencia.  

3. **Aislamiento (Isolation):**  
   - Las transacciones concurrentes no deben interferir entre sí. Los resultados deben ser los mismos como si se ejecutaran secuencialmente.  
   - Ejemplo: Si dos personas están reservando boletos al mismo tiempo, ninguna debe poder seleccionar el mismo asiento simultáneamente.  

4. **Durabilidad (Durability):**  
   - Una vez que una transacción se completa (es decir, se confirma), sus cambios deben persistir en la base de datos, incluso en caso de fallos en el sistema.  
   - Ejemplo: Después de realizar un pago, el registro de la transacción debe permanecer aunque el sistema falle inmediatamente después.  

---

## **Control de Concurrencia**  

En sistemas donde múltiples usuarios acceden simultáneamente a la base de datos, el control de concurrencia asegura que las transacciones no entren en conflicto. Las técnicas comunes incluyen:  

1. **Bloqueos (Locks):** Restringen el acceso a ciertos datos mientras se ejecuta una transacción.  
   - Bloqueo compartido: Permite consultas pero no modificaciones.  
   - Bloqueo exclusivo: Restringe cualquier acceso.  

2. **Versionado de Datos:** Mantiene múltiples versiones de los datos para evitar bloqueos innecesarios y mejorar el rendimiento en entornos concurridos.  

3. **Control de Conflictos:** Detecta conflictos entre transacciones y toma medidas correctivas, como deshacer una transacción problemática.  

---

## **Niveles de Aislamiento**  

Los sistemas de bases de datos ofrecen diferentes niveles de aislamiento que equilibran rendimiento y consistencia:  

1. **Read Uncommitted:** Permite leer datos no confirmados, lo que puede causar inconsistencias (lecturas sucias).  
2. **Read Committed:** Garantiza que solo se lean datos confirmados, evitando lecturas sucias.  
3. **Repeatable Read:** Asegura que los datos leídos no cambien durante la transacción, evitando lecturas no repetibles.  
4. **Serializable:** Garantiza el aislamiento completo, evitando todas las anomalías, pero con mayor costo en rendimiento.  

---

## **Uso de Transacciones en Bases NoSQL**  

Aunque las bases NoSQL tradicionalmente no priorizan las transacciones como las bases relacionales, muchas han incorporado soporte para transacciones ACID en respuesta a las necesidades modernas. Por ejemplo:  

- **MongoDB:** Soporta transacciones multi-documento en colecciones.  
- **Cassandra:** Ofrece transacciones ligeras (Lightweight Transactions) para ciertas operaciones.  

---

## **Conclusión**  

Las transacciones son esenciales para garantizar la integridad, consistencia y confiabilidad de los datos, especialmente en sistemas críticos como banca, salud y comercio electrónico. La comprensión de sus propiedades y cómo manejar la concurrencia permite diseñar sistemas robustos que satisfagan los requisitos de las aplicaciones modernas.
