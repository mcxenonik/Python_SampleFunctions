"""
Napisz funkcję przyjmującą jako parametr liczbę N, która wygeneruje
listę liczb od 1 do N, gdzie wszystkie liczby podzielne przez 3 zostaną
zastąpione słowem fuzz. Uwaga: w rozwiązaniu nie używaj pętli.
"""


def fuzz(n):
    my_list = list(range(1, n + 1))
    fuzz_list = ['fuzz'] * (n // 3)
    my_list[2::3] = fuzz_list

    return my_list


print(fuzz(10))
