hasil = 0
list_bilangan = []

while True:
    list_bilangan.append(int(input("Input bilangan : ")))

    if len(list_bilangan) > 3 and list_bilangan[-1] <= list_bilangan[-2] and list_bilangan[-2] <= list_bilangan[-3] and list_bilangan[-3] <= list_bilangan[-4]:
        break

    if len(list_bilangan) > 1 and list_bilangan[-1] > list_bilangan[-2]:
        hasil += list_bilangan[-1]

print("\nHasil penjumlahan nilai yang membesar :", hasil)