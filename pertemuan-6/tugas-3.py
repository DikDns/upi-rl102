nilai_ujian = int(input("Masukkan nilai ujian siswa: "))
keuangan_keluarga = int(input("Masukkan kondisi keuangan keluarga: "))

if nilai_ujian > 90 and keuangan_keluarga < 2000000:
    print("Siswa akan mendapatkan beasiswa penuh")
elif nilai_ujian > 80 and keuangan_keluarga < 4000000:
    print("Siswa akan mendapatkan beasiswa parsial")
else:
    print("Siswa tidak akan mendapatkan beasiswa")
