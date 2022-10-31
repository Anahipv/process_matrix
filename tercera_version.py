
from functools import reduce

def process_matrix(matrix):
    """
    Recibe una matriz de numeros y devuelve una nueva con los elementos cambiados.
    Cada elemento de la nueva sera el promedio del valor antiguo y el de sus vecinos en las 4 direcciones
    """
    processed_matrix = []
    if matrix == [] or len(matrix[0]) == 0:        
        processed_matrix = matrix
    else:
        for i, column in enumerate(matrix):
            processed_list = []
            for j, value in enumerate(column):
                coordinate = [i,j]
                new_value = process_element(coordinate, matrix)
                processed_list.append(new_value)
            processed_matrix.append(processed_list)
    return processed_matrix

def process_element(coordinate, matrix):
    """
    Recibe una coordenada, calcula su promedio con sus vecinos y devuelve dicho promedio
    """
    indices = get_neighbours_indices(coordinate)
    values = get_neighbour_values(indices, matrix)
    average = get_avarage(values)

    return average

def get_neighbours_indices(coordinate):
    """
    Recibe una coordenada y devuelve una lista de coordenadas vecinas en sus 4 direcciones
    """
    indices = []
    indices.extend([[coordinate[0], coordinate[1]-1],
                    [coordinate[0], coordinate[1]+1],
                    [coordinate[0]-1, coordinate[1]],
                    [coordinate[0]+1, coordinate[1]],
                    coordinate])
                    
    return indices

def get_neighbour_values(indices, matrix):
    """
    Recibe una lista de coordenadas con su matriz, filtra los incorrectos y devuelve una lista de los valores correspondientes
    """
    right_indices = list(filter(lambda x: len(matrix) > x[0] >= 0 and 0 <= x[1] < len(matrix[0]), indices))
    values = []
    for index in right_indices:
        values.append(matrix[index[0]][index[1]])

    return values

def get_avarage(values):
    return round((reduce(lambda accum, b : accum + b, values, 0) / len(values)), 2)


