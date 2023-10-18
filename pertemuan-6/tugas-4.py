print(f"[]{'='*10} Kalkulasi Bonus Tahunan Karyawan {'='*10}[]")
print("Kategori Performa Karyawan: 1. Sangat Baik, 2. Cukup")

performa = input("Masukkan kategori performa karyawan: ")
gaji = input("Masukkan gaji karyawan: ")

if not gaji.isdigit():
    print("Gaji karyawan harus berupa angka")
else:
    bonus = 0
    if not performa.isnumeric():
        bonus = 0.05 * int(gaji)
    elif int(performa) == 2:
        bonus = 0.1 * int(gaji)
    elif int(performa) == 1:
        bonus = 0.2 * int(gaji)
    else:
        bonus = 0.05 * int(gaji)
    print(f"Bonus karyawan: {bonus}")
