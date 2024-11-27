2024-02-27

# Contexto

Para desarrollar el software se debe abordar desde una perspectiva de gestión de proyectos
1)  Análisis de viabilidad
	- Creación de registros
	- Análisis previo de alcance
	- Análisis de riesgos
2) Planificación detallada
	- Análisis detallado del alcance
	- **Realización de estimaciones** (costos, tiempos y personas)
	- Definición del plan Proyecto
	- Negociación del contrato

# ¿Qué es la estimación?

Se refiere a definir los costos, duración y número de personas para desarrollar y entregar un proyecto de software. Implica analizar su alcance, complejidad, requisitos y recursos disponibles para hacer predicciones sobre el esfuerzo que necesita el proyecto, su objetivo es ayudar a los jefes de proyecto y a los equipos de desarrollo a planificar y gestionar sus recursos con eficacia, y garantizar que el proyecto se complete a tiempo y dentro del presupuesto. Permite:
- Planear recursos
- Ayuda a identificar riesgos
- Ayuda a comprender la cumple de la solución requerida
- Siempre se desarrolla la estimación en etapas previas al desarrollo del proyecto

![[Pasted image 20240227142548.png]]

## Plan de proyectos

Es el momento donde se planea el proyectos, los KPIs, se presupuesta, se gestionan los riesgos, se habla con las partes interesadas, medimos el rendimiento}

## Métodos para estimar esfuerzos

- Juicio de expertos: se evalúa la estimación basada en el conocimiento y experiencia de las personas
- Métodos algorítmicos: Son formulas ajustadas que bajo ciertas condiciones nos permiten realizar cálculos
	- Cocomo: Cantidad de líneas de código
	- Puntos de función: Identificar y categorizar las funciones proporcionadas por el software:
		1. Entradas externas (EI) - Los procesos o funciones que reciben datos del usuario o de sistemas externos. 
		2. Salidas externas (EO): procesos o funciones que envían datos al usuario o a sistemas externos. 
		3. Consultas Externas (EQ) - Los procesos o funciones que proporcionan información al usuario sin modificar ningún dato. 
		4. Archivos Lógicos Internos (ILF) - Los almacenes de datos o archivos mantenidos por el sistema
		5. Archivos de Interfaz Externa (EIF) - Los almacenes de datos o archivos que se comparten con otros sistemas.
	- Puntos de casos de uso
	- Métodos basados en inteligencia artificial

### Pasos para el cálculo de los PF

1. Descomponer la aplicación a construir, en funciones elementales a implementar. Para esto se puede utilizar: 
	1. Técnicas de descomposición funcional 
	2. Diagramas de flujos de datos
	3. Listado de las funciones a contemplar
2. Calcular la complejidad de las funciones:  ![[Pasted image 20240227145949.png]]
3. Obtener el total de puntos de función para la aplicación completa: $TotalCuenta = \sum Cuenta$ 
4. Factores de ajuste Fi: A cada pregunta se le asigna un valor desde 0 a 5![[Pasted image 20240227150257.png]]
5. Calcular los Puntos de Función Totales: $PF = TotalCuenta ∗ (0,65 + 0,01 ∗ \sum_{i=1}^{14} Fi)$
6. Determinar el estándar de productividad en $\frac{PF}{hombre∗mes}$ que utilizará la organización medido en Puntos de Función por hombre-mes. Es decir, cuantos $\frac{PF}{mes}$ en promedio, producirá un integrante del equipo. (Algunas organizaciones utilizan valores entre 50 y 75 $\frac{PF}{hombre∗mes}$)
7. Finalmente, calcular el esfuerzo y duración del proyecto utilizando las siguientes ecuaciones: $$E = \frac{PF} {Productividad} [hombre − mes]$$ $$Duracion = \frac{E}{ Numero Personas} [meses]$$
