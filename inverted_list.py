"""
Napisz funkcję, która dla zadanej listy zwróci listę zawierającą
co trzeci element, w odwróconej kolejności, zaczynając od
przedostatniego. Przykład: dla listy [1, 2, 3, 4, 5, 6, 7, 8, 9]
wynikiem będzie [8, 5, 2].
"""


def get_inverted_list(list):
    return list[-2::-3]


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_inverted_list(my_list))
