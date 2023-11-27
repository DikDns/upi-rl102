"""
    Kuis No 5
"""

panjang_dalam_m = 8
lebar_dalam_m = 10
tinggi_dalam_m = 4

biaya_per_meter_persegi = 520000

luas_permukaan_dinding = 2 * (panjang_dalam_m * tinggi_dalam_m) + 2 * (
    lebar_dalam_m * tinggi_dalam_m
)

biaya_dinding = luas_permukaan_dinding * biaya_per_meter_persegi

print(f"Total biaya: Rp{biaya_dinding}")
