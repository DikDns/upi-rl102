"""
    Nama  : Andika Eka Kurnia
    NIM   : 2306033
    Kelas : 1A
"""
import tpcsv
import os

data_path = "inventaris_barang.csv"

def main():
    while True:
        clear_terminal()
        
        print("[]==================================================[]")
        print("[]===|", f"{'Program Inventaris Barang':^40}", "|===[]")
        print("[]--------------------------------------------------[]")
        print("[]===|", f"{'1. Lihat Semua Barang':<40}", "|===[]")
        print("[]===|", f"{'2. Tambah Barang':<40}", "|===[]")
        print("[]===|", f"{'3. Hapus Barang':<40}", "|===[]")
        print("[]===|", f"{'4. Ubah Jumlah Barang':<40}", "|===[]")
        print("[]===|", f"{'5. Cari Barang':<40}", "|===[]")
        print("[]===|", f"{'6. Lihat Jumlah Semua Barang':<40}", "|===[]")
        print("[]===|", f"{'7. Keluar':<40}", "|===[]")
        print("[]==================================================[]")

        pilihan = input("[]=| Masukkan pilihan: ")
        if pilihan == "1":
            lihat_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            hapus_barang()
        elif pilihan == "4":
            ubah_jumlah_barang()
        elif pilihan == "5":
            lihat_barang()
        elif pilihan == "6":
            jumlah_semua_barang()
        elif pilihan == "7":
            clear_terminal()
            break
        else:
            alert("Pilihan tidak tersedia!")


def lihat_barang():
    clear_terminal()

    data = tpcsv.get(data_path)

    print_barang(data)
    alert("")


def print_barang(data: list):
    if len(data) == 0:
        alert("Data kosong!")
        return
    
    list_header_baris = list(data[0].keys())

    print("-"*62)
    print(f'[]===| {list_header_baris[0]:4} | ', end='')
    print(f'{list_header_baris[1]:^32} | ', end='')
    print(f'{list_header_baris[2]:4} |===[]')
    print("-"*62)

    for baris in data:
        print(f'[]===| {baris["id"]:<4} | ', end='')
        print(f'{baris["nama_barang"]:32} | ', end='')
        print(f'{baris["jumlah"]:<6} |===[]')
    print("-"*62)


def tambah_barang():
    data = tpcsv.get(data_path)
    
    barang_baru = {
        "id": None,
        "nama_barang": None,
        "jumlah": None
    }

    if len(data) == 0:
        barang_baru["id"] = 1
    else:
        barang_baru["id"] = int(data[-1]["id"]) + 1

    while True:
        clear_terminal()
        print_barang(data)

        barang_baru["nama_barang"] = input_nama_barang()
        
        if barang_baru["nama_barang"] is False:
            continue

        barang_baru["jumlah"] = input_jumlah_barang()

        if barang_baru["jumlah"] is False:
            continue
        
        clear_terminal()
        print_barang([barang_baru])
        pilihan = input("[]=| Apakah data sudah benar? (y/n): ")

        if pilihan == "y": 
            data.append(barang_baru)

            tpcsv.put(data_path, data)

            alert("Barang berhasil ditambahkan!")
            return

        if pilihan == "n":   
            alert("Data dibatalkan!")
            return
        
def hapus_barang():
    data = tpcsv.get(data_path)
    while True:
        clear_terminal()
        print_barang(data)

        search = input("[]=| Masukkan nama atau id barang: ")

        index = search_barang(data, search)

        if index is None:
            alert("Barang tidak ditemukan!")
            continue

        clear_terminal()
        print_barang([data[index]])
        pilihan = input("[]=| Apakah yakin ingin menghapus data? (y/n): ")

        if pilihan == "y":
            data.pop(index)
            tpcsv.put(data_path, data)
            alert("Barang berhasil dihapus!")
            return

        if pilihan == "n":
            alert("Data tidak ada yang dihapus!")
            return

def ubah_jumlah_barang():
    data = tpcsv.get(data_path)
    while True:
        clear_terminal()
        print_barang(data)

        search = input("[]=| Masukkan nama atau id barang: ")

        index = search_barang(data, search)

        if index is None:
            alert("Barang tidak ditemukan!")
            continue

        clear_terminal()
        print_barang([data[index]])

        jumlah_barang = input_jumlah_barang()

        if jumlah_barang is False:
            continue

        if jumlah_barang == 0:
            data.pop(index)
            tpcsv.put(data_path, data)
            alert("Barang berhasil dihapus!")
            return

        data[index]["jumlah"] = jumlah_barang
        tpcsv.put(data_path, data)
        alert("Jumlah barang berhasil diubah!")
        return

def lihat_barang():
    data = tpcsv.get(data_path)
    while True:
        clear_terminal()
        print_barang(data)

        search = input("[]=| Masukkan nama atau id barang: ")

        index = search_barang(data, search)

        if index is None:
            alert("Barang tidak ditemukan!")
            continue

        clear_terminal()
        print_barang([data[index]])
        alert("")
        return

def jumlah_semua_barang():
    data = tpcsv.get(data_path)

    clear_terminal()

    jumlah = 0

    for barang in data:
        jumlah += barang["jumlah"]

    print(f"[]===| Jumlah semua barang: {jumlah}")
    alert("")

def input_nama_barang():
    nama_barang = input("[]=| Masukkan nama barang: ")
    
    if len(nama_barang) == 0:
        alert("Nama barang tidak boleh kosong!")
        return False

    if len(nama_barang) >= 32:
        alert("Nama barang terlalu panjang!")
        return False

    return nama_barang

def input_jumlah_barang():
    try:
        jumlah = int(input("[]=| Masukkan jumlah barang: "))
    except ValueError:
        alert("Jumlah barang harus berupa angka!")
        return False

    if jumlah < 0:
        alert("Jumlah barang tidak boleh negatif!")
        return False

    return jumlah

def search_barang(data: list, search: str):
    for index, barang in enumerate(data):
        if search.isnumeric() and barang["id"] == int(search):
            return index
        
        if barang["nama_barang"] == search:
            return index
        
    return None

def alert(msg: str = ""):
    if msg != "":
        print("[]===>", msg)
    input("[]=| Tekan enter untuk melanjutkan...")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

main()

