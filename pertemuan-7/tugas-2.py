awal = int(input("Masukkan nilai awal  : "))
akhir = int(input("Masukkan nilai akhir : ")) + 1

for index in range(awal, akhir):
    if index != awal:
        print(end=", ")
    if index % 5 == 0:
        print(end="pass")
    else:
        print(end=f"{index}")
