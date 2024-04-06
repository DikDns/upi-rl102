""" 
    Nama  : Andika Eka Kurnia 
    NIM   : 2306033  
    Kelas : 1A 
"""
import pandas as pd

df = pd.read_csv("./daftar_mahasiswa_2018.csv")

# 1. Tampilkan 10 data pertama
print("\nData Mahasiswa")
print(df.head(10))

# 2. Sorting berdasarkan kolom nama
print("\nData Mahasiswa yang telah diurutkan")
dfSorted = df.sort_values(by="Nama")

# 3. Filter berdasarkan NIM, Nama, L/P, Status, SKS, IP, dan Lama Studi(Smt)
dfFiltered = dfSorted.filter(
    items=["NIM", "Nama", "L/P", "Status", "SKS", "IP", "Lama Studi(Smt)"])
print(dfFiltered.head(10))

# 4. Rata-rata seluruh IPK Mahasiswa
print("\nRata-rata IPK Mahasiswa")
dfIPK = df.filter(items=["IPK"])
print(dfIPK.mean())

# 5. Jumlah Mahasiswa Laki-laki
dfGender = df.filter(items=["L/P"])

print("\nJumlah Mahasiswa Laki-laki")
dfLaki = dfGender.query('`L/P` == "L"')
print(dfLaki.count())

# 6. Jumlah Mahasiswa Perempuan
print("\nJumlah Mahasiswa Perempuan")
dfPerempuan = dfGender.query('`L/P` == "P"')
print(dfPerempuan.count())

# 7. Mahasiswa Perempuan Terdaftar
print("\nMahasiswa Perempuan Terdaftar")
dfPerempuan = dfFiltered.query('`L/P` == "P" and `Status` == "Terdaftar"')
print(dfPerempuan)

# 8. Mahasiswa bukan Terdaftar
print("\nMahasiswa bukan Terdaftar")
dfBukanTerdaftar = dfFiltered.query('`Status` != "Terdaftar"')
print(dfBukanTerdaftar)
