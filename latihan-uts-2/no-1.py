kode = ""
batas = 3

while batas > 0:
    kode = input("Kode: ")
    
    if kode == "adm123":
        print("\nSelamat datang di aplikasi Achmad Pay.")
        break
    else:
        batas -= 1
        if batas > 0:
            print(f"Salah! (sisa {batas}x kesempatan)")
        else:
            print("Anda tidak dapat mengakses aplikasi ini.")