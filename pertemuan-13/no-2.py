"""
    Nama    : Andika Eka Kurnia
    NIM     : 2306033
    Kelas   : 1A
"""

from algorithm import linear_search


def main():
    array = []
    n = int(input("[]=> Masukkan jumlah Array: "))

    for i in range(n):
        array.append(int(input(f"[]=> Masukkan nilai ke-{i+1}: ")))

    cari = int(input("[]=> Masukkan nilai yang ingin dicari: "))

    index = linear_search(array, cari)

    if index == -1:
        print("[]=> Maaf nilai yang dicari tidak ada di array!")
    else:
        print(f"[]=> Nilai {cari} ada di index ke-{index}")


main()
