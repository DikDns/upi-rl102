
n = int(input("n = "))
for i in range(0, n):
    print(f"\nAnak ayam turunlah {n - i}")
    
    if i + 1 == n:
        print("Mati satu tinggal induknya")
        break

    print(f"Mati satu tinggallah {n - i - 1}")
