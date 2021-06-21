#! /usr/bin/env python3
"""Programa para calcular el coste de un aqueducto en modo BackTracking Iterativo."""

import sys
from typing import final, no_type_check_decorator

from calculate import Calcul


def backtracking():
    """Funcion Inicial Backtracking"""
    result = backtracking_iterative2(calcular.get_n_points(),
                                     calcular.get_pos_x(),
                                     calcular.get_pos_y())
    if result != "impossible":
        result = int(result +
                     (calcular.get_h_max() - calcular.get_pos_y()[-1]) *
                     calcular.get_alpha())
    return result


def backtracking_iterative2(n_points, pos_x, pos_y):
    result = sys.maxsize
    STACK = []
    longitud = 1
    inicial = 0
    new_pos = 0
    coste_stack = 0
    coste_total = 0
    cost_aux = 0
    STACK.append([0, 0])

    cost_aux = calcular.calculate_cost(pos_x, pos_y, inicial,
                                       inicial + longitud)
    if cost_aux != "impossible":
        STACK.append([inicial + longitud, cost_aux])
        
    longitud += 1

    while STACK:

        if inicial + longitud < n_points - 1:

            cost_aux = calcular.calculate_cost(pos_x, pos_y, inicial,
                                               inicial + longitud)
            if cost_aux != "impossible":
                STACK.append([inicial + longitud, coste_stack + cost_aux])
            longitud += 1
        else:  # un salto simple de 1
            
            # NO CALCULAMOS SALTO DE PRINCIPIO A FINAL 
            #if STACK.top() != [0, 0]:
            #    coste_total = coste_stack + calcular.calculate_cost(pos_x, pos_y, inicial, -1)
                
            new_pos, coste_stack = STACK.pop()
            cost_aux = calcular.calculate_cost(pos_x, pos_y, new_pos, -1)
            if cost_aux != "impossible":
                coste_total = coste_stack + cost_aux

            if coste_total != "impossible":
                if coste_total < result:
                    result = coste_total

            # coste_total comparar con el mínimo coste y poner el minimo, sustituirlo si es necesario
            inicial = new_pos
            longitud = 1
            if new_pos == 0 and coste_stack == 0:
                continue

    if result == 0:
        return "impossible"

    return result


"""def iterative():

    while(n_posiciones):

        while():

            #hacer un arco de longitud i
            #calculamos su coste
            
            #añadimos al stack punto inicio [i], punto final [-1]

            posicion_inicial = posicion_n

                if (punto_inicio == punto_final):
                    #sacar del stack y calcular costes


    i++
    
    STACK.insert(0, ['CALL', n - i, pos_x_b, pos_y_b]) #indicando el numero de puntos

        while i < n_points - 1:
            pos = 1
            while repetir repetir hasta n-2
                arcos de 1
                
                
                STACK.POP salto
                salto ++
                STACK.insert(0, ['CALL', salto])
                if salto != final:
                    STACK.insert(0, ['CALL', salto - final])

                
                pos ++
                while repetir

            
            
    while inicial:  
           
        while final:
            

            if final != n_points:
                #seguir
                STACK.insert(inicial, final) # ponemos de que posicion a cual hacemos un arco
            else:
                #tenemos uno de los posibles costes,
                #lo comparamos con el coste mínimo

            
    

    1 Arco 
        1 Arco 
            1 Arco 
                1 Arco 
                    1 Arco      [Posibilidad 1]
                    
                2 Arco          [Posibilidad 2]

            2 Arco
                    1 Arco      [Posibilidad 3]

            3 Arco              [Posibilidad 4]

        2 Arco
                1 Arco
                    1 Arco      [Posibilidad 5]
        2 Arco
                2 Arco          [Posibilidad 6]
        3 Arco      
                    1 Arco      [Posibilidad 7]
                    
        4 Arco                  [Posibilidad 8]

"""


def backtracking_iterative(n_points, pos_x, pos_y):
    """Funcion Iterativa"""
    coste = {}

    #if calcular.get_n_points() > 2:

    i = 1

    while i < calcular.get_n_points() - 1:

        # Array con las posiciones desde la a hasta la final
        pos_x_a = pos_x[:i + 1]
        pos_y_a = pos_y[:i + 1]

        n = n + 1
        #aux_a = calculate_cost_one_arch(i + 1, pos_x_a, pos_y_a)
        aux_a = calcular.calculate_cost(pos_x_a, pos_y_a, 0, -1)

        #llamada recursiva con los puntos desde i al final

        # Array con las posiciones desde la a hasta la final
        pos_x_b = pos_x[i:]
        pos_y_b = pos_y[i:]

        #aux_b = backtracking_iterative(calcular.get_n_points() - i, pos_x_b, pos_y_b)

        STACK = []
        STACK.insert(0, ['CALL', n - i, pos_x_b, pos_y_b])
        aux_b = None
        while STACK:
            action, data, x, y = STACK.pop(0)
            if action == 'CALL':
                n_p = data
                if n <= 2:
                    #coste[n] = calculate_cost_one_arch(n, pos_x, pos_y)
                    coste[n] = calcular.calculate_cost(pos_x, pos_y, 0, -1)
                else:
                    #llamada recursiva con los puntos desde i al final
                    STACK.insert(0, ['RESUME', n_p, pos_x_b, pos_y_b])
                    pos_x_b = pos_x[
                        i:]  # Array con las posiciones desde la a hasta la final
                    pos_y_b = pos_y[i:]
                    STACK.insert(len(STACK),
                                 ['CALL', n_p - i, pos_x_b, pos_y_b])

            elif action == "RESUME":
                n_p = data
                x_p = x
                y_p = y
                aux_b = calcular.calculate_cost(pos_x, pos_y, 0, -1)

        if aux_a == "impossible" or aux_b == "impossible":
            coste[i] = "impossible"
            #coste.append("impossible")
        else:
            #pilar_contado_por_dos = (calcular.get_h_max() - pos_y[i - 1] ) * calcular.get_alpha()
            coste[i] = aux_a + aux_b
        i += 1

    result = min(coste)
    return result


if __name__ == "__main__":

    debug = True

    if debug:
        f = open("aqueductes/secret-03.in", "r")

    else:
        if len(sys.argv) != 2:
            if len(sys.argv) == 1:
                print(u"\n\u001b[31mIntroducir datos por teclado\u001b[0m\n")
                # Por hacer
                sys.exit(0)
                print(
                    u"\n\u001b[31mTienes que indicar el nombre le archivo\u001b[0m\n"
                )
            sys.exit(0)

        f = open(sys.argv[1], "r")

    calcular = Calcul(0, 0, 0, 0)  # IMPORTANTE CAMBIAR
    calcular.read_valores_aqueductor(f)

    if calcular.is_valid():
        if calcular.read_terrain(f):

            print(backtracking())

        else:
            print("impossible")
    else:
        print("impossible")
    sys.exit(0)
