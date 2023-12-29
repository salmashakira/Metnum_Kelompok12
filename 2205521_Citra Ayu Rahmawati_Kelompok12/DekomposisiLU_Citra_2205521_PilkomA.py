Citra Ayu Rahmawati
2205521
PIKOM A

# Mengimpor library NumPy untuk operasi matriks
import numpy as np

# Mendefinisikan fungsi 'jalanLU' yang akan melakukan faktorisasi LU pada matriks A dengan matriks vektor b sebagai parameter
def jalanLU(A, b):
    n = len(A)  # Mendapatkan ukuran matriks A (n x n)
    L = np.zeros((n, n))  # Inisialisasi matriks L dengan nol
    for i in range(n):
        L[i][i] = 1  # Mengisi elemen diagonal matriks L dengan 1

    for k in range(n - 1):  # Memulai iterasi untuk faktorisasi matriks A menjadi L dan U

        if A[k][k] == 0:
            # Pertukaran baris jika elemen diagonal A[k][k] adalah 0 untuk menghindari pembagian oleh nol
            for s in range(n):
                v = A[k][s]
                u = A[k+1][s]
                A[k][s] = u
                A[k+1][s] = v

        for j in range(k+1, n):
            m = A[j][k] / A[k][k]  # Menghitung elemen matriks L
            L[j][k] = m
            for i in range(n):
                A[j][i] = A[j][i] - m * A[k][i]  # Menghitung elemen matriks U

    # Mencetak matriks L
    print('Matriks L')
    print(L)

    # Mencetak matriks U
    print('Matriks U')
    print(A)

    y = np.zeros((n, 1))  # Membuat matriks vektor y
    y[0][0] = b[0][0] / L[0][0]  # Menghitung elemen pertama matriks y

    for j in range(1, n):
        S = 0
        for i in range(j):
            S = S + y[i][0] * L[j][i]  # Menghitung elemen matriks y
        y[j][0] = b[j][0] - S  # Menghitung elemen matriks y

    x = np.zeros((n, 1))  # Membuat matriks vektor x
    x[n-1][0] = y[n-1][0] / A[n-1][n-1]  # Menghitung elemen terakhir matriks x

    for j in range(n-2, -1, -1):
        S = 0
        for i in range(j+1, n):
            S = S + A[j][i] * x[i][0]  # Menghitung elemen matriks x
        x[j][0] = (y[j][0] - S) / A[j][j]  # Menghitung elemen matriks x

    # Mencetak solusi sistem persamaan linier
    print('Solusi:\n')
    for i in range(n):
        print(f'X{i+1} = {x[i]}')

# Meminta input matriks A dari pengguna
A = []
n = int(input("Masukkan ukuran matriks (n x n): "))
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n):
    row = []
    for j in range(n):
        elem = float(input(f"A[{i+1}][{j+1}]: "))  # Meminta elemen-elemen matriks A
        row.append(elem)
    A.append(row)

# Meminta input matriks b dari pengguna
b = []
print("Masukkan elemen-elemen matriks B:")
for i in range(n):
    elem = float(input(f"B[{i+1}]: "))  # Meminta elemen-elemen matriks vektor b
    b.append([elem])

# Memanggil fungsi 'jalanLU' dengan matriks A dan b yang dimasukkan oleh pengguna
jalanLU(np.array(A), np.array(b))


