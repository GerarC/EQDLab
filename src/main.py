from utils.uinput import *
from utils.umatrix import matrix_multiplication, gauss_jordan

def print_first_info():
    print(
        'Ejemplo Dado:',
        '\tP: [1,0,0];[0,0,1];[0,1,0]',
        '\tU: [1,-2,1];[0,7,-4];[0,0,2]',
        '\tL: [1,0,0];[3,1,0];[-2,0,1]',
        '\tB: [7];[-8];[2]\n',
        sep = '\n'
    )
    print(
        'El formato de la matriz debe ser:',
        '\t[a11,a12,...,a1n];[a21,a22,...,a2n];...;[an1,an2,...,ann]',
        'Es decir, insertar las filas usando corchetes,' + 
        'separando los items con comas,',
        'y separando cada fila usando punto y coma.\n',
        sep='\n'
    )

def print_matrixes(p, u, l, b):
    print(
        '\nMatrices:',
        f'\tP: {p}',
        f'\tU: {u}',
        f'\tL: {l}',
        f'\tB: {b}\n',
        sep = '\n'
    )

def main():
    l, u, p, b = [[] for _ in range(4)]
    print_first_info()

    while not p: p = matrix_input("Entra la matriz P: ")
    while not u: u = matrix_input("Entra la matriz U: ")
    while not l: l = matrix_input("Entra la matriz L: ")
    while not b: b = matrix_input("Entra la matriz B: ")
    print('\n')

    c = []
    pb = matrix_multiplication(p,b)
    c = gauss_jordan(l, pb)
    X = gauss_jordan(u, c)
    print("PB: ", pb)
    print("C: ", c)
    print("X: ", X)


if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt:
        print("\nSe ha interrumpido la ejecución desde el teclado '^C'.")
