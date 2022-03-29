"""
Napisz funkcję, która jako parametr przyjmuje wyraz i tworzy słownik,
gdzie kluczami są litery, zaś wartościami liczba ich wystąpień w danym
słowie. Przykład: dla słowa "kukułka" funkcja powinna zwrócić:
{'k': 3, 'u': 2, 'ł': 1, 'a': 1}
"""

def word_to_dict(word):
    my_dict = {}
    for character in word:
        if character in my_dict:
            my_dict[character] += 1
        else:
            my_dict[character] = 1

    return my_dict


if __name__ == "__main__":
    print(word_to_dict('kukulka'))
