"""
    Nama  : Andika Eka Kurnia
    NIM   : 2306033 
    Kelas : 1A
"""
import os


def main():
    data_nilai_siswa_path = 'nilai_siswa.txt'

    data_nilai_siswa_path = read_file(data_nilai_siswa_path)

    if data_nilai_siswa_path is None:
        print('File nilai_siswa.txt tidak ditemukan')
        return

    list_nilai_siswa = [to_int(nilai_siswa.split(':')[-1].strip())
                        for nilai_siswa in data_nilai_siswa_path]

    print("Rata-rata nilai siswa adalah", average(list_nilai_siswa))


def read_file(path: str):
    if not os.path.exists(path):
        return None

    with open(path, 'r') as file:
        return file.read().strip().split('\n')


def to_int(string: str):
    if string.isdigit():
        return int(string)
    return None


def average(list_number: list):
    total = 0
    for number in list_number:
        total += number
    return total / len(list_number)


main()
