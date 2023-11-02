
n = int(input("Faktorial: "))
for i in range(0, n):
    if i + 1 == n:
        print(f"{n - i}! = {n - i}")
    else:
        print(f"{n - i}! = {n - i} * {n - i - 1}!")
