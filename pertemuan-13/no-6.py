"""
    Nama    : Andika Eka Kurnia
    NIM     : 2306033
    Kelas   : 1A
"""


def main():
    ranking_siswa = []

    n = int(input("[]=> Masukkan jumlah siswa: "))

    for i in range(n):
        nama = input(f"[]=> Masukkan nama siswa ke-{i+1}: ")
        nilai = int(input(f"[]=> Masukkan nilai siswa ke-{i+1}: "))
        ranking_siswa.append({"nama": nama, "nilai": nilai})

    print(ranking_siswa)
    sort_ranking_siswa(ranking_siswa)
    print(ranking_siswa)

    cari = input("[]=> Masukkan nama siswa yang ingin dicari: ")

    index_hasil = cari_siswa(ranking_siswa, cari)

    if index_hasil == -1:
        print("[]=> Siswa tidak ditemukan")
    elif index_hasil < 3:
        print("[]=| Nama    :", ranking_siswa[index_hasil]["nama"])
        print("[]=| Ranking :", index_hasil+1)
    else:
        print("[]=| Nama    :", ranking_siswa[index_hasil]["nama"])
        print("[]=| Siswa masih harus belajar dengan giat!")


def cari_siswa(ranking_siswa, cari):
    for i in range(len(ranking_siswa)):
        if ranking_siswa[i]["nama"] == cari:
            return i
    return -1


def sort_ranking_siswa(ranking_siswa):
    for i in range(len(ranking_siswa)):
        for j in range(len(ranking_siswa)-1):
            if ranking_siswa[j]["nilai"] < ranking_siswa[j+1]["nilai"]:
                ranking_siswa[j], ranking_siswa[j +
                                                1] = ranking_siswa[j+1], ranking_siswa[j]


main()
