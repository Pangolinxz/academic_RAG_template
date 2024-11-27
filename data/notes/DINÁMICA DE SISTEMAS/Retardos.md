2024-08-13
# Retardos

Es un proceso cuyos resultados quedan atrás de sus causas en alguna forma o que existe una acumulación igual a la diferencia entre lo que entra y lo que sale, son una fuente crítica de comportamiento dinámico en casi todos los sistemas.

| Peligros      | Beneficios                           |
| ------------- | ------------------------------------ |
| Inestabilidad | Filtración de variabilidad indeseada |
| Oscilación    | Separación de señales y ruidos       |
Los retardos pueden generar:
- Ansiedad
- Tranquilidad
- Inquietud
- Incertidumbre
- Gastos
- Estrés

> *"Los retardos siempre crean peligros"* - **Cervantes**

> *"Nunca hagas hoy lo que puedas dejar para mañana. El retardo puede arrojar mayor claridad sobre lo que debe hacerse"* - **Aaron Burr**

**¿Cómo se generan?**
- Medición y reportes de información
- Tomar decisiones
- Afectar el estado de un sistema

**Los modeladores necesitan...**
- Entender el comportamiento del retardo
- Representarlo
- Escoger entre varios tipos de retardo
- Estimar su duración
## Tipos

![[Pasted image 20240813125107.png]]
### Orden 1
**Retardo de material:** Existen unidades físicas moviéndose a través del proceso. Por ejemplo:
- Flujo de un producto a través de una cadena de abastecimiento
- Envío de cartas
- Construcción de edificios

![[Pasted image 20240813130014.png]]
$$Salida = \frac{Nivel}{\text{Tiempo de retardo}}$$

### Orden 3
Es similar a tener tres retardos de orden 1.

![[Pasted image 20240813130136.png]]
$$Retardo = \frac{\text{Tiempo de retardo}}{3}$$

$$Tasa2 = \frac{\text{Nivel 1}}{\text{Retardo}}$$
$$Tasa3 = \frac{\text{Nivel 2}}{\text{Retardo}}$$
$$Salida = \frac{\text{Nivel 3}}{\text{Retardo}}$$
### Orden infinito

Las entradas son iguales a la salida

![[Pasted image 20240813130538.png]] 
### De información

![[Pasted image 20240813132307.png]]
- Diferencia entre el retardo de material y retardo de información de orden 2