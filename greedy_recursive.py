#! /usr/bin/env python3
"""Greedy Recursive"""

import sys

from calculate import Calcul


def greedy():
    """Greedy"""
    coste_total = greedy_recursive(calcular.get_n_points(),
                                   calcular.get_pos_x(), calcular.get_pos_y())
    if coste_total not in (-1, "impossible"):
        coste_total = int(coste_total +
                          (calcular.get_h_max() - calcular.get_pos_y()[-1]) *
                          calcular.get_alpha())  # Sumamos el último pilar
    if coste_total == -1:
        coste_total = "impossible"

    return coste_total


def greedy_recursive(n_points, pos_x, pos_y):
    """Greedy"""
    coste_total = 0
    if n_points > 1:
        i = 1
        x_menor_coste = i
        menor_coste = calcular.calculate_cost_greedy(pos_x, pos_y, 0, i)

        if menor_coste == "impossible":
            menor_coste = -1
        while i < len(pos_x) - 1:
            i += 1
            aux = calcular.calculate_cost_greedy(pos_x, pos_y, 0, i)
            if aux == "impossible":
                continue
            if aux < menor_coste or menor_coste == -1:
                x_menor_coste = i
                menor_coste = aux

        if menor_coste not in (-1, "impossible"):
            coste_total += (menor_coste -
                            (calcular.get_h_max() - pos_y[x_menor_coste]) *
                            calcular.get_alpha())
            # Restamos el coste de pilares duplicados

        if menor_coste == -1:
            coste_total = "impossible"
            return "impossible"

        result_temp = greedy_recursive(n_points - x_menor_coste,
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
            print(u"\n_points\u001b[31mIntroducir datos por teclado\u001b[0m\n_points")
            # Por hacer
            sys.exit(0)
        print(
            u"\n_points\u001b[31mTienes que indicar el nombre le archivo\u001b[0m\n_points")
        sys.exit(0)

    f = open(sys.argv[1], "r")

    calcular = Calcul(0, 0, 0, 0)
    calcular.read_valores_aqueductor(f)

    if calcular.is_valid():
        if calcular.read_terrain(f):

            print(greedy())

        else:
            print("impossible")
    else:
        print("impossible")
    sys.exit(0)
