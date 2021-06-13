#! /usr/bin/env python3
"""Greedy Iterative"""  # Coste minimo O(n^2)

import math
import sys

from calculate import Calcul


def greedy():
    """Greedy"""

    coste_total = greedy_iterative(calcular.get_n_points(),
                                   calcular.get_pos_x(), calcular.get_pos_y())
    if coste_total != -1 and coste_total != "impossible":
        coste_total = int(coste_total)
    if coste_total == -1:
        coste_total = "impossible"

    return coste_total


def greedy_iterative(n, pos_x, pos_y):
    i = 0
    coste_total = 0
    # x_menor_coste = 0
    # Array 0-4
    # i     0-3
    # x     i-4
    while i < n - 1:
        x = i + 1
        #menor_coste = calculate_cost_arch(pos_x, pos_y, i, x)
        menor_coste = calcular.calculate_cost_greedy(pos_x, pos_y, i, x)
        if menor_coste == "impossible":
            menor_coste = -1
        x_menor_coste = x

        #print("POS X: ", x)
        while x < len(pos_x) - 1:
            x += 1
            #aux = calculate_cost_arch(pos_x, pos_y, i, x)
            aux = calcular.calculate_cost_greedy(pos_x, pos_y, i, x)
            #print("POS X: ", x)
            if aux == "impossible":
                continue
            if aux < menor_coste or menor_coste == -1:
                x_menor_coste = x
                menor_coste = aux
                #print("+++++++++++")
        pilar_contado_por_dos = (calcular.get_h_max() -
                                 pos_y[x_menor_coste]) * calcular.get_alpha()
        if menor_coste != -1 and menor_coste != "impossible":
            coste_total += (menor_coste - pilar_contado_por_dos
                            )  # Restamos el coste de pilares duplicados
        i = x_menor_coste
        #print("Posición de arco", x_menor_coste)
        #print("POS I: ", i)
        if menor_coste == -1:
            coste_total = "impossible"
            break

    if menor_coste != -1 and menor_coste != "impossible":
        coste_total += pilar_contado_por_dos  # Sumamos el último pilar
        #print("*****    +", pilar_contado_por_dos)

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
