"""
    Nama  : Andika Eka Kurnia
    NIM   : 2306033
    Kelas : 1A - RPL
"""


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def interval_search(arr, key):
    for i in range(0, len(arr), 2):
        if arr[i] <= key <= arr[i+1]:
            return i
    return -1
