2024-03-05

Recordemos que al tratar de estimar esfuerzos se intenta determinar en detalle el costo, la duración y las personas. Hay técnicas para estimar esfuerzos:
- Técnicas algorítmicas
	- Puntos de función
	- **Puntos de caso de uso:** Funcionalidades y actores
- Técnicas humanas
	- Juicio de expertos
- Técnicas de machine learning
	- Redes neuronales
	- Ingeniería de software basado en ML

# Puntos de caso de uso

Al igual que los puntos de función, es bastante conservadora. Es un método para estimar el tamaño y la complejidad de un proyecto teniendo en cuenta sus requisitos funcionales. Un caso de uso tiene un objetivo, unas precondiciones (como debe estar el sistema para iniciar la ejecución del caso de uso), postcondiciones (como debe quedar el sistema después de la ejecución). A cada paso se le denomina transacción, describen que sucede en una condición normal, pero no es una normal, es una guía.

## Pasos

### 1. Factor de peso de los actores sin ajustar (UAW)

Consiste en la evaluación de la complejidad de los actores con los que interactúa el sistema, dependiendo de como se interactúe 

| Tipo de Actor | Descripción                                                                                                                              | Factor |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Simple        | Otro sistema que intectua con el sistema a desarrollar mediante una interfaz de programación                                             | 1      |
| Medio         | Otro sistema interactuando a través de un protocolo (Ejemplo TCP-IP) o una persona interactuando a traves de una interfaz en modo texto. | 2      |
| Complejo      | Una persona que interactua con el sistema mediante una interfaz gráfica (GUI)                                                            | 3      |
$$UAW=\sum_{i=0}^nFactorActor_i \text{ donde n = número de actores}$$


### 2. Factor de peso de los casos de uso sin ajustar (UUCW)

Se toma cada caso de uso y se contabiliza las transacciones

| Tipo de Actor | Descripción                                                                                                                              | Factor |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Simple        | Otro sistema que intectua con el sistema a desarrollar mediante una interfaz de programación                                             | 1      |
| Medio         | Otro sistema interactuando a través de un protocolo (Ejemplo TCP-IP) o una persona interactuando a traves de una interfaz en modo texto. | 2      |
| Complejo      | Una persona que interactua con el sistema mediante una interfaz gráfica (GUI)                                                            | 3      |
$$UUCW=\sum_{i=0}^nFactorCasoUso_i$$
### 3. Puntos de Caso de Uso sin Ajustar (UUCP)

Se puede proyectar una breve descripción de cada caso de uso, en el cual se describe de forma breve la funcionalidad que éste debe brindar.
El UUCP son los puntos de casos de uso sin ajustar, esto nos puede servir para tener una idea un poco m´as precisa de la dificultad de los casos de uso e interfaces, tomando en cuenta los pesos de los actores (UAW) y los pesos de los casos de uso (UUCW).
$$UUCP = UAW + UUCW$$
### 4. Factores de complejidad técnica (TCF)

![[Pasted image 20240305144953.png]]
![[Pasted image 20240305145058.png]]

$$TFactor = \sum_{i=1}^{13} Factor_i \text{ } $$$$ TCF = 0,6 + (0,01 ∗ TFactor)$$
### 5. Factores ambientales (EF)

![[Pasted image 20240305145949.png]]

$$EFactor = \sum_{i=1}^8 Factor_i$$ $$ EF = 1,4 + (−0,03 ∗ EFactor)$$
### 6. Puntos de caso de uso ajustados (UCP)

$$UCP = UUCP*TCF*EF$$
### 7. Esfuerzo horas-hombre (E)

Este cálculo se realiza con el fin de tener una aproximación del esfuerzo, pensando solo en el desarrollo según las funcionalidades de los casos de uso.
Primero se debe contar la cantidad de factores ambientales del E1 al E6 que tienen una puntuación mayor a 3, también contar la cantidad de estos mismos del E7 y E8 que son menores que -3. SUMAR AMBAS CANTIDADES

![[Pasted image 20240305150330.png]]
$$E = UCP ∗ CF$$

Al realizar la multiplicación del UCP por las horas- persona, se consigue un esfuerzo estimado, que representa una parte del total del esfuerzo de todo el proyecto, generalmente un 40 %. Este 40 % se refiere al esfuerzo total para el desarrollo de la funcionalidades especificadas en los Casos de Uso.
![[Pasted image 20240305150402.png]]
# Taller

Estimar el esfuerzo por PF y PCU para desarrollar una aplicación que gestione una natillera, representar el proceso en un mapa mental y subir el json.