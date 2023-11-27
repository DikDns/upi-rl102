"""
    Kuis No 6
"""

mobil_lama = {
    "merk": "Honda",
    "tipe": "HRV",
    "tahun": "2018",
    "warna": "Hitam",
    "no_polisi": "D 1234 ABC",
    "bensin": "Pertalite",
    "transmisi": "Manual",
}

print("Mobil lama Pak Oki adalah: ")
print("Merk:", mobil_lama["merk"])
print("Tipe:", mobil_lama["tipe"])
print("Warna:", mobil_lama["warna"])
print("Tahun:", mobil_lama["tahun"])


mobil_sekarang = mobil_lama.copy()

print("\nMasukkan informasi detail mobil baru")
mobil_sekarang["merk"] = input("Merk: ")
mobil_sekarang["tipe"] = input("Tipe mobil: ")
mobil_sekarang["tahun"] = input("Tahun keluaran: ")
mobil_sekarang["warna"] = input("Warna: ")
mobil_sekarang["no_polisi"] = input("No. polisi: ")
mobil_sekarang["bensin"] = input("Bensin: ")
mobil_sekarang["transmisi"] = input("Transmisi: ")

print(f"\n{'-'*12}***{'-'*12}")
print("Mobil baru Pak Oki adalah: ")
print("Merk:", mobil_sekarang["merk"])
print("Tipe:", mobil_sekarang["tipe"])
print("Warna:", mobil_sekarang["warna"])
print("Tahun:", mobil_sekarang["tahun"])
print(f"{'-'*12}***{'-'*12}")
