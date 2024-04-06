"""
    Nama  : Andika Eka Kurnia
    NIM   : 2306033 
    Kelas : 1A
"""
import pandas as pd

df = pd.read_csv("./daftar_penjualan_2023.csv", parse_dates=["Tanggal"])

print(df.head())

# 1. Total pendapatan setiap bulannya
pendapatan_per_bulan = df.groupby(
    df["Tanggal"].dt.strftime("%B"))["Total"].sum()

print("\nTotal Pendapatan Setiap Bulannya")
print(pendapatan_per_bulan)

# 2. Rata-rata pendapatan 2023
rata_rata_pendapatan = df["Total"].mean()
print("\nRata-rata Pendapatan 2023")
print(rata_rata_pendapatan)

# 3. Pendapatan Paling Sedikit
pendapatan_min = df["Total"].min()
print("\nPendapatan Paling Sedikit")
print(pendapatan_min)

# 4. Pendapatan Paling Banyak
pendapatan_max = df["Total"].max()
print("\nPendapatan Paling Banyak")
print(pendapatan_max)

# 5. Produk terlaris yang paling banyak terjual
produk_terlaris = df.groupby(
    "Produk")["Jumlah"].sum().sort_values(ascending=False)
print("\nProduk Terlaris")
print(produk_terlaris)
