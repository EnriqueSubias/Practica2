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


def calculate_cost_arch(pos_x, pos_y, start, end):
    if doesnt_overlap_one_arch(pos_x, pos_y, start, end):
        result_columns = 0
        result_columns = float(result_columns +
                               (calcular.get_h_max() - int(pos_y[start])))
        result_columns = float(result_columns +
                               (calcular.get_h_max() - int(pos_y[end])))
        result_columns = calcular.get_alpha() * result_columns

        result_distances = 0
        result_distances = result_distances + (
            (int(pos_x[end]) - int(pos_x[start])) *
            (int(pos_x[end]) - int(pos_x[start])))
        result_distances = float(calcular.get_beta() * result_distances)
        result_total = float(result_columns + result_distances)
        return result_total
    return "impossible"


def doesnt_overlap_one_arch(pos_x, pos_y, start, end):
    """Comprueba que ningun punto del terreno interfiera con la semicircunferencia de cada arco,
    si el angulo es mayor de 90 grados, el punto del terreno no se solapa con el
    aqueducto, pero si es menor de 90 grados, significa que si que interfiere."""

    terrain_point = [0, 0]
    d_horizontal = pos_x[end] - pos_x[start]
    # center_y = h_max - float(max(pos_x)) / 2 # center y es la mitad del ancho total,
    # tenemos que calcular la mitad del ancho de donde vaya el arco
    center_y = calcular.get_h_max() - (d_horizontal / 2)

    point1 = [0, 0]
    point1[0] = float(pos_x[start])
    point1[1] = center_y

    point2 = [0, 0]
    point2[0] = float(pos_x[end])
    point2[1] = center_y

    for i in range(start, end):
        if center_y < int(pos_y[i]):
            terrain_point[0] = int(pos_x[i])
            terrain_point[1] = int(pos_y[i])
            angle = calculate_angle(point1, point2, terrain_point,
                                    d_horizontal)
            if angle < 90:
                return False
    return True


def calculate_angle(point1, point2, terrain_point, distance_horizontal):
    """Calcula el angulo de incidencia entre un punto del terreno y dos puntos
    en los pilares a la altura del centro de la semicircunferencia"""

    angle = 0

    # Distancia x e y del punto1 al punto del terreno
    distance1vector = [0, 0]
    distance1vector[0] = float(terrain_point[0] - point1[0])
    distance1vector[1] = float(terrain_point[1] - point1[1])

    # Distancia x e y del punto2 al punto del terreno
    distance2vector = [0, 0]
    distance2vector[0] = float(point2[0] - terrain_point[0])
    distance2vector[1] = float(terrain_point[1] - point2[1])

    distance1 = math.sqrt(distance1vector[0] * distance1vector[0] +
                          distance1vector[1] * distance1vector[1])
    distance2 = math.sqrt(distance2vector[0] * distance2vector[0] +
                          distance2vector[1] * distance2vector[1])

    cos_result = ((distance1 * distance1) + (distance2 * distance2) -
                  (distance_horizontal * distance_horizontal)) / (
                      2 * distance1 * distance2)
    angle = math.degrees(math.acos(cos_result))

    return angle


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
