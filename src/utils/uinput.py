from .umatrix import string_to_matrix, is_valid

def matrix_input(msg: str) -> list:
    """ Receives the input of the user and create a matrix with it.

    Args:
        msg (str): a message to print to the user which Matrix must send.

    Returns:
        matrix (list): the resulting matrix, parsed and validated. 
    """
    matrix_str = input(msg)
    try: matrix = string_to_matrix(matrix_str)
    except ValueError:
        print("Algún ítem de los que has digitado no se puede convertir a flotante.")
        return []
    except Exception:
        print("El formato de la matriz es erroneo, por favor revisa cómo la digitaste.")
        return []
    if not is_valid(matrix): 
        print("La matriz que digitaste no es válida, debe ser cuadrada o tener solo una fila.")
        return []
    return matrix
