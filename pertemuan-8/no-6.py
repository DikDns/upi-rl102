n = int(input("Masukkan nilai N = "))
jumlah_bilangan_prima = 0

for i in range(0, n):
    bilangan = int(input(f"Masukkan bilangan ke-{i + 1} = "))

    prima = True
    for j in range(2, bilangan):
        if (bilangan % j == 0):
            prima = False
            break

    if prima:
        jumlah_bilangan_prima += bilangan

if jumlah_bilangan_prima > 0:
    print("Jumlah bilangan prima adalah", jumlah_bilangan_prima)
else:
    print("Tidak ada item list yang bilangan prima")
