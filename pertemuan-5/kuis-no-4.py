"""
    Kuis No 4
"""

daftar_barang_bulan_juli = {
    "baju": ["T-Shirt", "Blouse", "Kemeja", "Baju Renang"],
    "celana": ["Celana Panjang", "Rok"],
    "lainnya": ["Tas", "Topi", "Sepatu", "Sendal"],
}

daftar_barang_bulan_agustus = {
    "baju": ["T-Shirt", "Blouse", "Kemeja", "Baju Renang"],
    "celana": ["Celana Panjang", "Rok"],
    "lainnya": ["Tas", "Topi", "Sepatu", "Sendal"],
}

daftar_barang_bulan_agustus["baju"][3] = "Gamis"
daftar_barang_bulan_agustus["lainnya"].append("Ikat Rambut")
daftar_barang_bulan_agustus["lainnya"].append("Kerudung")

print(
    "Jumlah Jenis Barang Jualan Bulan Juli: ",
    len(daftar_barang_bulan_juli) - 1 + len(daftar_barang_bulan_juli["lainnya"]),
)
print("Daftar Barang Jualan Bulan Juli: ", daftar_barang_bulan_juli)

print(
    "Jumlah Jenis Barang Jualan Bulan Agustus: ",
    len(daftar_barang_bulan_agustus) - 1 + len(daftar_barang_bulan_agustus["lainnya"]),
)
print("Daftar Barang Jualan Bulan Agustus: ", daftar_barang_bulan_agustus)
