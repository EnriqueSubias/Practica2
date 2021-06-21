#! /usr/bin/env python3
"""Greedy Iterative"""  # Coste minimo O(n^2)

import sys

from calculate import Calcul


def greedy():
    """Greedy"""

    coste_total = greedy_iterative(calcular.get_n_points(),
                                   calcular.get_pos_x(), calcular.get_pos_y())
    if coste_total not in (-1, "impossible"):
        coste_total = int(coste_total)
    if coste_total == -1:
        coste_total = "impossible"

    return coste_total


def greedy_iterative(n_points, pos_x, pos_y):
    """Greedy"""

    i = 0
    coste_total = 0
    # x_menor_coste = 0
    # Array 0-4
    # i     0-3
    # j     i-4
    while i < n_points - 1:
        j = i + 1
        #menor_coste = calculate_cost_arch(pos_x, pos_y, i, j)
        menor_coste = calcular.calculate_cost_greedy(pos_x, pos_y, i, j)
        if menor_coste == "impossible":
            menor_coste = -1
        x_menor_coste = j

        #print("POS X: ", j)
        while j < len(pos_x) - 1:
            j += 1
            #aux = calculate_cost_arch(pos_x, pos_y, i, j)
            aux = calcular.calculate_cost_greedy(pos_x, pos_y, i, j)
            #print("POS X: ", j)
            if aux == "impossible":
                continue
            if aux < menor_coste or menor_coste == -1:
                x_menor_coste = j
                menor_coste = aux
        pilar_contado_por_dos = (calcular.get_h_max() -
                                 pos_y[x_menor_coste]) * calcular.get_alpha()
        if menor_coste not in (-1, "impossible"):
            coste_total += (menor_coste - pilar_contado_por_dos
                            )  # Restamos el coste de pilares duplicados
        i = x_menor_coste
        if menor_coste == -1:
            coste_total = "impossible"
            break

    if menor_coste not in (-1, "impossible"):
        coste_total += pilar_contado_por_dos  # Sumamos el último pilar

    return coste_total


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

            print(greedy())

        else:
            print("impossible")
    else:
        print("impossible")
    sys.exit(0)
