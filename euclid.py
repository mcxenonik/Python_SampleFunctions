"""
Napisz funkcję zwracającą największy wspólny dzielnik dwóch
liczb całkowitych M i N obliczony za pomocą algorytmu Euklidesa.
"""

def euclid(first_number, second_number):
    rest = first_number % second_number
    first_number = second_number
    second_number = rest

    if (second_number == 0):
        return first_number
    else:
        return euclid(first_number, second_number)


if __name__ == "__main__":
  print(euclid(3180, 3763))
