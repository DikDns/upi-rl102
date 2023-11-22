"""
    Nama  : Andika Eka Kurnia
    NIM   : 2306033
    Kelas : 1A - RPL
"""

import numpy as np


def random_array(low: int, high: int, size: int):
    rng = np.random.default_rng()
    return rng.integers(low=low, high=high, size=size)


def Celcius_to_Fahrenheit(celcius):
    return 9/5 * celcius + 32


suhu_singapura = random_array(-100, 100, 10)

print("Celcius: ", suhu_singapura)
print("Fahrenheit: ", Celcius_to_Fahrenheit(suhu_singapura))
