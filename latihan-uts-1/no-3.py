
list_kata = input("Kalimat: ").split(" ")
batas_huruf = int(input("Batas huruf: "))

list_kata_melebihi_batas = []
for kata in list_kata:
    if len(kata) > batas_huruf:
        list_kata_melebihi_batas.append(kata)

print(list_kata_melebihi_batas)
