total = int(input("Masukkan total belanja: "))
diskon = 0

if total > 500000:
    diskon = 0.1 * total
    print("Anda berhak mendapatkan diskon.")
else:
    print("Anda tidak berhak mendapatkan diskon.")

print("Total yang harus dibayar:", total - diskon)
