

buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga", ]

# List ke-2 sampai ke-5
print(buah[1:5])
# Hapus apel
buah.pop(-2)
# Rename ceri
buah[2] = "cherry"
# Tambah strawberry di index ke-3
buah.insert(3, "strawberry")
# sort
buah.sort()

print(buah)
