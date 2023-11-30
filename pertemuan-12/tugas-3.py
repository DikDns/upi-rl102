"""
    Nama  : Andika Eka Kurnia
    NIM   : 2306033
    Kelas : 1A - RPL
"""

from time import perf_counter
import numpy as np
import dnsearch as dns

array = np.array([1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57,
                  58, 59, 60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100])


time_start = perf_counter()
dns.linear_search(array, 60)
time_end = perf_counter()
waktu_eksekusi = (time_end - time_start) * 1000

print(
    f"Waktu eksekusi kode linear search: {((time_end - time_start) * 1000):.5f} ms")


time_start = perf_counter()
dns.binary_search(array, 60)
time_end = perf_counter()
waktu_eksekusi = (time_end - time_start) * 1000

print(
    f"Waktu eksekusi kode binary search: {((time_end - time_start) * 1000):.5f} ms")
