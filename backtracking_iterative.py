#! /usr/bin/env python3
"""Programa para calcular el coste de un aqueducto en modo BackTracking Iterativo."""
import os, os.path, glob
import math
import sys

#comentado-print(u"\u001b[36m\nBackTracking Recursivo\n\u001b[0m")

sys.setrecursionlimit(20000)
solucion = 1
# BackTracking Iterativo


def rec_func(n, pos_x, pos_y):  # anadir mas parametros que hagan falta
    """5 puntos
        recusividad

        0 - 1,2,3,4
            0 - 2,3,4
                0 - 3,4 -> 3 - 4
                    0 - 4"""

    coste = {}

    #if n > 2:

    i = 1

    while i < n - 1:

        pos_x_a = pos_x[:i +
                        1]  # Array con las posiciones desde la a hasta la final
        pos_y_a = pos_y[:i + 1]
        aux_a = calculate_cost_one_arch(i + 1, pos_x_a, pos_y_a)

        #llamada recursiva con los puntos desde i al final
        pos_x_b = pos_x[
            i:]  # Array con las posiciones desde la a hasta la final
        pos_y_b = pos_y[i:]

        #aux_b = rec_func(n - i, pos_x_b, pos_y_b)

        STACK = []
        STACK.insert(0, ['CALL', n - i, pos_x_b, pos_y_b])
        aux_b = None
        while STACK:
            action, data, x, y = STACK.pop(0)
            if action == 'CALL':
                n_p = data
                if n <= 2:
                    coste[n] = calculate_cost_one_arch(n, pos_x, pos_y)
                else:
                    #llamada recursiva con los puntos desde i al final
                    STACK.insert(0, ['RESUME', n_p, pos_x_b, pos_y_b])
                    pos_x_b = pos_x[
                        i:]  # Array con las posiciones desde la a hasta la final
                    pos_y_b = pos_y[i:]
                    STACK.insert(len(STACK),
                                 ['CALL', n_p - i, pos_x_b, pos_y_b])

            elif action == "RESUME":
                n_p = data
                x_p = x
                y_p = y
                aux_b = calculate_cost_one_arch(n_p, x, y)

        if aux_a == "impossible" or aux_b == "impossible":
            coste[i] = "impossible"
            #coste.append("impossible")
        else:
            #pilar_contado_por_dos = (h_max - pos_y[i - 1] ) * alpha
            coste[i] = aux_a + aux_b
        i += 1

    # Calculo de costes para un solo arco
    #coste[n] = calculate_cost_one_arch(n, pos_x,  pos_y) # dos puntos del terreno y la altura máxima

    result = 999999999999999999

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
                result = coste[k]
    return result


def backtraking_iterativeV2(n, pos_x, pos_y):
    return 0


def check_overlap_and_calculate_cost_multiple_arches():
    """Comprueba que todos los arcos posibles no interfieran con el terreno,
    funciona comprobando que los puntos no esten por encima del inicio de los arcos,
    ya que nunca habra puntos sin pilar, es suficiente con esta comprobacion.
    Y si no se solapan los putnos con el aqueducto,
    calcula el coste del aquaducto con todos los arcos posibles"""

    result_columns = 0
    result_distances = 0
    for i in range(0, n_points):
        if i < n_points - 1:
            radio = (float(pos_x[i + 1]) - float(pos_x[i])) / 2
            center_y = h_max - radio
            if center_y < int(pos_y[i]) or center_y < int(pos_y[i + 1]):
                return "impossible"
            dist = int(pos_x[i + 1]) - int(pos_x[i])
            result_distances = float(result_distances + (dist**2))
        result_columns = float(result_columns + (h_max - int(pos_y[i])))
    result_columns = float(alpha * result_columns)
    result_distances = float(beta * result_distances)
    result_total = float(result_columns + result_distances)
    ## Sumatorio de alturas de columnas
    ## Sumatorio de distancias al cuadrado de puntes
    #result_distances = 0
    #for i in range(0, n_points - 1):
    #    dist = int(pos_x[i + 1]) - int(pos_x[i])
    #    result_distances = float(result_distances + (dist ** 2))
    #result_distances = float(beta * result_distances)
    #result_total = float(result_columns + result_distances)
    return result_total


