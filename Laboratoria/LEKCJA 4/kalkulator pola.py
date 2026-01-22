import math


def oblicz_pole(figura, a, b, r):
    '''
    Oblicza pole podanej figury

    argument figura bierze figure od uzytkownika,
    argument a bok a, arg b bok b, arg r promien
    funckja zwraca wynik w zaleznosci od uzytej ekspresji matematycznej
    '''
    if figura == 'prostokat':
        wynik = a * b
    elif figura =='kolo':
        wynik = math.pi * pow(r, 2)
    else:
        return None

    return wynik

help(oblicz_pole)

figura = input('Podaj figurę: ').lower()
a = int(input('Podaj parametr a: '))
b = int(input('Podaj parametr b: '))
r = int(input('Podaj parametr r: '))

obliczone = oblicz_pole(figura, a, b, r)

print(obliczone)
