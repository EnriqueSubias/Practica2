#! /usr/bin/env python3
"""Programa para calcular el coste de un aqueducto en modo Dynamic Programming Iterativo."""

import sys

from calculate import Calcul


def dynamic_programming(d_results):
    """Funcion Inicial Dynamic Programming"""
    result = dynamic_programming_iterative(calcular.get_n_points(),
                                           calcular.get_pos_x(),
                                           calcular.get_pos_y(), d_results)
    if result != "impossible":
        result = int(result +
                     (calcular.get_h_max() - calcular.get_pos_y()[-1]) *
                     calcular.get_alpha())
    return result


def dynamic_programming_iterative(n_points, pos_x, pos_y, dynamic_results):
    """Funcion Iterativa"""

    result = sys.maxsize
    stack = []
    longitud = 1
    inicial = 0
    new_pos = 0
    coste_stack = 0
    coste_total = 0
    cost_aux = 0
    stack.append([0, 0])

    if dynamic_results[inicial][inicial + longitud] != 0:
        cost_aux = dynamic_results[inicial][inicial + longitud]
    else:
        cost_aux = calcular.calculate_cost_iterative(pos_x, pos_y, inicial,
                                                     inicial + longitud)
        dynamic_results[inicial][inicial + longitud] = cost_aux

    if cost_aux != "impossible":
        stack.append([inicial + longitud, cost_aux])

    longitud += 1

    while stack:

        if inicial + longitud < n_points:  # -1
            if dynamic_results[inicial][inicial + longitud] != 0:
                cost_aux = dynamic_results[inicial][inicial + longitud]
            else:
                cost_aux = calcular.calculate_cost_iterative(
                    pos_x, pos_y, inicial, inicial + longitud)
                dynamic_results[inicial][inicial + longitud] = cost_aux

            if cost_aux != "impossible":
                stack.append([inicial + longitud, coste_stack + cost_aux])
            longitud += 1
        else:  # un salto simple de 1

            new_pos, coste_stack = stack.pop()
            if dynamic_results[new_pos][n_points - 1] != 0:
                cost_aux = dynamic_results[new_pos][n_points - 1]
            else:
                cost_aux = calcular.calculate_cost_iterative(
                    pos_x, pos_y, new_pos, n_points - 1)
                dynamic_results[new_pos][n_points - 1] = cost_aux

            if cost_aux != "impossible":
                coste_total = coste_stack + cost_aux
            else:
                coste_total = "impossible"

            if coste_total != "impossible":
                if coste_total < result:
                    #print(result)
                    result = coste_total
                    #print(result)

            #coste_total comparar con el mínimo coste y poner el minimo, sustituirlo si es necesario
            inicial = new_pos
            longitud = 1
            if new_pos == 0 and coste_stack == 0:
                continue

    if result in (0, sys.maxsize):
        return "impossible"

    return result  # Por acabar


if __name__ == "__main__":

    if len(sys.argv) != 2:
        if len(sys.argv) == 1:
            print(u"\n\u001b[31mIntroducir datos por teclado\u001b[0m\n")
            sys.exit(0)
        print(
            u"\n\u001b[31mTienes que indicar el nombre le archivo\u001b[0m\n")
        sys.exit(0)

    f = open(sys.argv[1], "r")

    calcular = Calcul(0, 0, 0, 0)
    calcular.read_valores_aqueductor(f)

    if calcular.is_valid():
        if calcular.read_terrain(f):
            numero_de_puntos = calcular.get_n_points()

            results_array = []
            for x in range(numero_de_puntos):
                row = []
                for j in range(numero_de_puntos):
                    NUM = 0
                    row.append(NUM)
                results_array.append(row)

            print(dynamic_programming(results_array))

            #for i in range(calcular.get_n_points()):
            #    print(results_array[i])

        else:
            print("impossible")
    else:
        print("impossible")
    sys.exit(0)
