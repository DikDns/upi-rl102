"""
    Nama    : Andika Eka Kurnia
    NIM     : 2306033
    Kelas   : 1A
"""
import os


antrian = []
pilih_antrian = [0]


def main():
    while True:
        clear_screen()
        print(f"[]=> Antrian saat ini: {antrian}")
        print(f"[]=> Antrian yang dipilih: {pilih_antrian}")
        print("[]=> Antrian Klinik")
        print("[]=| 1. (Pasien) Ambil Antrian")
        print("[]=| 2. (Pasien) Cek Antrian")
        print("[]=| 3. (Klinik) Pilih Antrian")
        print("[]=| 4. Keluar")
        pilihan = input("[]=> Masukkan pilihan: ")

        if pilihan == "1":
            ambil_antrian()
        elif pilihan == "2":
            input_antrian()
        elif pilihan == "3":
            klinik_pilih_antrian()
        elif pilihan == "4":
            break


def ambil_antrian():
    clear_screen()

    nomor_antrian = antrian[-1] + 1 if len(antrian) > 0 else 1
    antrian.append(nomor_antrian)
    print(f"[]=> Nomor antrian Anda: {nomor_antrian}")
    input("[]=> Silahkan menunggu...")


def input_antrian():
    clear_screen()

    nomor_antrian = int(input("[]=> Masukkan nomor antrian Anda: "))

    if pilih_antrian[0] == nomor_antrian:
        return input("[]=> Silahkan masuk...")

    if pilih_antrian[0] < nomor_antrian:
        return input("[]=> Silahkan menunggu...")

    return input("[]=> Nomor antrian Anda tidak ditemukan!")


def klinik_pilih_antrian():
    clear_screen()
    pilih_antrian[0] = antrian.pop(0)
    input(f"[]=> (klinik) Antrian no. {pilih_antrian[0]} dipanggil!")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


main()
