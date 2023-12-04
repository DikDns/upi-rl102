"""
    Nama    : Andika Eka Kurnia
    NIM     : 2306033
    Kelas   : 1A
"""

from algorithm import heap_sort


def main():
    array = []
    n = int(input("[]=> Masukkan jumlah Array: "))

    for i in range(n):
        array.append(int(input(f"[]=> Masukkan nilai ke-{i+1}: ")))

    heap_sort(array)

    print("[]=> Array setelah diurutkan:", array)


main()
