#! /usr/bin/env python3
"""Programa para calcular el coste de un aqueducto en modo BackTracking Iterativo."""

import os
import os.path
import glob
import math
import sys

from calculate import Calcul

sys.setrecursionlimit(20000)
#solucion = 1


def backtracking():
    """Funcion Inicial Backtracking"""
    result = "impossible" # Por acabar
    #result = backtracking_iterative(calcular.get_n_points(), calcular.get_pos_x(), calcular.get_pos_y())
    return result


def backtracking_iterative(n, pos_x, pos_y):
    """Funcion Recursiva"""

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

    # Calculo de costes para un solo arco
    #coste[n] = calculate_cost_one_arch(n, pos_x,  pos_y) # dos puntos del terreno y la altura máxima

    result = sys.maxsize

    all_impossible = True
    for x in coste:
        if coste[x] != "impossible":
            all_impossible = False
            break

    if all_impossible:
        return "impossible"

    for k in coste:
        if coste[k] != "impossible":
            if coste[k] < result:
                result = coste[k]
    return result


if __name__ == "__main__":

    if len(sys.argv) != 2:
        if len(sys.argv) == 1:
            print(u"\n\u001b[31mIntroducir datos por teclado\u001b[0m\n")
            # Por hacer
            sys.exit(0)
        print(
            u"\n\u001b[31mTienes que indicar el nombre le archivo\u001b[0m\n")
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
