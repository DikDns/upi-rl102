n = int(input("Masukkan angka: "))

jumlah = 0
for angka in range(3, n, 3):
    jumlah += angka

print(f"Jumlah bilangan kelipatan 3 dibawah {n} adalah {jumlah}")
