print("Silakan login\n")

batas = 3
while batas > 0:
    username = input("Username : ")
    password = input("Password : ")
    
    if username == "utsdaspro" and password == "rpl2023":
        break
    
    batas -= 1
    if batas > 0:
        print(f"\nLogin Salah! Kesempatan Anda {batas}x kali lagi.\n")
    else:
        print("\nAnda tidak diperkenankan mengakses aplikasi ini.\n")