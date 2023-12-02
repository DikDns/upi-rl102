"""
    Nama    : Andika Eka Kurnia
    NIM     : 2306033
    Kelas   : 1A
"""

import os

perpustakaan = [
    {
        "judul": "Pemrograman Python",
        "nama_penulis": "Andika Eka Kurnia",
        "kode_buku": "PYT001",
        "status_buku": "Tersedia"
    },
    {
        "judul": "Pemrograman C++",
        "nama_penulis": "Andika Eka Kurnia",
        "kode_buku": "CPP001",
        "status_buku": "Dipinjam"
    }
]


def main():
    while True:
        clear_screen()

        print("[]=> Perpustakaan UPI Kampus Cibiru")
        print("[]=| 1. Tambah Buku")
        print("[]=| 2. Pinjam Buku")
        print("[]=| 3. Kembalikan Buku")
        print("[]=| 4. Lihat Buku Tersedia")
        print("[]=| 5. Lihat Buku Dipinjam")
        print("[]=| 6. Keluar")
        pilihan = input("[]=> Masukkan pilihan: ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            pinjam_buku()
        elif pilihan == "3":
            kembalikan_buku()
        elif pilihan == "4":
            lihat_buku()
        elif pilihan == "5":
            lihat_buku("Dipinjam")
        elif pilihan == "6":
            break


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_detail_buku(buku):
    print(f"[]=| Judul   : {buku['judul']}")
    print(f"[]=| Penulis : {buku['nama_penulis']}")
    print(f"[]=| Kode    : {buku['kode_buku']}")
    print(f"[]=| Status  : {buku['status_buku']}")


def cari_buku(kode_buku):
    for i in range(len(perpustakaan)):
        if perpustakaan[i]["kode_buku"] == kode_buku:
            return i
    return -1


def tambah_buku():
    clear_screen()

    buku = {
        "judul": None,
        "nama_penulis": None,
        "kode_buku": None,
        "status_buku": "Tersedia"
    }
    yakin = False

    while not yakin:
        buku["judul"] = input("[]=> Masukkan judul buku: ")
        buku["nama_penulis"] = input("[]=> Masukkan nama penulis: ")
        buku["kode_buku"] = input("[]=> Masukkan kode buku: ").upper()
        yakin = input("[]=> Apakah data sudah benar? (y/n) ").lower() == "y"

    perpustakaan.append(buku)
    print_detail_buku(buku)
    print("[]=> Buku berhasil ditambahkan!")
    input("[]=> Tekan enter untuk kembali...")


def pinjam_buku():
    clear_screen()

    kode_buku = input("[]=> Masukkan kode buku yang ingin dipinjam: ").upper()
    indeks_buku = cari_buku(kode_buku)

    if indeks_buku == -1:
        return print("[]=> Buku tidak ditemukan!")

    if perpustakaan[indeks_buku]["status_buku"] == "Dipinjam":
        return print("[]=> Buku sedang dipinjam!")

    perpustakaan[indeks_buku]["status_buku"] = "Dipinjam"

    print_detail_buku(perpustakaan[indeks_buku])
    print("[]=> Buku berhasil dipinjam!")
    input("[]=> Tekan enter untuk kembali...")


def kembalikan_buku():
    clear_screen()

    kode_buku = input(
        "[]=> Masukkan kode buku yang ingin dikembalikan: ").upper()
    indeks_buku = cari_buku(kode_buku)

    if indeks_buku == -1:
        return print("[]=> Buku tidak ditemukan!")

    if perpustakaan[indeks_buku]["status_buku"] == "Tersedia":
        return print("[]=> Buku tidak sedang dipinjam!")

    perpustakaan[indeks_buku]["status_buku"] = "Tersedia"

    print_detail_buku(perpustakaan[indeks_buku])
    print("[]=> Buku berhasil dikembalikan!")
    input("[]=> Tekan enter untuk kembali...")


def lihat_buku(status="Tersedia"):
    clear_screen()

    for buku in perpustakaan:
        if buku["status_buku"] == status:
            print_detail_buku(buku)
            print("[]=> ---------------------------")

    input("[]=> Tekan enter untuk kembali...")


main()
