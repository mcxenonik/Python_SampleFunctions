"""
Napisz funkcję, która zamieni podaną godzinę w formacie liczbowym
na format opisowy.
"""

def time_description(hour, minutes):
    str_time_dict = {
        '0':    "o'clock",
        '1':    'one',
        '2':    'two',
        '3':    'three',
        '4':    'four',
        '5':    'five',
        '6':    'six',
        '7':    'seven',
        '8':    'eight',
        '9':    'nine',
        '10':   'ten',
        '11':   'eleven',
        '12':   'twelve',
        '13':   'thirteen',
        '14':   'fourteen',
        '15':   'quarter',
        '16':   'sixteen',
        '17':   'seventeen',
        '18':   'eighteen',
        '19':   'nineteen',
        '20':   'twenty',
        '21':   'twenty one',
        '22':   'twenty two',
        '23':   'twenty three',
        '24':   'twenty four',
        '25':   'twenty five',
        '26':   'twenty six',
        '27':   'twenty seven',
        '28':   'twenty eight',
        '29':   'twenty nine',
        '30':   'half'
    }

    t = 'past'

    if(minutes > 30):
        minutes = 60 - minutes
        t = 'to'
        hour += 1

    m = str_time_dict[str(minutes)]
    h = str_time_dict[str(hour)]

    if(minutes == 0):
        return f'{h} o\'clock'

    return f'{m} minutes {t} {h}'


if __name__ == "__main__":
    print(time_description(11, 15))
    