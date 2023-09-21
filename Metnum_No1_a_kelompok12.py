'''
METNUM Kelompok 12
No. 1
a. f(x) = x^3 - 2x + 1
'''
import numpy as np

def my_bisection(func, a, b, tol=1e-6, max_iterations=100):
    iterations = 0
    while iterations < max_iterations:
        c = (a + b) / 2
        if func(c) == 0 or (b - a) / 2 < tol:
            return c
        if np.sign(func(c)) == np.sign(func(a)):
            a = c
        else:
            b = c
        iterations += 1
    return None

# Fungsi baru: f(x) = x^3 - 2x + 1
f = lambda x: x**3 - 2*x + 1

r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
print("f(r1) =", f(r1))

r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)
print("f(r01) =", f(r01))