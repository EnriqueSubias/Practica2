#! /usr/bin/env python3
"""Programa para calcular el coste de un aqueducto en modo Dynamic Programming Recursivo."""

import sys

from calculate import Calcul

sys.setrecursionlimit(20000)


def dynamic_programming(d_results):
    """Funcion Inicial Backtracking"""
    result = dynamic_programming_recursive(calcular.get_n_points(), 0,
                                           calcular.get_pos_x(),
                                           calcular.get_pos_y(), d_results)
    if result != "impossible":
        result = int(result +
                     (calcular.get_h_max() - calcular.get_pos_y()[-1]) *
                     calcular.get_alpha())
    return result


def dynamic_programming_recursive(n_points, pos_inicial, pos_x, pos_y,
                                  dynamic_results):
    """Funcion Recursiva"""

    coste = {}

    if n_points > 2:

        i = 1

        while i < n_points - 1:
            pos_i = pos_inicial

            pos_x_a = pos_x[:i + 1]
            pos_y_a = pos_y[:i + 1]

            pos_x_b = pos_x[i:]
            pos_y_b = pos_y[i:]
            pos_i += i

            if dynamic_results[pos_i][pos_i + len(pos_x_b) - 1] != 0:
                aux_a = dynamic_results[pos_i][pos_i + len(pos_x_b) - 1]

            else:
                aux_a = calcular.calculate_cost(pos_x_a, pos_y_a, 0, -1)
                dynamic_results[pos_i][pos_i + len(pos_x_b) - 1] = aux_a

            # llamada recursiva con los puntos desde i al final

            # Array con las posiciones desde la inicial hasta la final
            aux_b = dynamic_programming_recursive(n_points - i, pos_inicial,
                                                  pos_x_b, pos_y_b,
                                                  dynamic_results)

            if aux_a == "impossible" or aux_b == "impossible":
                coste[i] = "impossible"
            else:
                coste[i] = aux_a + aux_b
            i += 1

    # Calculo de costes para un solo arco
    if dynamic_results[pos_inicial][pos_inicial + len(pos_x) - 1] != 0:
        coste[n_points] = dynamic_results[pos_inicial][pos_inicial +
                                                       len(pos_x) - 1]

    else:
        coste[n_points] = calcular.calculate_cost(pos_x, pos_y, 0, -1)
        dynamic_results[pos_inicial][pos_inicial + len(pos_x) -
                                     1] = coste[n_points]

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

            # Imprime el array que utiliza el dynamic programming
            #for i in range(calcular.get_n_points()):
            #  print(results_array[i])

        else:
            print("impossible")
    else:
        print("impossible")
    sys.exit(0)
