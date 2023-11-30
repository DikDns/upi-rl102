import dnsearch as dns


nama_mahasiswa = ['Katon', 'Rudi', 'Joko', 'Rina', 'Rudi', 'Andika', 'Rita', "Achmad",
                  "Nashirul", "Fatra", "Risti", "Rifiani", "Bagas", "Asep", "Rizal", "Dicky", "Rafi", "Zamzami", "Shandy", "Salsabila"]

cari_mahasiswa = input('Masukkan nama: ')

hasil_index = dns.linear_search(nama_mahasiswa, cari_mahasiswa)

if hasil_index != -1:
    print(cari_mahasiswa, f"ditemukan di index ke-{hasil_index}")
else:
    print(cari_mahasiswa, 'tidak ditemukan')
