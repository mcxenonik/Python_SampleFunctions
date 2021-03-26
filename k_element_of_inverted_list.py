"""
Napisz funkcję, która dla zadanej listy elementów pobierze od użytkownika
liczbę k i zwróci k-ty element od końca listy. Uwaga: załóż, że użytkownik
podaje poprawne wartości (tzn. 0 < k <= długość listy).

Przyjęcie, że użytkownik wprowadza poprawne dane, jest w realnej pracy
programisty zdecydowanie zbyt daleko idącym założeniem. Rozbuduj funkcję
z poprzedniego zadania tak, aby sprawdzała, czy liczba k podana przez
użytkownika mieści się we właściwym przedziale i w razie błędu wypisz
na ekran stosowny komunikat. Pamiętaj o obsłużeniu sytuacji, w której
wartość podana przez użytkownika w ogóle nie jest liczbą całkowitą.

Zmień funkcję z poprzedniego zadania w ten sposób, aby użytkownik był
proszony o podanie liczby k dopóty, dopóki wprowadzona wartość nie będzie
poprawna.
"""


def get_k_element_of_inverted_list(my_list):
    max_index = len(my_list)
    input_text = f'Enter index of element (1 - {max_index}): '
    index = input(input_text)

    while not(index.isdigit() and int(index) >= 1 and int(index) <= max_index):
        print('Wrong index of element')
        index = input(input_text)
    else:
        return my_list[-int(index)]


my_list = list(range(1, 11))
print(get_k_element_of_inverted_list(my_list))
