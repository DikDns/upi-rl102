def bubble_sort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def selection_sort(data):
    for i in range(len(data) - 1, 0, -1):
        pos_max = 0
        for j in range(1, i + 1):
            if data[j] > data[pos_max]:
                pos_max = j
        data[i], data[pos_max] = data[pos_max], data[i]


def heap_sort(arr):
    def max_heap(arr, n, i):
        index_parent = i
        index_kiri = 2 * i + 1
        index_kanan = 2 * i + 2

        if index_kiri < n and arr[index_parent] < arr[index_kiri]:
            index_parent = index_kiri

        if index_kanan < n and arr[index_parent] < arr[index_kanan]:
            index_parent = index_kanan

        if index_parent != i:
            arr[i], arr[index_parent] = arr[index_parent], arr[i]
            max_heap(arr, n, index_parent)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heap(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heap(arr, i, 0)
