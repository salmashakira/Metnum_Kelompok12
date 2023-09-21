'''
METNUM Kelompok 12
No. 2
'''

import numpy as np
import matplotlib.pyplot as plt

def my_bisection(func, a, b, tol=1e-6, max_iterations=100):
    iterations = 0
    results = []  # Menyimpan hasil iterasi untuk grafik

    while iterations < max_iterations:
        c = (a + b) / 2
        results.append(c)  # Menyimpan nilai c pada setiap iterasi
        if func(c) == 0 or (b - a) / 2 < tol:
            return c, results
        if np.sign(func(c)) == np.sign(func(a)):
            a = c
        else:
            b = c
        iterations += 1

    return None, results

def plot_bisection_results(func, a, b, tol=1e-6, max_iterations=100):
    root, results = my_bisection(func, a, b, tol, max_iterations)

    if root is not None:
        print("Akar yang ditemukan:", root)
    else:
        print("Metode Bagi Dua tidak konvergen.")

    x = np.linspace(a, b, 100)
    y = np.vectorize(func)(x)

    plt.plot(x, y, label='f(x)')
    plt.scatter(results, np.vectorize(func)(results), c='red', marker='x', label='Iterasi')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Metode Bagi Dua')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    func_str = input("Masukkan fungsi (gunakan 'x' sebagai variabel): ")
    func = lambda x: eval(func_str)
    a = float(input("Masukkan batas bawah: "))
    b = float(input("Masukkan batas atas: "))
    max_iterations = int(input("Masukkan jumlah maksimal iterasi: "))
    tol = float(input("Masukkan toleransi galat: "))

    plot_bisection_results(func, a, b, tol, max_iterations)
