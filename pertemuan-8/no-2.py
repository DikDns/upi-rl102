jumlah_bilangan_genap = 0
jumlah_bilangan_ganjil = 0
bilangan = 0

while bilangan >= 0:
    if bilangan % 2 == 0:
        jumlah_bilangan_genap += bilangan
    else:
        jumlah_bilangan_ganjil += bilangan

    bilangan = int(input("Input bilangan : "))


print("\nJumlah bilangan genap :", jumlah_bilangan_genap)
print("Jumlah bilangan ganjil :", jumlah_bilangan_ganjil)
