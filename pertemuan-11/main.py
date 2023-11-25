import dnsort as ds
from time import perf_counter
from numpy import array

bilangan_acak = array([7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46,
                       28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77])


time_start = perf_counter()
ds.heap_sort(bilangan_acak)
time_end = perf_counter()

print(f"Waktu eksekusi kode: {(time_end - time_start) * 1000:.5f} ms")
