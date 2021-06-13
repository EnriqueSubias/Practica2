#! /usr/bin/env python3
"""Greedy Recursive"""

import math
import sys

from calculate import Calcul


def greedy():
    """Greedy"""
    coste_total = greedy_recursive(calcular.get_n_points(),
                                   calcular.get_pos_x(), calcular.get_pos_y())
    if coste_total != -1 and coste_total != "impossible":
        coste_total = int(coste_total +
                          (calcular.get_h_max() - calcular.get_pos_y()[-1]) *
                          calcular.get_alpha())  # Sumamos el último pilar
    if coste_total == -1:
        coste_total = "impossible"

    return coste_total


def greedy_recursive(n, pos_x, pos_y):
    """Greedy"""
    coste_total = 0
    if n > 1:
        x = 1
        x_menor_coste = x
        menor_coste = calcular.calculate_cost_greedy(pos_x, pos_y, 0, x)

        if menor_coste == "impossible":
            menor_coste = -1
        while x < len(pos_x) - 1:
            x += 1
            aux = calcular.calculate_cost_greedy(pos_x, pos_y, 0, x)
            if aux == "impossible":
                continue
            if aux < menor_coste or menor_coste == -1:
                x_menor_coste = x
                menor_coste = aux

        if menor_coste != -1 and menor_coste != "impossible":
            coste_total += (menor_coste -
                            (calcular.get_h_max() - pos_y[x_menor_coste]) *
                            calcular.get_alpha())
            # Restamos el coste de pilares duplicados

        if menor_coste == -1:
            coste_total = "impossible"
            return "impossible"

        result_temp = greedy_recursive(n - x_menor_coste,
                                       pos_x[x_menor_coste:],
                                       pos_y[x_menor_coste:])

        if result_temp == "impossible":
            coste_total = "impossible"
        else:
            coste_total += result_temp
    return coste_total


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

            print(greedy())

        else:
            print("impossible")
    else:
        print("impossible")
    sys.exit(0)
