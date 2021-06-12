#! /usr/bin/env python3

"""Programa para calcular el coste de un aqueducto en modo BackTracking Recursivo."""

import os, os.path, glob
import math
import sys

from calculate import calcul

sys.setrecursionlimit(20000)
solucion = 1

#print(u"\u001b[36m\nBackTracking Recursivo\n\u001b[0m")
def rec_func(n, pos_x, pos_y): # anadir mas parametros que hagan falta
    """5 puntos
        recusividad

        0 - 1,2,3,4
            0 - 2,3,4
                0 - 3,4 -> 3 - 4
                    0 - 4"""

    coste = {}

    if n > 2:

        i = 1

        while i < n - 1:

            pos_x_a = pos_x[:i+1] # Array con las posiciones desde la a hasta la final
            pos_y_a = pos_y[:i+1]
            aux_a = calcular.calculate_cost_one_arch_backtraking(i + 1, pos_x_a, pos_y_a, 0, -1)

            #llamada recursiva con los puntos desde i al final
            pos_x_b = pos_x[i:] # Array con las posiciones desde la a hasta la final
            pos_y_b = pos_y[i:]
            aux_b = rec_func(n - i, pos_x_b, pos_y_b)

            if aux_a == "impossible" or aux_b == "impossible":
                coste[i]= "impossible"
                #coste.append("impossible")
            else:
                #pilar_contado_por_dos = (h_max - pos_y[i - 1] ) * alpha
                coste[i] = aux_a + aux_b
            i += 1

    # Calculo de costes para un solo arco
    coste[n] = calcular.calculate_cost_one_arch_backtraking(n, pos_x,  pos_y, 0, -1) # dos puntos del terreno y la altura máxima

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
                #comentado-print("+++++++++++++++++++++++++++++++++++", coste[k], "+++++++++++++++++++++++++++++++++++")
                result = coste[k]

    return result


if __name__ == "__main__":
        
    if len(sys.argv) != 2:
        if len(sys.argv) == 1:
            print(u"\n\u001b[31mIntroducir datos por teclado\u001b[0m\n")
            # Por hacer
            exit(0)
        print(u"\n\u001b[31mTienes que indicar el nombre le archivo\u001b[0m\n")
        exit(0)
       
    f = open(sys.argv[1], "r")

    calcular = calcul(0,0,0,0)  # IMPORTANTE CAMBIAR
    calcular.read_valores_aqueductor(f)
    if calcular.is_valid():  
        if calcular.read_terrain(f): 
            #print(calcular.get_n_points())
            #print(calcular.get_posX())
            #print(calcular.get_posY())
            result = rec_func(calcular.get_n_points(), calcular.get_posX(), calcular.get_posY())
            if result != "impossible":
                result = result + (calcular.get_h_max() - calcular.get_posY()[-1] ) * calcular.get_alpha()
                print(int(result))
            else:
                print("impossible")
        else:
            print("impossible")
    else:
        print("impossible")
    exit(0)
