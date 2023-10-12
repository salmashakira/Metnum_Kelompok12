import numpy as np

def dekomposisiLU(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.copy(A)

    for k in range(n-1):
        for j in range(k+1, n):
            m = U[j][k] / U[k][k]
            L[j][k] = m
            for i in range(k, n):
                U[j][i] = U[j][i] - m * U[k][i]

    return L, U

def solusiLU(L, U, b):
    n = len(L)
    y = np.zeros((n, 1))
    x = np.zeros((n, 1))

    for j in range(n):
        S = 0
        for i in range(j):
            S = S + y[i][0] * L[j][i]
        y[j][0] = b[j][0] - S

    for j in range(n-1, -1, -1):
        S = 0
        for i in range(j+1, n):
            S = S + U[j][i] * x[i][0]
        x[j][0] = (y[j][0] - S) / U[j][j]

    return x

def caraLU(A, b):
    L, U = dekomposisiLU(A)
    
    print('Matriks L')
    print(L)

    print('Matriks U')
    print(U)

    x = solusiLU(L, U, b)

    print('Solusi:\n')
    for i in range(len(x)):
        print(f'X{i+1} = {x[i]}')

A = []
n = int(input("Masukkan uk matriks (nxn) : "))
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n):
    row = []
    for j in range(n):
        element = float(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    A.append(row)

b = []
print("Masukkan elemen-elemen matriks B:")
for i in range(n):
    element = float(input(f"B[{i+1}]: "))
    b.append([element])

caraLU(np.array(A), np.array(b))