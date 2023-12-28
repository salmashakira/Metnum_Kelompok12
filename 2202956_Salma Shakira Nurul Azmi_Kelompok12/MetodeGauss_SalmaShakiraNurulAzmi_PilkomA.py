'''
Nama : Salma Shakira Nurul Azmi
NIM : 2202956
Kelas : Pendidikan Ilmu Komputer A
Metode Gauss
'''

# Mengimpor library NumPy untuk operasi matriks
import numpy as np

# Mendefinisikan fungsi gaussian_partial untuk melakukan eliminasi Gauss dengan pembagian parsial
def gaussian_partial(A, b):
    # Mendapatkan ukuran matriks A
    n = A.shape[0]

    # Menggabungkan matriks A dan matriks vektor b menjadi matriks C
    C = np.c_[A, b.reshape(-1, 1)]

    # Inisialisasi flag untuk penanganan kasus khusus
    flag = 0

    # Iterasi untuk melakukan eliminasi Gauss
    for i in range(n - 1):
        max_c, chosen_k = 0, i

        # Mencari baris dengan elemen terbesar dalam kolom i
        for k in range(i, n):
            if np.abs(C[k, i]) > max_c:
                max_c = np.abs(C[k, i])
                chosen_k = k

        # Jika elemen terbesar adalah 0, solusi tidak unik
        if max_c == 0:
            flag = 1
            break

        # Jika baris yang dipilih tidak sama dengan baris saat ini, tukar baris
        if chosen_k != i:
            temp = C[i, :].copy()
            C[i, :] = C[chosen_k, :]
            C[chosen_k, :] = temp

        # Proses eliminasi Gauss untuk mengubah elemen-elemen di bawah A[i, i] menjadi 0
        for j in range(i + 1, n):
            c = C[j, i] / C[i, i]
            C[j, :] = C[j, :] - c * C[i, :]

    # Mengembalikan matriks C hasil eliminasi Gauss dan flag
    return C, flag

# Mendefinisikan fungsi backsubstitution untuk melakukan substitusi mundur
def backsubstitution(T):
    flag = 0
    n = T.shape[0]

    # Membuat matriks vektor X yang akan menampung solusi
    X = np.zeros((n))

    # Jika elemen diagonal terakhir adalah 0, solusi tidak unik
    if T[n - 1, n - 1] == 0:
        flag = 1
    else:
        # Menghitung solusi X[n-1]
        X[n - 1] = T[n - 1, n] / T[n - 1, n - 1]

        # Melakukan substitusi mundur untuk menghitung solusi X[i] untuk i dari n-2 hingga 0
        for i in range(n - 2, -1, -1):
            s = 0
            for j in range(i + 1, n):
                s += T[i, j] * X[j]

            X[i] = (T[i, n] - s) / T[i, i]

    # Mengembalikan matriks vektor X yang berisi solusi dan flag
    return X, flag

# Meminta input ukuran matriks A dari pengguna
n = int(input("Masukkan ukuran matriks (n x n): "))
A = []

# Meminta elemen-elemen matriks A dari pengguna
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")
for i in range(n):
    row = []
    for j in range(n):
        elem = float(input(f"A[{i+1}][{j+1}]: "))
        row.append(elem)
    A.append(row)

# Meminta elemen-elemen matriks vektor b dari pengguna
b = []
print("Masukkan elemen-elemen matriks B:")
for i in range(n):
    elem = float(input(f"B[{i+1}]: "))
    b.append([elem])

# Memanggil fungsi gaussian_partial untuk melakukan eliminasi Gauss
T, err = gaussian_partial(np.array(A), np.array(b))

# Menangani kasus jika solusi tidak unik
if err:
    print('Solusi tidak unik')
else:
    # Memanggil fungsi backsubstitution untuk menghitung solusi sistem persamaan linier
    X, err = backsubstitution(T)

    # Menangani kasus jika solusi tidak unik
    if err:
        print('Solusi tidak unik')
    else:
        # Mencetak solusi sistem persamaan linier
        print('Solusi:')
        for i, val in enumerate(X):
            print(f"X{i+1} = {val}")