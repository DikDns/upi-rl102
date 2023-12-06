"""
    Nama    : Andika Eka Kurnia
    NIM     : 2306033
    Kelas   : 1A
"""

from algorithm import linear_search


def main():
    menu = ["Ayam Gulai", "Babat", "Cumi", "Ikan Kembung", "Kikil",
            "Limpa", "Otak", "Paru", "Rendang", "Telur", "Usus"]

    cari = input("[]=> Masukkan menu yang ingin dicari: ")

    index = linear_search(menu, cari)

    if index == -1:
        print("[]=> Maaf menu yang dicari tidak tersedia!")
    else:
        print(f"[]=> Menu {cari} tersedia!")


main()
