2024-08-13
# Naive bayes

El teorema de bayes es una ecuación que describe la relación de probabilidades condicionales de cantidades estadísticas. En la clasificación bayesiana estamos interesados en encontrar la probabilidad de que ocurra una clase.

$$P(Clase | Datos) = \frac{P(Datos|Clase)*P(Clase)}{P(Datos)}$$
Clases: Setosa, Versicolor, Virginica
# Métricas

## Matriz de confusión

|                   | Positivo predicho       | Negativo predicho       |
| ----------------- | ----------------------- | ----------------------- |
| **Positivo real** | Verdadero positivo (TP) | Falso positivo (FN)     |
| **Negativo real** | Falso negativo (FP)     | Verdadero negativo (TN) |
## Accuracy

También conocida como exactitud.
$$Accuracy=\frac{TP+TN}{FP+FN+TP+TN}​$$
## Recall

También conocido como sensibilidad
$$Recall=\frac{TP}{TP+FN}$$
## Precision

$$Precision=\frac{TP}{TP+FP}$$
## F1-Score

Es el equilibrio entre la precisión y la sensibilidad.

$$F1Score = \frac{2*Precision*Recall}{Precision + Recall}$$