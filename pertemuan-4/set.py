"""
Set
Bersifat immutable, unordered, unindexed dan tidak ada duplikasi.
"""


set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set)
print(len(set))

# print(set[0]) # error
for item in set:
    print(item)

# menambahkan item
set.add(11)
print(set)

# menambahkan item dari collection lain
set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
new_list = [11, 12, 13, 14, 15]
set.update(new_list)
print(set)

set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
new_tuple = (11, 12, 13, 14, 15)
set.update(new_tuple)
print(set)

set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
new_set = {11, 12, 13, 14, 15}
set.update(new_set)
print(set)

# union method
print("\n[]============| union method |============[]")
# menggabungkan set
buah_1 = {"apel", "jeruk", "melon", "pisang"}
buah_2 = {"pisang", "semangka", "apel", "durian"}
gabungan_buah = buah_1.union(buah_2)
print(gabungan_buah)

# intersection method
print("\n[]============| intersection method |============[]")
# menyimpan item yang sama
buah_1 = {"apel", "jeruk", "melon", "pisang"}
buah_2 = {"pisang", "semangka", "apel", "durian"}
buah_sama = buah_1.intersection(buah_2)
print(buah_sama)
buah_1.intersection_update(buah_2)
print(buah_1)

# symmetric_difference method
print("\n[]============| symmetric_difference method |============[]")
# menyimpan item yang tidak sama
buah_1 = {"apel", "jeruk", "melon", "pisang"}
buah_2 = {"pisang", "semangka", "apel", "durian"}
buah_beda = buah_1.symmetric_difference(buah_2)
print(buah_beda)
buah_1.symmetric_difference_update(buah_2)
print(buah_1)
