

buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga", )

# List ke-2 sampai ke-5
print(buah[2:5])

temp = list(buah)
# Hapus durian
temp.remove("durian")
# Tambah manggis di antara jeruk dan ceri
temp.insert(2, "manggis")

buah = tuple(temp)

print(buah)
