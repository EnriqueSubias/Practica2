#! /usr/bin/env python3

"""Programa para calcular el coste de un aqueducto en modo BackTracking Recursivo."""

import sys

from calculate import Calcul

sys.setrecursionlimit(20000)
# solucion = 1


def backtracking():
    """Funcion Inicial Backtracking"""
    result = backtracking_recursive(
        calcular.get_n_points(), calcular.get_pos_x(), calcular.get_pos_y()
    )
    if result != "impossible":
        result = int(
            result
            + (calcular.get_h_max() - calcular.get_pos_y()[-1]) * calcular.get_alpha()
        )
    return result


def backtracking_recursive(n_points, pos_x, pos_y):
    """Funcion Recursiva"""

    coste = {}

    if n_points > 2:

        i = 1

        while i < n_points - 1:

            pos_x_a = pos_x[: i + 1]
            pos_y_a = pos_y[: i + 1]
            aux_a = calcular.calculate_cost(pos_x_a, pos_y_a, 0, -1)

            # llamada recursiva con los puntos desde i al final
            pos_x_b = pos_x[i:]  # Array con las posiciones desde la a hasta la final
            pos_y_b = pos_y[i:]
            aux_b = backtracking_recursive(n_points - i, pos_x_b, pos_y_b)

            if aux_a == "impossible" or aux_b == "impossible":
                coste[i] = "impossible"
                # coste.append("impossible")
            else:
                # pilar_contado_por_dos = (h_max - pos_y[i - 1] ) * alpha
                coste[i] = aux_a + aux_b
            i += 1

    # Calculo de costes para un solo arco
    coste[n_points] = calcular.calculate_cost(pos_x, pos_y, 0, -1)

    result_ = sys.maxsize

    all_impossible = True
    for value in coste:
        if coste[value] != "impossible":
            all_impossible = False
            break

    if all_impossible:
        return "impossible"

    for k in coste:
        if coste[k] != "impossible":
            if coste[k] < result_:
                result_ = coste[k]

    return result_


if __name__ == "__main__":

    if len(sys.argv) != 2:
        if len(sys.argv) == 1:
            print(u"\n\u001b[31mIntroducir datos por teclado\u001b[0m\n")
            # Por hacer
            sys.exit(0)
        print(u"\n\u001b[31mTienes que indicar el nombre le archivo\u001b[0m\n")
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
