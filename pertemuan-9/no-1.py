bilangan = []


def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


n = int(input("n: "))

for i in range(0, n + 1):
    bilangan.append(fibonacci(i))

print(bilangan)
