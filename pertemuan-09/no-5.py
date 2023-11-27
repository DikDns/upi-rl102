def nilai_mutlak(angka=0):
    if angka < 0:
        return -angka

    return angka


def selisih(a, b):
    return nilai_mutlak(a - b)


print("Input mulai:")
a_jam = int(input("Jam: "))
a_menit = int(input("Menit: "))
a_detik = int(input("Detik: "))

print("Input selesai:")
b_jam = int(input("Jam: "))
b_menit = int(input("Menit: "))
b_detik = int(input("Detik: "))


print("Hitung selisih:")
print(
    f"Output: {selisih(a_jam, b_jam)} jam - {selisih(a_menit, b_menit)} menit - {selisih(a_detik, b_detik)} detik")
