# Fundamentos de calidad de software

- Usar la terminología correctamente
- Identificar los tipos de errores en el software
- Entender los diferentes puntos de vista en calidad de software
- Definir la garantía de calidad de software
- Entender los modelos de negocios con sus respectivos riesgos

## Calidad de software

El software se puede observar en muchos sectores de negocios, por lo que se debe identificar las prácticas específicas para cada uno de estos sectores. La guía de ingeniería de software (SWEBOK) constituye el primer censo desarrollado para los fundamentos de los ingeniero de software. En este se define la calidad de software en 4:

- Fundamentos de calidad
	- Cultura y ética
	- Valor y costo de calidad
	- Modelos y calidad de características
	- Mejora de la calidad
	- Seguridad
- Gestión de procesos de calidad
	- Garantía de calidad
	- Verificación y validación
	- Reseñas y auditorías
- Consideraciones practicas
	- Requerimientos
	- Caracterización de defectos
	- Técnicas de gestión  de calidad
	- Medición de calidad
- Herramientas de calidad
### Definiciones básicas

| Concepto | Definición |
| ---- | ---- |
| Software | Conjunto de instrucciones que componen un programa |
| Sotfware source code | Instrucciones de un software |
| Aplicación | Conjunto de programas |
| Sistema de información | Interacción entre la aplicación y el sistema o hardware |
| Programas | Son las intrucciones que fueron traducidos a código, con buen diseño y testeo, ademas aceptado por los clientes |
| Trámites |  |
| Reglas | Son las reglas de negocio |
| Documentación asociada | Son todos los tipos de documentación util para entender el producto, comunicarlo, revisarlo, testearlo y mantenerlo. |
| Datos | Es la información que está guardada, modelada y estandarizada |
| Firmware | Está presente en productos comerciales del mercado masivo y controla máquinas y dispositivos utilizados en nuestra vida diaria. |
| Ciclo de vida | Evolución de un sistema, producto, servicio, proyecto |
| Desarrollo del ciclo de vida | Es el proceso que contiene las actividades que requieren análisis, diseño, codificar, integrar, testear, instalar y darle soporte |
No es suficiente solo garantizar buen código para la calidad de un sistema, ya que este es más complejo, se compone de elemento e interacciones que deben ser aseguradas

## Errores, defectos y fallos

Palabras comunes para problemas de software:
- Crash
- Error
- Defect
- Bug
- Broke down
- Problem
- Failure

Cada palabra se le asocia a un tipo de problema distinto

- Error: Ingresado por un humano
- Defect: Error detectado
- Failure: Defecto ejecutado

Se puede decir que un error es algo mal programado que no fue detectado en su momento, pueden ocurrir en cualquier fase del ciclo de vida, un defect es cuando un programa tiene un comportamiento no deseado, deben ser identificados antes de enviar a producción y que se vuelvan failures y un failure es cuando el software no cumple con las expectativas o los requisitos del usuario debido a un defecto.

Es importante detectar correctamente los errores para poder estudiarlos, según Beizer (1990) [BEI 90], los errores se distribuyen así:

- 25% structural; 
- 22% data; 
- 16% functionalities implemented; 
- 10% construction/coding; 
- 9% integration;
- 8% requirements/functional specifications; 
- 3% definition/running tests; 
- 2% architecture/design; 
- 5% unspecified.
Muchos de los defectos son limitados y fáciles de corregir, en gran medida vienen de otros lugares fuera del código (Requerimientos, actividades de arquitectura). El pobre entendimiento del diseño es un problema recurrente en los errores. Algunos de los más comunes son:

1) problemas con la definición de requisitos; 
2) mantener una comunicación efectiva entre cliente y desarrollador; 
3) desviaciones de las especificaciones; 
4) errores de arquitectura y diseño; 
5) errores de codificación (incluido el código de prueba); 
6) incumplimiento de los procesos/procedimientos vigentes; 
7) revisiones y pruebas inadecuadas; 
8) errores de documentación.

### Problemas definiendo requerimientos

