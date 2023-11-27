"""
Solusi andika, which is kejauhan mikirnya
while(True):
    angka = input("Masukkan bilangan ganjil yang lebih dari 50: ")

    if angka.isdigit() == False:
        print("Salah, inputkan lagi:", angka, "\n")
        continue

    angka = int(angka)
    if angka > 50 and angka % 2 != 0:
        print("Benar!")
        break
    else:
        print("Salah, inputkan lagi:", angka, "\n")
"""

"""
Solusi Fatra, Andika, Alwan, dan Bu Indira
"""
angka = int(input("Masukkan angka: "))

while not (angka > 50 and angka % 2 != 0):
    angka = int(input("Salah, masukkan angka: "))

print("Benar!")