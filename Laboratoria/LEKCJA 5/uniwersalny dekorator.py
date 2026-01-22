import functools

def uniwersalny_dekorator(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args, **kwargs):
        print('Przed:  ')

        wynik = funkcja(*args, **kwargs)

        print('Po :  ')

        return wynik
    return wrapper


@uniwersalny_dekorator
def dodaj(a,b):
    return a + b

rezultat = dodaj(1,2)
print(rezultat)

print(f'Nazwa Funkcji {dodaj.__name__}')
print(f'Docstring Funkcji {dodaj.__doc__}')