banyak_bilangan = int(input('Masukkan banyak bilangan: '))
bilangan_bukan_prima = 0

for i in range(0, banyak_bilangan):
    bilangan = int(input(f'Masukkan bilangan ke-{i+1}: '))

    prima = True
    for i in range(2, bilangan):
        if (bilangan % i == 0):
            prima = False
            break

    if not prima:
        bilangan_bukan_prima += bilangan

print(f'Hasil penjumlahan bilangan yang bukan prima: {bilangan_bukan_prima}')
