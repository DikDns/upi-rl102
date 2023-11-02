hasil = 1
list_bilangan = []

while True:
    list_bilangan.append(int(input("Input: ")))

    if len(list_bilangan) > 3 and list_bilangan[-1] >= list_bilangan[-2] and list_bilangan[-2] >= list_bilangan[-3] and list_bilangan[-3] >= list_bilangan[-4]:
        break

    if len(list_bilangan) > 1 and list_bilangan[-1] < list_bilangan[-2]:
       hasil *= list_bilangan[-1]

print("Hasil perkalian nilai yang mengecil:", hasil)