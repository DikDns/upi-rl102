import dnsearch as dns


barang = ['kunci', 'ember', 'jaket', 'ban', 'mobil',
          'sepeda', 'motor', 'baju', 'celana', 'topi', 'jam', 'sendal', 'sepatu', 'dompet', 'jaket']

cari_barang = input('Masukkan nama barang yang ingin dicari: ')

hasil_index = dns.linear_search(barang, cari_barang)

if hasil_index != -1:
    print(cari_barang, f"ditemukan di index ke-{hasil_index}")
else:
    print(cari_barang, 'tidak ditemukan')
