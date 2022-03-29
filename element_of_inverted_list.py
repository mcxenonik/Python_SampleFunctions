"""
Napisz funkcję, która dla zadanej listy elementów pobierze od użytkownika
liczbę k i zwróci k-ty element od końca listy. Uwaga: załóż, że użytkownik
będzie proszony o podanie liczby k dopóty, dopóki wprowadzona wartość nie 
będzie poprawna.
"""

def get_element_of_inverted_list(my_list):
    max_index = len(my_list)
    input_text = f'Enter index of element (1 - {max_index}): '
    index = input(input_text)

    while not(index.isdigit() and int(index) >= 1 and int(index) <= max_index):
        print('Wrong index of element')
        index = input(input_text)
    else:
        return my_list[-int(index)]


if __name__ == "__main__":
    my_list = list(range(1, 11))
    print(get_element_of_inverted_list(my_list))
