#! /usr/bin/env python3
"""Programa para calcular el coste de un aqueducto en modo Dynamic Programming Recursivo."""

import sys

from calculate import Calcul


def dynamic_programming():
    return dynamic_programming_recursive(calcular.get_n_points(),
                                         calcular.get_pos_x(),
                                         calcular.get_pos_y())


def dynamic_programming_recursive(n_points, pos_x, pos_y):
    """Funcion Recursiva"""
    return "impossible" # Por acabar


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

            print(dynamic_programming())

        else:
            print("impossible")
    else:
        print("impossible")
    sys.exit(0)