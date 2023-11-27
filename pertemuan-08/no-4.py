nim = int(input("Input 3 digit NIM terakhir : "))

if nim % 2 == 0:
    if nim >= 1 and nim <= 50: 
        print("Silakan masuk ke kelas K2")
    elif nim >= 51 and nim <= 100:
        print("Silakan masuk ke kelas K4")
    elif nim >= 101 and nim <= 150:
        print("Silakan masuk ke kelas K6")
    elif nim >= 151:
        print("Silakan masuk ke kelas K8")
else:
    if nim >= 1 and nim <= 50: 
        print("Silakan masuk ke kelas K1")
    elif nim >= 51 and nim <= 100:
        print("Silakan masuk ke kelas K3")
    elif nim >= 101 and nim <= 150:
        print("Silakan masuk ke kelas K5")
    elif nim >= 151:
        print("Silakan masuk ke kelas K7")