def calculate_cost_one_arch(n_points, pos_x, pos_y):
    if doesnt_overlap_one_arch(n_points, pos_x, pos_y):
        result_columns = 0
        result_columns = float(result_columns + (h_max - int(pos_y[0])))
        #result_columns = float(result_columns + (h_max - int(pos_y[n_points - 1])))
        result_columns = alpha * result_columns

        result_distances = 0
        result_distances = result_distances + \
            ((int(pos_x[-1]) - int(pos_x[0])) * (int(pos_x[-1]) - int(pos_x[0])))
        result_distances = float(beta * result_distances)
        result_total = float(result_columns + result_distances)

        return result_total
    return "impossible"


#def doesnt_overlap_multiple_arches():
#for i in range(0, n_points - 1):
#   radio = (float(pos_x[i + 1]) - float(pos_x[i])) / 2
#  center_y = h_max - radio

# if center_y < int(pos_y[i]) or center_y < int(pos_y[i + 1]):
#    return False
#return True


def doesnt_overlap_one_arch(n_points, pos_x, pos_y):
    """Comprueba que ningun punto del terreno interfiera con la semicircunferencia de cada arco,
       si el angulo es mayor de 90 grados, el punto del terreno no se solapa con el
       aqueducto, pero si es menor de 90 grados, significa que si que interfiere."""
    terrain_point = [0, 0]
    print(pos_x)
    print(pos_y)
    d_horizontal = pos_x[-1] - pos_x[0]
    #center_y = h_max - float(max(pos_x)) / 2 # center y es la mitad del ancho total, tenemos que calcular la mitad del ancho de donde vaya el arco
    center_y = h_max - (d_horizontal / 2)

    ##comentado-print("-------Puntos-------")

    ##comentado-print(pos_x)
    ##comentado-print(pos_y)

    ##comentado-print(n_points)
    ##comentado-print(h_max, "max =",max(pos_x), pos_x[-1], center_y)
    ##comentado-print("--------------------")

    point1 = [0, 0]
    point1[0] = float(pos_x[0])
    point1[1] = center_y

    point2 = [0, 0]
    point2[0] = float(pos_x[n_points - 1])
    point2[1] = center_y

    for i in range(0, n_points):
        if center_y < int(pos_y[i]):
            terrain_point[0] = int(pos_x[i])
            terrain_point[1] = int(pos_y[i])
            angle = calculate_angle(point1, point2, terrain_point,
                                    d_horizontal)
            if angle < 90:
                return False
            #else:
            #seguir dando vueltas
    return True


