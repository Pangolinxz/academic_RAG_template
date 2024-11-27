Los sistemas expertos son programas de computadora que utilizan mecanismos de conocimiento e inferencia para proveer consejos, soluciones o recomendaciones en dominios especializados

![[Pasted image 20240215082558.png]]
# ¿Cómo se crean?
1. Identificar el problema y comprender los objetivos del sistema
2. Adquirir conocimientos: conocer reglas y hechos
3. Representar el conocimiento
4. Desarrollar el modo de inferencia

# PROLOG

- **Variables:** empiezan con [A-Z] ∪ _ 
- **Átomos:** constantes – empiezan con [a-z] o ‘entre single quotes’ 
- **Listas:** [1,2,3] 
- **Comentarios:** % 
- **Cut :** ! Para prevenir el backtracking 
- **Conjunción:** , (AND) 
- **Disyunción:** ; (OR) 
- **Negación**: not o \+ 
- **Implicación:** :- 
- **Fin de línea:** . • Diferente de: \= 
- **Bloque de comentario:** /* */

```PROLOG
oracion --> frase_sustantivo, frase_verbo.
frase_sustantivo --> articulo, sustantivo.
frase_verbo --> verbo, frase_sustantivo.
articulo --> [the].
articulo -->[a].
sustantivo --> [cat].
sustantivo --> [bat].
verbo --> [ears].

oracion(A,Z) :- frase_sustantivo(A,B), frase_verbo(B,Z).
frase_sustantivo(A,Z) :- articulo(A,B), sustantivo(B,Z).
frase_verbo(A,Z) :- verbo(A,B), frase_sustantivo(B,Z).
articulo([the|X],X).
articulo([a|X],X).
sustantivo([X|cat],X).
sustantivo([X|bat],X).
verbo([X|eats],X).

% ---------------------OUTPUT---------------------

oracion(X,[])  

X = [the, cat, ears, the, cat]
X = [the, cat, ears, the, bat]
X = [the, cat, ears, a, cat]
X = [the, cat, ears, a, bat]
X = [the, bat, ears, the, cat]
X = [the, bat, ears, the, bat]
X = [the, bat, ears, a, cat]
X = [the, bat, ears, a, bat]
X = [a, cat, ears, the, cat]
X = [a, cat, ears, the, bat]
X = [a, cat, ears, a, cat]
X = [a, cat, ears, a, bat]
X = [a, bat, ears, the, cat]
X = [a, bat, ears, the, bat]
X = [a, bat, ears, a, cat]
X = [a, bat, ears, a, bat]
```