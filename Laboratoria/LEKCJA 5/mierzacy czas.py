import functools
import time


def mierz_czas(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        czas_trwania = koniec - start
        print(f' Funkcja {funkcja.__name__} wykonala sie w {czas_trwania} sek')
        return wynik
    return wrapper


@mierz_czas
def dlugie_obliczenia(a,b):
    time.sleep(1)
    return a + b


@mierz_czas
def przywitaj(imie):
    print(f'Witaj, {imie}')

print ('Test 1')
