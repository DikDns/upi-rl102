import os
import andika
from andika import kucing

# Membuka dan Membaca File

file = open("./data/admin.txt", "r")
print(file.read())
file.close()

file = open("./data/admin.txt", "r")
print(file.read(10))
file.close()

with open("./data/admin.txt", "r") as file:
    print(file.read())

file = open("./data/admin.txt", "r")
print(file.readline())
file.close()

with open("./data/admin.txt", "r") as file:
    for line in file:
        print(line)

# Menulis File

with open("./data/hello.txt", "w") as file:
    file.write("Hello File!")

with open("./data/hello.txt", "w") as file:
    file.write("Halo (dalam bahasa Indonesia) File!")

with open("./data/hello.txt", "r") as file:
    print(file.read())

with open("./data/hello.txt", "a") as file:
    file.write("Hello File! v2")

with open("./data/hello.txt", "r") as file:
    print(file.read())

# Menulis File (File tidak ada)

with open("./data/append.txt", "a") as file:
    file.write("Append!")

with open("./data/append.txt", "r") as file:
    print(file.read())

# Menulis menggunakan List

with open("./data/hello.txt", "w") as file:
    lines = ["Hello\n", "World\n", "from\n", "Python\n"]
    file.writelines(lines)

with open("./data/hello.txt", "r") as file:
    print(file.read())

# Mengecek keberadaan File

is_exist = os.path.exists("./data/hello.txt")

if is_exist:
    print("File ada")
else:
    print("File tidak ada")


is_file = os.path.isfile("./data/hello.txt")

if is_file:
    print("ini adalah file")
else:
    print("ini bukan file atau file tidak ada")

# File dan List
file_path = "./data/file_list.txt"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    list_data = []
    for line in lines:
        list_data.append(line.strip().split())

    for item in list_data:
        print(item)
else:
    print(f"Maaf file untuk {file_path} tidak ditemukan")


list_buah = ["mangga", "strawberry", "pisang", "anggur",
             "salak", "apel", "jeruk", "semangka", "durian"]

with open("./data/list_to_file.txt", "w") as file:
    file.write(" ".join(list_buah))


# Import Module
andika.sapa("Asep")
peliharaan = andika.kucing["nama"]

print(peliharaan)

peliharaan = kucing["nama"]
print(peliharaan)
