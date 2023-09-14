

print("[]=====| Program Print Segitiga |=====[]\n")

n = int(input("Masukkan jumlah n: "))


if (n < 1):
    print("<1")
elif (n > 1):
    print(">1")
else:
    print("1")


i = 0
while i <= n:

    j = 0
    while j <= i:
        print("*", end="")
        j += 1

    print("")
    i += 1


i = n
while i >= 0:

    j = i
    while j >= 0:
        print("*", end="")
        j -= 1

    print("")
    i -= 1
