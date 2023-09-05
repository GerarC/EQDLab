def string_to_matrix(matrix_str: str):
    tokens = [ tkn[1: -1] for tkn in matrix_str.split(";") ]
    matrix = [ list(map(float, token.split(','))) for token in tokens ]
    if len(matrix) == 1: return matrix[0]
    return matrix

def is_valid(matrix):
    try: m = len(matrix[0])
    except TypeError: m = 1
    n = len(matrix)
    for row in matrix:
        try: l = len(row)
        except TypeError: l = 1
        if l != m: return False
    return (m == n) or (m == 1 and n >= 1)

def matrix_multiplication(A: list, B: list) -> list:
    if len(A[0]) != len(B): return []
    B_T = [b_col for b_col in zip(*B)]
    C = [[ sum(a*b for a,b in zip(A_row, B_col)) for B_col in B_T ] 
        for A_row in A ]
    return C

def gauss_jordan(A: list, b: list):
    n = len(A)
    M = A.copy()

    i = 0
    for x in M:
        x.append(b[i][0])
        i += 1

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]): M[k], M[i] = M[i], M[k]
            else: pass
        for j in range(k+1, n):
            q = M[j][k] / M[k][k]
            for m in range(k, n+1): M[j][m] -= q * M[k][m]

    x = [[0] for _ in range(n)]

    x[n-1][0] = M[n-1][n] / M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n): z = z  + M[i][j]*x[j][0]
        x[i][0] = round((M[i][n] - z) / M[i][i], 3)
    return x

