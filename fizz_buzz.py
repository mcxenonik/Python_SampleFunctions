"""
Napisz funkcję iterującą po liczbach całkowitych od 1 do n
i wypisującą je na ekran. Dla liczb podzielnych przez 3 zamiast
liczby wypisz “fizz”, dla liczb podzielnych przez 5 wypisz “buzz”,
natomiast zamiast liczb podzielnych przez 3 i 5 wypisz “fizzbuzz”.
"""


def fizz_buzz(n):
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("fizzbuzz")
        elif (i % 3 == 0):
            print("fizz")
        elif (i % 5 == 0):
            print("buzz")
        else:
            print(i)


fizz_buzz(100)
