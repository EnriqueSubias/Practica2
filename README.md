# Informe Practica 2

Práctica 2 de Algorítmica y Complejidad

# Greddy
El Greddy es un algorithmo que busca el coste minimo actual independientemente si da una solución correcta. En este caso sobre el problema de la construción de un aqueducto cuando queramos construit un arco tendremos que precalcular los costes de quantos puntos sera el arco, en la mayoria de casos el menor coste sera de poner un arco entre 2 puntos. Segun el camino que elijamos podrems llegar a un punto que ya no podemos poner ningun arco mas ya que hemos elejido el minimo siempre y nos lleva a un camino impossible, por eso en algunas ocaciónes el resultado nos da Impossible
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

# BackTraking
El Backtraking es un algorithmo que buscar un resultado possible ,si llega un aun punto que no pueda continuar vuelve al punto anteriro i elije otro camino. En este caso al construir un aqueducto nos pide que demos el mejor coste de construción de todo el aqueducto, para eso tenemos que encontrar todos los caminos possible para crear un aqueducto y elegir el de minimo coste.
## BackTraking Recursivo
Uso:
    $ ./aqueducte.py <fitxer entrada>
### Costes Teóricos BackTraking Recursivo
hay que pensar en los costes teoricos pero creo que podria ser n^n
### Pseudocódigo y Costes Prácticos BackTraking Recursivo

def backtracking_recursive(n_points, pos_x, pos_y):

    # si hay varios punts entrar al if para hacer todas las combinación con los diferentes puntos

    if numero_de_puntos > 2        # si no hay mas de 2 puntos solo tienes que calcular un salto simple
        i=1
        while i < numero_de_puntos - 1
            pos_x_a = pos_x [:i +1]         # recortamos el array 
            pos_x_y = pos_y [:i +1]         # recortamos el array 
            
            aux_a = calculate_cost( pos_x_a, pos_y_a, 0, -1 ) 
            pos_x_b = pos_x[i:]         # Array con las posiciones desde la i hasta la final
            pos_y_b = pos_y[i:]

            aux_b = backtracking_recursive(n_points - i, pos_x_b, pos_y_b) # llamamos la función recursiva para continuar probando caminos con el resto de puntos

            # si alguno de los calcualos da impossible no hace falta continuar ya que no es un camino possible

            if aux_a == "impossible" or aux_b == "impossible":  
                coste[i] = "impossible"

            else:   # en caso contrario sumamos una possible solución 
                coste[i] = aux_a + aux_b 

    # calculamos la posibilidad de un solo arco desde pos_x hasta al final

    coste[n_points] = calcular.calculate_cost(pos_x, pos_y, 0, -1)

    # si todos los resultados obtenidos son impossibl hacemos retunr impossible

    if all_impossible:
        return "impossible"

    # cojemos el resultado que sea possible de menor coste
    for k in coste:
        if coste[i] != "impossible":
            if coste[i] < result_:
                result_ = coste[i]

    return result

# Dynamic_Progaming
El Dynamic Progaming es un algorithmo muy parecido al BackTraking pero en este caso guarda los costes calculados de los puntes para reutilizarlo y no volver a calcular todos los soltos possibles. En este caso al construir un aqueducto nos pide que demos el mejor coste de construción de todo el aqueducto, para eso tenemos que encontrar todos los caminos possible para crear un aqueducto y elegir el de minimo coste.
## Dynamic_Progaming Recursivo
Uso:
    $ ./aqueducte.py <fitxer entrada>
### Costes Teóricos Dynamic_Progaming Recursivo
hay que pensar en los costes teoricos pero creo que podria ser n^n
### Pseudocódigo y Costes Prácticos Dynamic_Progaming Recursivo

def backtracking_recursive(n_points, pos_x, pos_y, costes_calculados):

    # si hay varios punts entrar al if para hacer todas las combinación con los diferentes puntos

    if numero_de_puntos > 2        # si no hay mas de 2 puntos solo tienes que calcular un salto simple
        i=1
        while i < numero_de_puntos - 1
            pos_x_a = pos_x [:i +1]         # recortamos el array 
            pos_x_y = pos_y [:i +1]         # recortamos el array 
            
            # si en la posición [x][y] es diferente de zero es que hay algun valor calculado entonces no tenemos que volver a calcularlo solo lo cojemos

            if costes_calculados[x][y] != 0     
                aux_a = costes_calculados[x][y]

            # en caso contrario hay que calcularlo por primera vez y lo guardamos en el array de calculados

            else
                aux_a = calculate_cost( pos_x_a, pos_y_a, 0, -1 ) 
                costes_calculados[x][y] = aux_a

            pos_x_b = pos_x[i:]         # Array con las posiciones desde la i hasta la final
            pos_y_b = pos_y[i:]

            aux_b = backtracking_recursive(n_points - i, pos_x_b, pos_y_b) # llamamos la función recursiva para continuar probando caminos con el resto de puntos

            # si alguno de los calcualos da impossible no hace falta continuar ya que no es un camino possible

            if aux_a == "impossible" or aux_b == "impossible":  
                coste[i] = "impossible"

            else:   # en caso contrario sumamos una possible solución 
                coste[i] = aux_a + aux_b 

    # calculamos la posibilidad de un solo arco desde pos_x hasta al final

    coste[n_points] = calcular.calculate_cost(pos_x, pos_y, 0, -1)

    # si todos los resultados obtenidos son impossibl hacemos retunr impossible

    if all_impossible:
        return "impossible"

    # cojemos el resultado que sea possible de menor coste
    for k in coste:
        if coste[i] != "impossible":
            if coste[i] < result_:
                result_ = coste[i]

    return result