Los errores más comunes recurren a no:
- Identificar los stakeholders que participan.
- Gestionar las reuniones.
- Crear técnicas que identifiquen las diferencias entre deseos, expectativas y necesidades
- Tener una documentación limpia y concisa de los requerimientos funcionales, de desempeño, obligaciones y propiedades de sistemas futuros
- Aplicar técnicas sistemáticas para la obtención de requisitos.
- Gestionar prioridades y cambios

### Mantener comunicaciones efectivas entre el cliente y el desarrollador

Los errores también pueden darse por malos entendidos entre el personal del software y los clientes. Es ideal que la empresa use un lenguaje no técnico y tratar de llevar los términos a la realidad del usuario. Los errores más usuales son:

- Entendimiento pobre de las instrucciones
- El cliente quiere resultados inmediatos
- El cliente no se toma el tiempo de leer la documentación
- Entendimiento pobre de los cambios requeridos por los desarrolladores
- Que el analista no acepte cambios durante la definición de requisitos y la fase de diseño.

Para evitarlos:
- Tomar notas en cada reunión
- Revisar los documentos
- Ser consistente con el uso de términos y el glosario de desarrollo
- Informar a los clientes el costo de las especificaciones
- Elegir una forma de desarrollo que permita cambios
- Enumerar cada requerimiento

### Desviaciones para especificaciones

Esto pasa cuando un desarrollador interpreta incorrectamente un requerimiento y hace el software según su comprensión, estos errores generalmente se ven en el ciclo de desarrollo o el uso del software. También sucede cuando se reúsa código sin adaptarlo a los nuevos requerimientos, cuando se eliminan partes de los requerimientos por presupuesto o tiempo.

### Arquitectura y diseño de errores

### Errores de código
### Incumplimiento de los procesos/procedimientos actuales
### Revisiones y test inadecuados
### Errores de documentación
## Calidad de software
Es la capacidad de un producto de satisfacer e implementar las necesidades, pero también es cumplir con las expectativas del cliente que no están en la documentación, esta calidad depende de cada cliente, ya que en parte va con la subjetividad

## Aseguramiento de calidad

- Plan de calidad sobre los aspectos del producto
- Actividades sistémicas que indique las correcciones requeridas
- Tecnicas de QA para demostrar el nivel de calidad obtenido

## Modelos de negocios y la elección de las prácticas de ingeniería de software

Un modelo de negocios describe la relación de como una organización crea, distribuye y captura valor, tanto económico como social. Es importante definir los controladores de la empresa que da valor a los consumidores, entender estos modelos nos ayuda a:

- Evaluar la efectividad de las nuevas practicas para la organización o para un proyecto
- Aprendes prácticas de software de otros campos
- Entender el contexto que promueve colaboración con los miembros de otras culturas
- Integración sencilla en un nuevo trabajo.

### Elección de la práctica de software

| Modelo de Negocio | Descripción | Cómo se logra | Diferenciación | 
| -------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | 
| **Sistemas personalizados escritos por contrato** | Desarrollo de sistemas a medida para clientes individuales mediante contratos detallados. | Trabajo colaborativo con el cliente para comprender sus necesidades. Desarrollo basado en especificaciones del contrato. | Personalización extrema para adaptarse a requisitos específicos de cada cliente. |
| **Software personalizado escrito internamente** | Desarrollo interno de software para satisfacer necesidades operativas específicas de la empresa. | Establecimiento de un equipo de desarrollo interno. Diseño, implementación y mantenimiento del software a largo plazo. | Propiedad y control total del software por parte de la empresa para mayor flexibilidad y adaptabilidad. |
| **Software para el mercado masivo** | Desarrollo de software con la intención de comercializarlo para un público amplio. | Análisis de mercado para identificar oportunidades. Creación de productos escalables y comercialización masiva. | Escalabilidad y capacidad de llegar a un mercado más amplio ofreciendo soluciones estándar. | 
| **Firmware comercial y de mercado masivo** | Desarrollo de firmware para dispositivos hardware de consumo masivo. | Diseño y desarrollo de firmware para integración con hardware específico. Comercialización centrada en la eficiencia y la compatibilidad. | Eficiencia y compatibilidad con dispositivos de hardware específicos en productos electrónicos de consumo masivo. |
## Ejercicios

