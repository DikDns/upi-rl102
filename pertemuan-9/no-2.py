def luas_lingkaran(r):
    return 3.14 * r ** 2


def volume_tabung(a, t):
    return a * t


r = int(input("r: "))
t = int(input("t: "))

print("V Tabung: ", volume_tabung(luas_lingkaran(r), t))
