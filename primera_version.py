
from functools import reduce


def process_matrix(matrix):
    """
    Recibe una matriz de numeros y devuelve una nueva con los elementos cambiados.
    Cada elemento de la nueva sera el promedio del valor antiguo y el de sus vecinos en las 4 direcciones
    """
    processed_matrix = []
    if len(matrix) == 0 or len(matrix[0]) == 0:
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
    # obtengo la lista de vecinos
    indices = get_neighbours_indices(coordinate, matrix)
    values = get_neighbour_values(indices, matrix)
    # calculo su promedio
    average = get_avarage(values)
    # devuelvo el valor final
    return average

def get_neighbours(index, elements):
    neighbours = []
    if index == 0:
        neighbours.extend([elements[index], elements[index + 1]])
    elif index == len(elements) - 1:
        neighbours.extend([elements[index - 1], elements[index]])
    else:
        neighbours.extend([elements[index - 1], elements[index], elements[index + 1]])
    
    return neighbours

def get_neighbours_indices(coordinate, matrix):
    indices = []
    # si i es 0 y j es 0 (esq. superior izq)
    if coordinate == [0,0]:
        indices.append([coordinate[0], coordinate[1]+1])
        indices.append([coordinate[0]+1, coordinate[1]])
    # si i es el largo de la matriz - 1 y j es 0 (esq. inferior izq)
    elif coordinate == [len(matrix)-1, 0]:
        indices.append([coordinate[0], coordinate[1]+1])
        indices.append([coordinate[0]-1, coordinate[1]])
    # si i es 0 y j es el largo de la lista 0 menos 1 (esq. superior der)
    elif coordinate == [0,len(matrix[0])-1]:
        indices.append([coordinate[0], coordinate[1]-1])
        indices.append([coordinate[0]+1, coordinate[1]])
    # si i es el largo de la matriz - 1 y j es el largo de la lista 0 menos 1 (esq. inferior der)
    elif coordinate == [len(matrix)-1, len(matrix[0])-1]:
        indices.append([coordinate[0], coordinate[1]-1])
        indices.append([coordinate[0]-1, coordinate[1]])
    # si es la fila superior
    elif coordinate[0] == 0:
        indices.append([coordinate[0], coordinate[1]-1])
        indices.append([coordinate[0], coordinate[1]+1]) 
        indices.append([coordinate[0]+1, coordinate[1]])
    # si es la primer columna
    elif coordinate[1] == 0:
        indices.append([coordinate[0]-1, coordinate[1]])
        indices.append([coordinate[0]+1, coordinate[1]]) 
        indices.append([coordinate[0], coordinate[1]+1])
    # si es la ultima columna
    elif coordinate[1] == len(matrix[0])-1:
        indices.append([coordinate[0], coordinate[1]-1])
        indices.append([coordinate[0]-1, coordinate[1]]) 
        indices.append([coordinate[0]+1, coordinate[1]])
    # si es la fila inferior 
    elif coordinate[0] == len(matrix)-1:
        indices.append([coordinate[0], coordinate[1]-1])
        indices.append([coordinate[0], coordinate[1]+1]) 
        indices.append([coordinate[0]-1, coordinate[1]])
    # sino, esta en el medio
    else:
        indices.append([coordinate[0], coordinate[1]-1])
        indices.append([coordinate[0], coordinate[1]+1]) 
        indices.append([coordinate[0]-1, coordinate[1]])
        indices.append([coordinate[0]+1, coordinate[1]])

    indices.append(coordinate)    
    return indices

def get_neighbour_values(indices, matrix):
    values = []
    for index in indices:
        values.append(matrix[index[0]][index[1]])
    return values

def get_avarage(values):

    return round((reduce(lambda accum, b : accum + b, values, 0) / len(values)), 2)
