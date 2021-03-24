"""
Napisz funkcję zwracającą największy wspólny dzielnik dwóch
liczb całkowitych M i N obliczony za pomocą algorytmu Euklidesa:
- Oblicz resztę R z dzielenia M przez N.
- Zastąp M liczbą N, a następnie N liczbą R.
- Jeśli N wynosi zero, to M jest szukaną wartością największego
  wspólnego dzielnika. W przeciwnym wypadku przejdź do pierwszego
  kroku algorytmu.
Możesz założyć poprawność danych wejściowych.
"""


def euclid(first_number, second_number):
    rest = first_number % second_number
    first_number = second_number
    second_number = rest

    if (second_number == 0):
        return first_number
    else:
        return euclid(first_number, second_number)


print(euclid(3180, 3763))
