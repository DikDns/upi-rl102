jumlah_kelipatan_4 = 0
jumlah_kelipatan_5 = 0
angka = 0

while angka >= 0:
    if angka % 4 == 0:
        jumlah_kelipatan_4 += angka

    if angka % 5 == 0:
        jumlah_kelipatan_5 += angka

    angka = int(input("Input: "))


print("\nJumlah bilangan kelipatan 4:", jumlah_kelipatan_4)
print("Jumlah bilangan kelipatan 5:", jumlah_kelipatan_5)
