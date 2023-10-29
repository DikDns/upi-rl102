
list_awal = input("Masukkan list awal: ").replace(" ", "").split(",")
list_filter = input("Masukkan list filter: ").replace(" ", "").split(",")

list_hasil = list_awal.copy()
for item_awal in list_awal:
    for item_filter in list_filter:
        if item_awal == item_filter:
            list_hasil.remove(item_filter)

print("Sisa:", list_hasil)
