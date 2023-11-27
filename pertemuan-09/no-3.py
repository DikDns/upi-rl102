def total_dan_rata_rata(bilangan):
    jumlah = 0

    # ini untuk total
    for angka in bilangan:
        jumlah = jumlah + int(angka)

    # ini untuk rata_rata
    rata_rata = jumlah / len(bilangan)

    return {"jumlah": jumlah, "rata_rata": rata_rata}


def split_string(list_char, sep):
    hasil = []
    segment = ""

    for char in list_char:
        if char != sep:
            segment += char
        else:
            hasil.append(segment)
            segment = ""

    hasil.append(segment)
    return hasil


bilangan = split_string(input("Input: "), ",")

hasil = total_dan_rata_rata(bilangan)

sep = " + "

print("Total:", sep.join(bilangan), "=", hasil["jumlah"])
print(
    f'Rata-rata = {hasil["jumlah"]} / {len(bilangan)} = {hasil["rata_rata"]}')
