from utils.uinput import *
from utils.umatrix import matrix_multiplication, gauss_jordan

def print_first_info():
    print(
        'El formato de la matriz debe ser:',
        '\t[a11,a12,...,a1n;a21,a22,...,a2n;...;an1,an2,...,ann]',
        'separando los items de cada fila con comas,',
        'y separando cada fila usando punto y coma.\n',
        sep='\n'
    )
    print(
        'Ejemplo Dado:',
        '\tP: [1,0,0;0,0,1;0,1,0]',
        '\tU: [1,-2,1;0,7,-4;0,0,2]',
        '\tL: [1,0,0;3,1,0;-2,0,1]',
        '\tB: [7;-8;2]\n',
        sep = '\n'
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

def print_solution(p, u, l, b):
    print("\nUsando las matrices anteriores, el proceso es el siguiente:")
    # Hacer toda la operatoria

    print("\nCalcular la matriz PB")
    pb = matrix_multiplication(p,b)
    c = gauss_jordan(l, pb)
    x = gauss_jordan(u, c)
    print("\tPB: ", pb)
    print("Usando a PB y a L se encuentra C:")
    print("\tC: ", c);
    # El resultado final
    print("Y finalmente se hallamos X usando a U y a C.")
    print("El vector de resultados X es:\n\t", x)

def main():
    p, u, l, b = [[] for _ in range(4)]

    # Imprimir la información y pedir las matrices
    print_first_info()
    while not p: p = matrix_input("Digita la matriz P: ")
    while not u: u = matrix_input("Digita la matriz U: ")
    while not l: l = matrix_input("Digita la matriz L: ")
    while not b: b = matrix_input("Digita la matriz B: ")
    print('\n')

    print_matrixes(p, u, l, b)

    print_solution(p, u, l, b)
    

if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt: print("\nHubo una interrupción desde el teclado '^C'.\n")
