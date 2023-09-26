'''
Nama : Salma Shakira Nurul Azmi
NIM : 2202956
Kelas : Pendidikan Ilmu Komputer A
Newton Rapshon

Contoh soal: Tentukan akar persamaan f(x)=e^x-5x^2 dengan tebakan_awal = 1

Inputan:
Masukkan Tebakan Awal : 1.0
Masukkan Toleransi Error : 1e-6
Masukkan Jumlah Iterasi : 100
'''
 
# Mendefinisikan fungsi f(x)
def fungsi_f(x):
    return pow(2.71828, x) - 5 * pow(x, 2)

# Mendefinisikan fungsi turunan pertama g(x)
def turunan_f(x):
    return pow(2.71828, x) - 10 * x

# Mendefinisikan fungsi metode Newton-Raphson
def newtonRaphson(tebakan_awal, toleransi_error, jumlah_iterasi):
    langkah = 1
    konvergen = 1
    kondisi = True

    while kondisi:
        if turunan_f(tebakan_awal) == 0.0:
            print('Error: Terjadi pembagian oleh nol.')
            break

        # Iterasi
        tebakan_baru = tebakan_awal - fungsi_f(tebakan_awal) / turunan_f(tebakan_awal)
        print(f'Iterasi-{langkah}, x{langkah} = {tebakan_baru:.6f} dan f(x{langkah}) = {fungsi_f(tebakan_baru):.6f}')

        tebakan_awal = tebakan_baru
        langkah += 1

        if langkah > jumlah_iterasi:
            konvergen = 0
            break

        kondisi = abs(fungsi_f(tebakan_baru)) > toleransi_error

    if konvergen == 1:
        print('\nAkar yang diestimasi: {0:.8f}'.format(tebakan_baru))
    else:
        print('\nMetode tidak konvergen')

# Input tebakan awal, toleransi error, dan jumlah iterasi
tebakan_awal = float(input('Masukkan Tebakan Awal: '))
toleransi_error = float(input('Masukkan Toleransi Error: '))
jumlah_iterasi = int(input('Masukkan Jumlah Iterasi: '))

# Memanggil fungsi Newton-Raphson
newtonRaphson(tebakan_awal, toleransi_error, jumlah_iterasi)