def calculate_angle(point1, point2, terrain_point, distance_horizontal):
    """Calcula el angulo de incidencia entre un punto del terreno y dos puntos
       en los pilares a la altura del centro de la semicircunferencia"""

    #comentado-print("-------Angulo-------")
    #comentado-print(point1[0], point1[1])
    #comentado-print(point2[0], point2[1])
    #comentado-print(terrain_point[0], terrain_point[1])
    #comentado-print("--------------------")

    angle = 0

    #Distancia x e y del punto1 al punto del terreno
    distance1vector = [0, 0]
    distance1vector[0] = float(terrain_point[0] - point1[0])
    distance1vector[1] = float(terrain_point[1] - point1[1])

    #Distancia x e y del punto2 al punto del terreno
    distance2vector = [0, 0]
    distance2vector[0] = float(point2[0] - terrain_point[0])
    distance2vector[1] = float(terrain_point[1] - point2[1])

    distance1 = math.sqrt(distance1vector[0] * distance1vector[0] +
                          distance1vector[1] * distance1vector[1])
    distance2 = math.sqrt(distance2vector[0] * distance2vector[0] +
                          distance2vector[1] * distance2vector[1])

    cos_result = (((distance1 * distance1) + (distance2 * distance2) -
                   (distance_horizontal * distance_horizontal)) /
                  (2 * distance1 * distance2))
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

    directory = "aqueductes/"

    debug = True
    superDebug = True
    if superDebug == True:
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".in"):
                if filename == "secret-10.in":
                    continue

        #os.chdir("/mydir")
        #for file in glob.glob("*.txt"):

        #DIR = 'testing/'
        #for name in os.listdir(DIR):
        #if os.path.isfile(os.path.join(DIR, name)):
        # print(name)

                print(u"\n\u001b[36m-------- " + filename +
                      " --------\u001b[0m\n")
                #print(os.path.join(filename))

                #list = os.listdir("testing/") # dir is your directory path
                #number_files = len(list)
                #print (number_files)

                filename = filename[:-3]

                f = open(directory + filename + ".in", "r")
                valores = f.readline().split(" ")

                s = open(directory + filename + ".ans", "r")
                comparar_resultado = s.readline()

                n_points = int(valores[0])
                h_max = int(valores[1])
                alpha = int(valores[2])
                beta = int(valores[3])

                if is_valid():
                    pos_x = [0]  # X primera columna
                    pos_y = [0]  # Y segunda columna
                    if read_terrain():

                        #f.close # pylint dice que es innecesario ponerlo
                        #result = [0, 0]
                        #result = check_overlap_and_calculate_cost_multiple_arches()
                        #result[1] = calculate_cost_one_arch()

                        print("Calculando ...")

                        result = rec_func(n_points, pos_x, pos_y)
                        if result != "impossible":
                            result = result + (h_max - pos_y[-1]) * alpha

                        #print(int(result))

                        #result = int(result)
                        if debug == True:
                            print(u"\u001b[32mDebug Enabled\u001b[0m")
                            #print(pos_x)
                            #print(pos_y)
                            if result == "impossible":
                                print("impossible")
                                print(comparar_resultado)
                            else:
                                print(u"\n\u001b[33mResultado Calculado",
                                      int(result), u"\u001b[0m")
                                print(u"\u001b[32mResultado Correcto ",
                                      comparar_resultado, u"\u001b[0m")
                                comparar_resultado2 = " " + comparar_resultado
                                diff = int(result) - int(comparar_resultado)
                                print(diff)
                                #if int(result) == comparar_resultado or int(result) == comparar_resultado2:
                                if diff == 0:
                                    print(u"\u001b[32mOK\u001b[0m\n")
                                else:
                                    print(u"\u001b[31mMAL\u001b[0m\n")

                            #print(u"\u001b[36m" , pos_x , u"\u001b[0m")
                    else:
                        print("impossible")
                else:
                    print("impossible")
        exit(0)

    if debug == True:
        filename = "secret-08"

        f = open("aqueductes/" + filename + ".in", "r")
        valores = f.readline().split(" ")

        s = open("aqueductes/" + filename + ".ans", "r")
        comparar_resultado = s.readline()

    if debug == False:

        if len(sys.argv) != 2:
            print(
                u"\n\u001b[31mTienes que indicar el nombre le archivo\u001b[0m\n"
            )
            exit(0)
        f = open(sys.argv[1], "r")
        valores = f.readline().split(" ")

    n_points = int(valores[0])
    h_max = int(valores[1])
    alpha = int(valores[2])
    beta = int(valores[3])

    if is_valid():
        pos_x = [0]  # X primera columna
        pos_y = [0]  # Y segunda columna
        if read_terrain():

            #f.close # pylint dice que es innecesario ponerlo
            #result = [0, 0]
            #result = check_overlap_and_calculate_cost_multiple_arches()
            #result[1] = calculate_cost_one_arch()

            result = rec_func(n_points, pos_x, pos_y)

            #print(" " + str(int(result)))
            #print(int(result))
            print("\n")
            print(result)
            print("\n")

            #result = int(result)
            if debug == True:
                print(u"\u001b[32mDebug Enabled\u001b[0m")
                print(pos_x)
                print(pos_y)
                print(u"\n\u001b[33mResultado Calculado", int(result),
                      u"\u001b[0m")
                print(u"\u001b[32mResultado Correcto ", comparar_resultado,
                      u"\u001b[0m")
                comparar_resultado2 = " " + comparar_resultado
                diff = int(result) - int(comparar_resultado)
                print(diff)
                #if int(result) == comparar_resultado or int(result) == comparar_resultado2:
                if diff == 0:
                    print(u"\u001b[32mOK\u001b[0m\n")
                else:
                    print(u"\u001b[31mMAL\u001b[0m\n")

                print(u"\u001b[36m", pos_x, u"\u001b[0m")
        else:
            print("impossible")
    else:
        print("impossible")