**1.1 Diferencia entre defecto, error y fallo:**

- **Defecto:** Imperfección en el código que puede causar un comportamiento inesperado. Ya existe en el código, a la espera de manifestarse.
- **Error:** Equivocación durante el desarrollo, como un error de codificación o un fallo lógico en el diseño. Representa la acción de introducir el defecto.
- **Fallo:** Manifestación observable de un defecto que causa que el software produzca resultados incorrectos o inesperados. Es el impacto negativo del error en la funcionalidad del software.

**1.2 Estudios de Beizer sobre la ocurrencia de errores:**

Los estudios de Boris Beizer sugieren que la mayoría de los errores de software (alrededor del 60%) ocurren durante las fases de requisitos y diseño, incluso aunque se dedica un pequeño esfuerzo de desarrollo a estas. Esto destaca la importancia de la verificación temprana y las prácticas de calidad.

**1.3 Curvas de confiabilidad de software vs. hardware:**

- **Curva de confiabilidad del software:** Suele seguir una curva de bañera, con muchos defectos iniciales, un período estable después de corregirlos y luego una degradación gradual debido al envejecimiento y los cambios.
- **Curva de confiabilidad del hardware:** A menudo sigue una curva de campana, con una mortalidad infantil temprana, un período estable largo y luego un desgaste rápido al final. El software puede evitar teóricamente el desgaste mediante actualizaciones y mejoras.

**1.4 Ocho categorías de causas de errores:**

**Situaciones:**

- **Entorno de desarrollo:** Recursos limitados, herramientas inadecuadas, comunicación deficiente, plazos poco realistas, presión para tomar atajos.
- **Entorno de mantenimiento:** Cambios frecuentes, documentación incompleta, falta de pruebas de regresión, informes de problemas poco claros.

**Ingenieros de software:**

- Fatiga, falta de formación, requisitos poco claros, mala comprensión del sistema, habilidades de prueba inadecuadas.

**Gerentes de ingeniería de software:**

- Planificación inadecuada, objetivos poco claros del proyecto, presupuestos poco realistas, falta de procesos de control de calidad, personal insuficiente.

**1.5 Diferentes perspectivas sobre la calidad del software:**

- **Cliente:** Se centra en la funcionalidad, el cumplimiento de los requisitos, la rentabilidad y el retorno de la inversión.
- **Usuario:** Se preocupa por la usabilidad, la confiabilidad, el rendimiento y la satisfacción general con el software.
- **Ingeniero de software:** Preocupado por la calidad del código, el cumplimiento de los estándares, los desafíos técnicos y el orgullo personal por su trabajo.

**1.6 Discrepancia de necesidades y sus causas:**

- **Origen de las necesidades:** Las necesidades del cliente pueden provenir de diversas fuentes como estudios de mercado, comentarios de los usuarios, objetivos comerciales internos o requisitos reglamentarios.
- **Causas de la discrepancia:** Falta de comunicación, malentendidos, especificaciones incompletas, cambio de prioridades, falta de conocimiento del dominio, limitaciones técnicas.

**1.7 Modelos de negocio y requisitos de SQA:**

Los modelos de negocio definen cómo una organización crea y entrega valor. Diferentes modelos (por ejemplo, suscripción, freemium, pago por uso) conducen a diferentes prioridades para SQA. Por ejemplo, un modelo freemium podría enfatizar el rendimiento y la escalabilidad, mientras que un modelo de suscripción podría priorizar el tiempo de actividad y la seguridad de los datos.

**1.8 QA vs. control de calidad:**

- **QA:** Enfoque proactivo centrado en la prevención de defectos mediante actividades como análisis de requisitos, evaluación de riesgos, mejora de procesos y auditorías.
- **Control de calidad:** Enfoque reactivo centrado en la detección y corrección de defectos mediante pruebas, inspección y reelaboración.