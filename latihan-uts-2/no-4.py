x = int(input("Input: "))

if x % 2 == 0:
    if x >= 2 and x <= 25:
        print("Sistem akan memberikan karakter Rare")
    elif x >= 26 and x <= 75:
        print("Sistem akan memberikan karakter Common")
    elif x >= 76 and x <= 90:
        print("Sistem akan memberikan karakter SSR")
    elif x >= 91 and x <= 100:
        print("Sistem akan memberikan karakter Mythic")
else:
    if x >= 2 and x <= 25:
        print("Sistem akan memberikan karakter SR")
    elif x >= 26 and x <= 75:
        print("Sistem akan memberikan karakter Normal")
    elif x >= 76 and x <= 90:
        print("Sistem akan memberikan karakter SSSR")
    elif x >= 91 and x <= 100:
        print("Sistem akan memberikan karakter Legendary")
