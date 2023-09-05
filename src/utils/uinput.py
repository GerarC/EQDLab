from .umatrix import string_to_matrix, is_valid

def matrix_input(msg) -> list:
    matrix_str = input(msg)
    try: matrix = string_to_matrix(matrix_str)
    except Exception:
        print("El formato de la matriz es erroneo, por favor revisa cómo la digitaste.")
        return []
    if not is_valid(matrix): 
        print("La matriz que digitaste no es válida, debe ser cuadrada o tener solo una fila.")
        return []
    return matrix
