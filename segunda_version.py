
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
        transformed_matrix = transform_matrix(matrix)
        for i, column in enumerate(matrix):
            processed_list = []
            for j, value in enumerate(column):
                coordinate = [i+1,j+1]
                new_value = process_element(coordinate, transformed_matrix)
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
    Recibe una lista de coordenadas con su matriz y devuelve una lista de los valores correspondientes
    """
    values = []
    for index in indices:
        values.append(matrix[index[0]][index[1]])

    return values

def get_avarage(values):
    """
    Elimina los None de una lista de valores y devuleve su promedio
    """
    filter_values = list(filter(lambda x: x != None, values))
    return round((reduce(lambda accum, b : accum + b, filter_values, 0) / len(filter_values)), 2)

def transform_matrix(matrix):
    """
    Recibe una matriz y agrega None en todos los bordes
    """  
    new_matrix = []
    for column in matrix:
        row = []
        for element in column:
            row.append(element)
        new_matrix.append(row)
    for i in new_matrix:
        i.append(None)
        i.insert(0, None)
    len_list = len(new_matrix[0])
    zeros_list = [None for i in range(len_list)]
    new_matrix.append(zeros_list)
    new_matrix.insert(0, zeros_list)

    return new_matrix
    