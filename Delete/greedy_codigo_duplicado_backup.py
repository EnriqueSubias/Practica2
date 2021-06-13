
# Este archivo se puede borrar,
# es solo por si hace falta comprobar la estructura inicial del greedy

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

