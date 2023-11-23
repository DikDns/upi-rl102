"""
    Nama  : Andika Eka Kurnia
    NIM   : 2306033
    Kelas : 1A - RPL
"""

import numpy as np


def random_array(low: int, high: int, size: int):
    rng = np.random.default_rng()
    return rng.integers(low=low, high=high, size=size)


nilai_mentah = random_array(0, 100, 30)
nilai_mentah.sort()
nilai_sorted = nilai_mentah[::-1]

print(nilai_sorted)
print(nilai_sorted[:5])
