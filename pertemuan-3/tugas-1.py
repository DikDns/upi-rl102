

buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga", ]

# output: ceri durian apel
print(buah[2:5])
# Hapus apel
buah.pop(-2)
# Rename ceri
buah[2] = "cherry"
# Tambah strawberry di index ke-3
buah.insert(3, "strawberry")
# sort
buah.sort()

print(buah)
