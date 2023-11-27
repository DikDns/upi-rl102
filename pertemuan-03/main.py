"""
  Pertemuan 3

  Data Type: List and Tuple 
"""

# List
buah = ["apel", "jeruk", "mangga", "anggur", "pisang", "semangka", "apel"]

# mengambil data
print("\n[]============| Mengambil Data |============[]")
print(buah[3])
print(buah[4:])
print(buah[:4])
print(buah[1:4])

# menambah data
print("\n[]============| Menambah Data    |============[]")
buah.append("durian")
print(buah[-1])

buah.insert(2, "nanas")
print(buah[2])

# menghapus data
print("\n[]============| Menghapus Data   |============[]")
buah.remove("apel")
buah.pop(2)
print(buah)


# mengurutkan data
print("\n[]============| Mengurutkan Data |============[]")
buah.sort()
print(buah)

# Tuple
makanan_tradisional = ("rendang", "sate", "soto", "nasi goreng", "bakso", "rendang")

# Unpacking
print("\n[]============| Unpacking Data   |============[]")
makanan1, makanan2, makanan3, *makanan_lain = makanan_tradisional

print(makanan1)
print(makanan2)
print(makanan3)
print(makanan_lain)
