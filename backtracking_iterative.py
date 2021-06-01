#! /usr/bin/env python3

"""Programa para calcular el coste de un aqueducto en modo BackTracking Iterativo."""
import os, os.path, glob
import math
import sys

#comentado-print(u"\u001b[36m\nBackTracking Recursivo\n\u001b[0m")


# BackTracking Iterativo
def it_func(n, pos_x, pos_y): # anadir mas parametros que hagan falta
    #numero de opciones ???
    i = 1
    while i <= n:
        print(n)
        print("hello")
        a = n - i # (a + 1) priemras posiciones
        b = n - a # (b) ultimas posiciones /// no hace falta calcularlo
        pos_x_a = pos_x[:a+1] # Array con las posiciones desde la primera hasta la (a + 1)
        pos_y_a = pos_y[:a+1]

        pos_x_b = pos_x[a:] # Array con las posiciones desde la a hasta la final
        pos_y_b = pos_y[a:]
            #llamada recursiva
            # Antes de sumar los resultados de las funciones los comprobamosm, y paramos el bucle si es necesario
            # Si las funciones nos retornan imposible, retornar imposible, para indicar que esa rama no es la buena y asi se acaba la llama recursiva lo antes posible, no hacemos mas llamadas de las siguientes vueltas del bucle
            
        while i<= a:

            aux_a = rec_func(a, pos_x_a, pos_y_a)

        while i<= b:

            aux_b = rec_func(b, pos_x_b, pos_y_b)

        n-=1
    return 0


