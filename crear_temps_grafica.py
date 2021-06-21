#! /usr/bin/env python
"""Programa para hacer la grafica."""

import random
import timeit
import matplotlib.pyplot as plt

import dynamic_programming_recursive


def soil_generator(n_points):
    """Soil Generator"""
    h_max = random.randint(150, 200)
    alpha = random.randint(1, 100)
    beta = random.randint(1, 100)

    points_x = sorted(random.sample(range(1, n_points * 5), n_points))
    #print(n_points, h_max, alpha, beta)

    points = []
    for i in points_x:
        points.append((i, random.randint(1, 100)))

    return h_max, alpha, beta, points


def test_aqueducte(n_points):
    """Test Aqueducte"""
    h_max, alpha, beta, points = soil_generator(n_points)
    x_s, y_s = list(zip(*points))
    dynamic_programming_recursive.pos_x = x_s
    dynamic_programming_recursive.pos_y = y_s
    dynamic_programming_recursive.alpha = alpha
    dynamic_programming_recursive.beta = beta
    dynamic_programming_recursive.n_points = n_points
    dynamic_programming_recursive.h_max = h_max
    a = dynamic_programming_recursive.modografica()


def calcular_temps():
    """Calcular Temps"""
    temps_calc = []
    for n_points in range(1, 14):
        temps_calc.append(
            (n_points,
             timeit.timeit("test_aqueducte(" + str(n_points) + ")",
                           setup="from __main__ import test_aqueducte",
                           number=1000)))
    return temps_calc


def crear_grafica(x_list, y_list):
    """Crear Grafica"""
    plt.scatter(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    print("Calculando...")
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
