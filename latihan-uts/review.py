"""
1. Tipe Data Dasar dan Variabel
2. Input dan Output
3. Operator
4. Tipe Data Sequence
5. Pengkondisian
6. Looping
"""

# 1. Tipe Data Dasar
# # int
print(1234, type(1234))

# # float
print(3.14, type(3.14))

# # str
print("halo", type("halo"))

# # bool
print(True, type(True))

# Variabel: Harus ada isinya
x = 1
_10ribu = 10000

# 2. Input dan Output
nama = input("masukkan nama: ")
print("Halo", nama,)

# 3. Operator

# 3.1. Aritmetika (+,-,*,/,//,**,%)
print(1 + 2 - 3 * 4 / 2)
# Pembulatan ke yang terkecil
print(1 // 2)
# Pangkat
print(2 ** 2)
# Hasil Sisa dari pembagian
print(2 % 2)

# 3.2. Perbandingan (==,!=,<,>,<=,>=)
print(3 == 3, 3 != 3)
print(1 > 2, 1 < 2)
print(1 >= 1, 2 <= 2)

# 3.3. Assignment (+=,-=,*=,/=,**=,%=,)
x = 2
x += 2
x -= 2
x *= 2
x /= 2
print(x)

# 3.4. Logical (and, or, not)
print(1 == 1 and 1 != 2)
print(1 == 1 or 1 >= 2)
print(not 1 == 1)

# 3.5. Membership (in)
bilangan1 = [1, 2, 3, 4]
print(3 in bilangan1)
print(5 in bilangan1)

# 3.6. Identity (is)
# untuk cek id pake fungsi id()
bilangan2 = [1, 2, 3, 4]
print(bilangan2 is bilangan1)
bilangan3 = bilangan1
print(bilangan3 is bilangan1)

# 4. Tipe Data Sequence

# 4.1. List
x = [1, True, "halo", ["a", 0]]
# akses list pake []
x[1] = "benar"
print(x[2])
print(x[2:4])

# untuk liat fungsi-fungsi list
# ketik nama listnya + titik, terus ctrl + spasi
print(x)
x.append(2)
x.remove("halo")
print(x)

# 4.2. Tuple
t = (1, True, "halo", ["a", 0])
# Error: x[1] = "benar"
print(t)

# 4.3. Set
s = {1, True, "halo"}
print(s)

# 4.4. Dict
kucing = {
    "nama": "kuro",
    "umur": 2,
    "isHidup": True,
    "hobi": ["makan", "tidur"]
}
print(kucing)


# 5. Pengkondisian
angka = int(input("Angka: "))
if angka == 0:
    print("angka 0")
elif angka == -100:
    print("angka -100")
else:
    print("Bukan 0 dan -100")

# 6. Looping
for item in range(angka):
    print(item)

while angka >= 0:
    print(angka)
    angka -= 1