# BackTracking Recursivo
def rec_func(n, pos_x, pos_y): # anadir mas parametros que hagan falta
    #coste = [int(0)] * (n+1)
    coste = {}
    #coste = [0 for i in range(5)]
    # Calculo de costes con llamadas recursivas
    #for (int i = 1; i < n; i++): # n - 1 vueltas
    #n_tramos = n - 1
    if n > 2:
        i = 1
        while i < n - 1:

            #print(n)

            a = n - i # (a + 1) priemras posiciones
            b = n - a +  1 # (b) ultimas posiciones /// no hace falta calcularlo
            # Coger el rango de array correcto para pasarlo a las funciones
            #:1 o :-1
            #comentado-print("\n")
            #comentado-print(" - A", a, "B",b, "N", n)

            pos_x_a = pos_x[:a] # Array con las posiciones desde la primera hasta la (a + 1)
            pos_y_a = pos_y[:a]

            #comentado-print(u"\u001b[36m", pos_x_a ,u"\u001b[0m")

            pos_x_b = pos_x[a - 1:] # Array con las posiciones desde la a hasta la final
            pos_y_b = pos_y[a - 1:]
            #comentado-print(u"\u001b[36m" , pos_x_b , u"\u001b[0m")
            #llamada recursiva
            # Antes de sumar los resultados de las funciones los comprobamosm, y paramos el bucle si es necesario
            # Si las funciones nos retornan imposible, retornar imposible, para indicar que esa rama no es la buena y asi se acaba la llama recursiva lo antes posible, no hacemos mas llamadas de las siguientes vueltas del bucle


            aux_a = rec_func(a, pos_x_a, pos_y_a)
            aux_b = rec_func(b, pos_x_b, pos_y_b)


                #if aux_a && aux_b == "impossible"
                #    return "aux_a"


            ##comentado-print(aux_a)
            ##comentado-print(aux_b)

            if aux_a == "impossible" or aux_b == "impossible":
                coste[i]= "impossible"
                #coste.append("impossible")
            else:
                pilar_contado_por_dos = (h_max - pos_y[a - 1] ) * alpha
                coste[i] = aux_a + aux_b - pilar_contado_por_dos # Quitarle el coste del pilar en comun
                #comentado-print(coste[i],"=",aux_a, "+" ,aux_b ,"-",pilar_contado_por_dos)
                #coste.append(aux_a + aux_b - pilar_contado_por_dos)

            ##comentado-print(coste[i])

            #coste[i] = rec_func(a, pos_x_a, pos_y_a) + rec_func(b, pos_x_b, pos_y_b)
            i += 1

    # Calculo de costes para un solo arco
    coste[n] = calculate_cost_one_arch(n, pos_x,  pos_y) # dos puntos del terreno y la altura máxima
    #coste.append(calculate_cost_one_arch(n, pos_x,  pos_y)) # dos puntos del terreno y la altura máxima
    #comentado-print(u"\u001b[35m", pos_x ,u"\u001b[0m")
    #coste[n] = 5
    ##comentado-print(coste[n])

    #for i in coste: ## hacer en caso de que el min no pueda gestionar strings "imposible"
     #   if coste[i] == "impossible":
      #      return  "impossible"

    #for i in coste:
        #if coste[i] == 6460:
         #   #comentado-print("IF bucle", int(coste[i]))
            ###comentado-print("OK")
        ##comentado-print("IF bucle", coste[i])

    #return coste[n]
    ##comentado-print("----Vuelta----")
    #return coste[min(coste)]

    # Minimo de los costes , hay que ver como hacerlo
    #comentado-print(" -- coste",coste)

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
                #comentado-print("+++++++++++++++++++++++++++++++++++", coste[k], "+++++++++++++++++++++++++++++++++++")
                result = coste[k]

    """
    # Minimo de los costes
    result = coste[n]
    for i in coste:
        if coste[i] != "impossible":
            if coste[i] < result:
             result = coste[i]
        else:
            coste[i]= "impossible"
    #result = coste[min(coste)]"""

    #comentado-print(result)

    return result


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
            result_distances = float(result_distances + (dist ** 2))
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
        result_columns = float(result_columns + (h_max - int(pos_y[n_points - 1])))
        result_columns = alpha * result_columns

        result_distances = 0
        result_distances = result_distances + \
            ((int(pos_x[n_points-1]) - int(pos_x[0])) * (int(pos_x[n_points-1]) - int(pos_x[0])))
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
            angle = calculate_angle(point1, point2, terrain_point, d_horizontal)
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

    directory = "testing/"

    debug = True
    superDebug = False
    if superDebug == True:
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".in"):
                
        #os.chdir("/mydir")
            #for file in glob.glob("*.txt"):
        
                #DIR = 'testing/'
                #for name in os.listdir(DIR): 
                    #if os.path.isfile(os.path.join(DIR, name)):
                       # print(name)

                print(u"\n\u001b[36m-------- " + filename+ " --------\u001b[0m\n")
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
                    pos_x = [0]              # X primera columna
                    pos_y = [0]              # Y segunda columna
                    if read_terrain():
                        
                        #f.close # pylint dice que es innecesario ponerlo
                        #result = [0, 0]
                        #result = check_overlap_and_calculate_cost_multiple_arches()
                        #result[1] = calculate_cost_one_arch()
                        
                        print("Calculando ...")

                        result = rec_func(n_points, pos_x, pos_y)
                        
                        print(" " + str(int(result)))
                        #print(int(result))

                        #result = int(result)
                        if debug == True:
                            print(u"\u001b[32mDebug Enabled\u001b[0m")
                            print(pos_x)
                            print(pos_y)
                            print(u"\n\u001b[33mResultado Calculado", int(result) , u"\u001b[0m")
                            print(u"\u001b[32mResultado Correcto ", comparar_resultado , u"\u001b[0m")
                            comparar_resultado2 = " " + comparar_resultado
                            diff = int(result) - int(comparar_resultado)
                            print(diff)
                            #if int(result) == comparar_resultado or int(result) == comparar_resultado2:
                            if diff == 0:
                                print(u"\u001b[32mOK\u001b[0m\n")
                            else:
                                print(u"\u001b[31mMAL\u001b[0m\n")

                            print(u"\u001b[36m" , pos_x , u"\u001b[0m")
                    else:
                        print("impossible")
                else:
                    print("impossible")
        exit(0)
    
    if debug == True:
        filename = "secret-08"

        f = open("aqueductes/" + filename +".in", "r")
        valores = f.readline().split(" ")

        s = open("aqueductes/" + filename + ".ans", "r")
        comparar_resultado = s.readline()

    if debug == False:
        
        if len(sys.argv) != 2:
            print(u"\n\u001b[31mTienes que indicar el nombre le archivo\u001b[0m\n")
            exit(0)
        f = open(sys.argv[1], "r")
        valores = f.readline().split(" ")

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
                print(u"\n\u001b[33mResultado Calculado", int(result) , u"\u001b[0m")
                print(u"\u001b[32mResultado Correcto ", comparar_resultado , u"\u001b[0m")
                comparar_resultado2 = " " + comparar_resultado
                diff = int(result) - int(comparar_resultado)
                print(diff)
                #if int(result) == comparar_resultado or int(result) == comparar_resultado2:
                if diff == 0:
                    print(u"\u001b[32mOK\u001b[0m\n")
                else:
                    print(u"\u001b[31mMAL\u001b[0m\n")

                print(u"\u001b[36m" , pos_x , u"\u001b[0m")
        else:
            print("impossible")
    else:
        print("impossible")
