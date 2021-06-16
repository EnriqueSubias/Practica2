# Informe Practica 2

Práctica 2 de Algorítmica y Complejidad

# Greddy
## Greddy Recursivo
Uso:
    $ ./aqueducte.py <fitxer entrada>
### Costes Teóricos Greddy Recursivo
Coste Teorico del Greddy: El coste dependera que cual sea el camino a seguir, como en la mayoria de casos hacemos arcos de 2 puntos - un solo salto entonces el coste sera de O(n*n)

Coste mínimo: O(n)
Coste medio
Coste máximo: O(n*n)

### Pseudocódigo y Costes Prácticos Greddy Recursivo
A

Los coste practicos del greedy:
El mejor de los casos el coste sera de O(1) ya que la al empezar el el punto 1 la mejor opción es poner solo un arco hasta el final entonces nos saltamos todos los puntos de entremedias

El peor de los casos el coste seria de O(n) porque al calcular el mejor coste en este caso seria salta solo un punto entonces tendramos que recorer todos los puntos del suelo uno a uno hasta llegar al final.

greedy_recursive(numero_puntos, pos_x, pos_y)
    coste_total = 0
    if numero_puntos > 1    # para saber si estamos en el ultimo punto 
        x = 1
        menor_coste = calculate_cost_greedy(pos_x, pos_y, 0, x)    # desde la posición 0 hasta la x porque cuando llamamos a la función recursiva recortamos el array

        while x < len(pos_x)
            x + 1
            aux = calculate_cost_greedy(pos_x, pos_y, 0, x) 
            if  aux == "impossible"                                             # si da impossible no nos interesa comprar con el resultat del menor coste
                continue
            if aux < menor_coste
                x_menor_coste = x                                               # x_menor_coste indica que posición del array ha sido el de menor coste para poder recortarlo
                menor_coste = aux
        
        if menor_coste != "Impossible"
            result_temp = greedy_recursive(numero_puntos - x_menor_coste,       # llamamos a la recursividad recortando el array numero_puntos donde ha sido el x de menor coste
                                            pos_x[x_menor_coste:],              # hacemos lo mismo con los arrays de posición recordandolo igual numero_puntos
                                             pos_y[x_menor_coste:])                                  

            if result_temp == "Impossible"
                menor_coste = "Impossible"
            else
                coste_total = menor_coste + result_temp
    else
        return coste_total

# Análisis de costes

# Diseño
Dificultad y Coste del algoritmo
# Implementación

greedy_iterative.py
greedy_recursive.py

