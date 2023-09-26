'''
Nama : Salma Shakira Nurul Azmi
NIM : 2202956
Kelas : Pendidikan Ilmu Komputer A
Newton Rapshon
'''

# Fungsi Newton-Raphson untuk mencari akar suatu fungsi
def newton_raphson(f, df, xi, e):
    print("Nilai xi awal: ", xi)  # Cetak nilai xi awal
    if abs(f(xi)) < e:  # Cek apakah nilai f(xi) sudah mendekati nol
        return xi
    else:
        # Hitung nilai xi yang baru dengan metode Newton-Raphson
        xi = xi - f(xi) / df(xi)
        # Rekursi: Panggil fungsi ini kembali dengan nilai xi yang baru
        return newton_raphson(f, df, xi, e)

# Definisikan fungsi f(x), turunan pertamanya f'(x), dan nilai awal xi
fx = lambda x: ((x**2) + (5*x) - 10)  # Fungsi f(x)
f_prime = lambda x: 2*x + 5  # Turunan pertama f(x)
n = float(input("Masukkan Tebakan Awal (xi): "))  # Input nilai awal xi

# Panggil fungsi Newton Raphson untuk mencari akar
estimate = newton_raphson(fx, f_prime, n, 1e-5)  # Toleransi kesalahan: 1e-5

# Cetak hasil akar yang ditemukan
print("Akar yang diestimasi = %.3f" % estimate)
