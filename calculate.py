#! /usr/bin/env python3
"""Calculate"""

import math


class Calcul:
    """Calcul"""
    def __init__(self, n_points, h_max, alpha, beta):
        self.n_points = n_points
        self.h_max = h_max
        self.alpha = alpha
        self.beta = beta
        self.pos_x = [0]
        self.pos_y = [0]

    def calculate_cost(self, pos_x, pos_y, start, end):
        """A"""
        if self.doesnt_overlap_one_arch(pos_x, pos_y, start, end):
            result_columns = 0
            result_columns = float(result_columns +
                                   (self.h_max - int(pos_y[start])))
            # result_columns = float(result_columns + (self.h_max - int(pos_y[end])))
            result_columns = self.alpha * result_columns

            result_distances = 0
            result_distances = result_distances + (
                (int(pos_x[end]) - int(pos_x[start])) *
                (int(pos_x[end]) - int(pos_x[start])))
            result_distances = float(self.beta * result_distances)
            result_total = float(result_columns + result_distances)
            return result_total
        return "impossible"

    def calculate_cost_greedy(self, pos_x, pos_y, start, end):
        """A"""
        if self.doesnt_overlap_one_arch(pos_x, pos_y, start, end):
            result_columns = 0
            result_columns = float(result_columns +
                                   (self.h_max - int(pos_y[start])))
            result_columns = float(result_columns +
                                   (self.h_max - int(pos_y[end])))
            result_columns = self.alpha * result_columns

            result_distances = 0
            result_distances = result_distances + (
                (int(pos_x[end]) - int(pos_x[start])) *
                (int(pos_x[end]) - int(pos_x[start])))
            result_distances = float(self.beta * result_distances)
            result_total = float(result_columns + result_distances)
            return result_total
        return "impossible"

    def doesnt_overlap_one_arch(self, pos_x, pos_y, start, end):
        """Comprueba que ningun punto del terreno interfiera con la semicircunferencia de cada arco,
        si el angulo es mayor de 90 grados, el punto del terreno no se solapa con el
        aqueducto, pero si es menor de 90 grados, significa que si que interfiere."""

        terrain_point = [0, 0]
        d_horizontal = pos_x[end] - pos_x[start]
        # center_y = h_max - float(max(pos_x)) / 2 # center y es la mitad del ancho total,
        # tenemos que calcular la mitad del ancho de donde vaya el arco
        center_y = self.h_max - (d_horizontal / 2)

        point1 = [0, 0]
        point1[0] = float(pos_x[start])
        point1[1] = center_y

        point2 = [0, 0]
        point2[0] = float(pos_x[end])
        point2[1] = center_y

        for i in range(start, len(pos_x)):
            if center_y < int(pos_y[i]):
                terrain_point[0] = int(pos_x[i])
                terrain_point[1] = int(pos_y[i])
                angle = self.calculate_angle(point1, point2, terrain_point,
                                             d_horizontal)
                if angle < 90:
                    return False
                # else:
                # seguir dando vueltas
        return True

    @classmethod
    def calculate_angle(cls, point1, point2, terrain_point,
                        distance_horizontal):
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

    def is_valid(self):
        """Comprueba que los parametros de la primera linea son correctos segun el enunciado."""
        if (self.n_points < 2 or self.n_points > 10000 or self.h_max < 1
                or self.h_max > 100000):
            return False
        if self.alpha < 1 or self.alpha > 10000 or self.beta < 1 or self.beta > 10000:
            return False
        return True

    def read_valores_aqueductor(self, file_name):
        """A"""
        valores = file_name.readline().split(" ")
        self.n_points = int(valores[0])
        self.h_max = int(valores[1])
        self.alpha = int(valores[2])
        self.beta = int(valores[3])

    def read_terrain(self, file_name):
        """Lee los puntos del terreno y comprueba que esten por debajo de la altura maxima"""
        for i in file_name:
            string_doc = i.split(" ")
            if float(string_doc[1]) > self.h_max:
                return False
            self.pos_x.append(float(string_doc[0]))
            self.pos_y.append(float(string_doc[1]))
        self.pos_x.pop(0)
        self.pos_y.pop(0)
        return True

    def get_n_points(self):
        """A"""
        return self.n_points

    def get_h_max(self):
        """A"""
        return self.h_max

    def get_alpha(self):
        """A"""
        return self.alpha

    def get_beta(self):
        """A"""
        return self.beta

    def get_pos_x(self):
        """A"""
        return self.pos_x

    def get_pos_y(self):
        """A"""
        return self.pos_y
