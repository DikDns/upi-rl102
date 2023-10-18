angka = input("Masukkan angka: ")

if not angka.isdigit():
    print("Maaf silahkan masukan angka")
else:
    angka = int(angka)
    if angka % 2 != 0:
        print("Angka", angka, "merupakan angka ganjil")
    else:
        print("Angka", angka, "merupakan angka genap")
