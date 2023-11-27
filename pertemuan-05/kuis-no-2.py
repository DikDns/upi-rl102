"""
    Kuis No 2
"""

panjang_dalam_m = 80
lebar_dalam_cm = 3200

panjang_dalam_km = panjang_dalam_m / 1000
lebar_dalam_km = lebar_dalam_cm / 100000

keliling_persegi_dalam_km = 2 * (panjang_dalam_km + lebar_dalam_km)

berlari_5x_putaran = 5 * keliling_persegi_dalam_km

pemanasan_2x_putaran = 2 * keliling_persegi_dalam_km
pendinginan_2x_putaran = 2 * keliling_persegi_dalam_km

total_jarak_dalam_km = (
    berlari_5x_putaran + pemanasan_2x_putaran + pendinginan_2x_putaran
)

print(total_jarak_dalam_km, "km")
