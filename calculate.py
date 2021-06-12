
import math
import sys

class calcul:

    def __init__(self, n_points, h_max, alpha, beta):
        self.n_points = n_points
        self.h_max = h_max
        self.alpha = alpha
        self.beta = beta

    def calculate_cost_one_arch_backtraking(self,n_points, pos_x, pos_y):
        if self.doesnt_overlap_one_arch(n_points, pos_x, pos_y):
            result_columns = 0
            result_columns = float(result_columns + (self.h_max - int(pos_y[0])))
            #result_columns = float(result_columns + (h_max - int(pos_y[n_points - 1])))
            result_columns = self.alpha * result_columns

            result_distances = 0
            result_distances = result_distances + \
                ((int(pos_x[-1]) - int(pos_x[0])) * (int(pos_x[-1]) - int(pos_x[0])))
            result_distances = float(self.beta * result_distances)
            result_total = float(result_columns + result_distances)

            return result_total
        return "impossible"

    def doesnt_overlap_one_arch(self,n_points, pos_x, pos_y):
        """Comprueba que ningun punto del terreno interfiera con la semicircunferencia de cada arco,
        si el angulo es mayor de 90 grados, el punto del terreno no se solapa con el
        aqueducto, pero si es menor de 90 grados, significa que si que interfiere."""
        terrain_point = [0, 0]
        d_horizontal = pos_x[-1] - pos_x[0]
        #center_y = h_max - float(max(pos_x)) / 2 # center y es la mitad del ancho total, tenemos que calcular la mitad del ancho de donde vaya el arco
        center_y = self.h_max - (d_horizontal / 2)


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
                angle = self.calculate_angle(point1, point2, terrain_point, d_horizontal)
                if angle < 90:
                    return False
                #else:
                    #seguir dando vueltas
        return True

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

    def calculate_angle(self,point1, point2, terrain_point, distance_horizontal):
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