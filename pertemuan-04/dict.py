"""
Dictionary adalah struktur data yang berisi pasangan key-value.
Bersifat mutable, ordered, indexed dan tidak ada duplikasi.
"""

kucing = {
    "nama": "Kuro",
    "ras": "Anggora",
    "umur": 2,
    "berat_dalam_kg": 3.5,
    "warna": ["oren", "hitam", "putih"],
    "masih_hidup": True,
}

print(kucing)

buah = dict(nama="Apel", warna="Merah", berat=250, buruk=False)
print(buah)

print(kucing["nama"])
print(buah.get("warna"))

print(kucing.keys())
print(buah.values())

# menghapus item
buah.pop("buruk")

# menambah item
buah.update({"rasa": "Manis"})
kucing["makanan"] = "Whiskas"

print(kucing)
print(buah)
