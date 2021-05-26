#! /usr/bin/env python3

import math
import sys

print(u"\u001b[36m\nGreedy Recursivo\n\u001b[0m")

def greedy(n, pos_x, pos_y):

    coste_total = greedy_experimental(n, pos_x, pos_y)

    pilar_contado_por_dos = (h_max - pos_y[-1] ) * alpha
    if coste_total != -1 and coste_total != "impossible":
        coste_total += (h_max - pos_y[-1] ) * alpha # Sumamos el último pilar
        print("*****    +",pilar_contado_por_dos)
    return coste_total

def greedy_experimental(n, pos_x, pos_y):
    coste_total = 0
    if n > 1:
        x =  1
        menor_coste = calculate_cost_arch(n, pos_x,  pos_y, 0, x)
        if menor_coste == "impossible":
            menor_coste = -1
        x_menor_coste = x
        while x < len(pos_x) - 1:
            x += 1
            aux = calculate_cost_arch(n, pos_x,  pos_y, 0, x)
            print("POS X: ", x)
            if aux == "impossible":
                continue
            if aux < menor_coste or menor_coste == -1:
                x_menor_coste = x
                menor_coste = aux
                print("+++++++++++")
        pilar_contado_por_dos = (h_max - pos_y[x_menor_coste] ) * alpha
        if menor_coste != -1 and menor_coste != "impossible":
            coste_total += menor_coste - pilar_contado_por_dos # Restamos el coste de pilares duplicados

        print("Posición de arco", x_menor_coste)

        if menor_coste == -1:
            coste_total = "impossible"
            return "impossible"

        result_temp = greedy_experimental(n - x_menor_coste, pos_x[x_menor_coste:], pos_y[x_menor_coste:])

        if result_temp == "impossible":
            coste_total= "impossible"
        else:
            coste_total += result_temp

    return coste_total

def calculate_cost_arch(n_points, pos_x, pos_y, start, end):
    if doesnt_overlap_one_arch(n_points, pos_x, pos_y, start, end):
        result_columns = 0
        result_columns = float(result_columns + (h_max - int(pos_y[start])))
        result_columns = float(result_columns + (h_max - int(pos_y[end])))
        result_columns = alpha * result_columns

        result_distances = 0
        result_distances = result_distances + \
            ((int(pos_x[end]) - int(pos_x[start])) * (int(pos_x[end]) - int(pos_x[start])))
        result_distances = float(beta * result_distances)
        result_total= float(result_columns + result_distances)
        return result_total
    return "impossible"


def doesnt_overlap_one_arch(n_points, pos_x, pos_y, start, end):
    """Comprueba que ningun punto del terreno interfiera con la semicircunferencia de cada arco,
    si el angulo es mayor de 90 grados, el punto del terreno no se solapa con el
    aqueducto, pero si es menor de 90 grados, significa que si que interfiere."""
    terrain_point = [0, 0]
    d_horizontal = pos_x[end] - pos_x[start]
    #center_y = h_max - float(max(pos_x)) / 2 # center y es la mitad del ancho total, tenemos que calcular la mitad del ancho de donde vaya el arco
    center_y = h_max - (d_horizontal / 2)

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
            angle = calculate_angle(point1, point2, terrain_point, d_horizontal)
            if angle < 90:
                return False
            #else:
                #seguir dando vueltas
    return True


def calculate_angle(point1, point2, terrain_point, distance_horizontal):
    """Calcula el angulo de incidencia entre un punto del terreno y dos puntos
       en los pilares a la altura del centro de la semicircunferencia"""

    angle = 0

    #Distancia x e y del punto1 al punto del terreno
    distance1vector = [0, 0]
    distance1vector[0] = float(terrain_point[0] - point1[0])
    distance1vector[1] = float(terrain_point[1] - point1[1])

    #Distancia x e y del punto2 al punto del terreno
    distance2vector = [0, 0]
    distance2vector[0] = float(point2[0] - terrain_point[0])
    distance2vector[1] = float(terrain_point[1] - point2[1])

    distance1 = math.sqrt(
        distance1vector[0] * distance1vector[0] + distance1vector[1] * distance1vector[1])
    distance2 = math.sqrt(
        distance2vector[0] * distance2vector[0] + distance2vector[1] * distance2vector[1])

    cos_result = (((distance1 * distance1) + (distance2 * distance2) -
         (distance_horizontal * distance_horizontal)) / (2 * distance1 * distance2))
    angle = math.degrees(math.acos(cos_result))

    return angle


def is_valid():
    """Comprueba que los parametros de la primera linea son correctos segun el enunciado."""
    if n_points < 2 or n_points > 10000 or h_max < 1 or h_max > 100000:
        return False
    if alpha < 1 or alpha > 10000 or beta < 1 or beta > 10000:
        return False
    return True


def read_terrain():
    """Lee los puntos del terreno y comprueba que esten por debajo de la altura maxima"""
    for i in f:
        string_doc = i.split(" ")
        if float(string_doc[1]) > h_max:
            return False
        pos_x.append(float(string_doc[0]))
        pos_y.append(float(string_doc[1]))
    pos_x.pop(0)
    pos_y.pop(0)
    return True



if __name__ == "__main__":

    #f = open(sys.argv[1], "r") ##########  IMPORTANTE ################
    filename = "secret-28"
    # secret-06
    # secret-08
    # secret-12
    # secret-13
    # secret-14


    f = open("test-greedy/" + filename +".in", "r")
    valores = f.readline().split(" ")

    s = open("test-greedy/" + filename + ".ans", "r")
    comparar_resultado = s.readline()

    n_points = int(valores[0])
    h_max = int(valores[1])
    alpha = int(valores[2])
    beta = int(valores[3])

    if is_valid():
        pos_x = [0]              # X primera columna
        pos_y = [0]              # Y segunda columna
        if read_terrain():
            #f.close # pylint dice que es innecesario ponerlo
            #result = [0, 0]
            #result = check_overlap_and_calculate_cost_multiple_arches()
            #result[1] = calculate_cost_one_arch()

            result = greedy(n_points, pos_x, pos_y)
            #result = int(result)
            if result == -1:
                result = "impossible"
            print(u"\n\u001b[33mResultado Calculado", result , u"\u001b[0m")
            print(u"\u001b[32mResultado Correcto ", comparar_resultado , u"\u001b[0m\n")
            print(u"\u001b[36m" , pos_x , u"\u001b[0m")
        else:
            print("impossible")
    else:
        print("impossible")
