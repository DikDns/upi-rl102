def login(batas):
    input("username : ")
    password = input("password : ")

    if (batas <= 1):
        return print("Anda tidak dapat mengakses aplikasi ini.")

    if (password != "Latihan"):
        print(f"Salah! (sisa {batas - 1}x kesempatan)")
        return login(batas - 1)
    else:
        return print("\nSelamat datang di aplikasi")


batas = 3
login(3)
