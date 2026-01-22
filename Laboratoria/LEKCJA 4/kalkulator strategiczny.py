def dodaj(a,b):
    wynikd = a + b
    return wynikd

def odejmij(a,b):
    wyniko = a - b
    return wyniko

a = int(input('Podaj liczbe a:  '))
b = int(input('Podaj liczbe b:  '))
funkcja = input('Podaj operacje:  ').lower()

def wykonaj_operacje(a,b,funkcja):
    if funkcja == 'dodawanie':
        wynik_dodawania = dodaj(a, b)
        return wynik_dodawania
    elif funkcja == 'odejmij':
        wynik_odejmija = odejmij(a, b)
        return wynik_odejmija
    else:
        return None

print(wykonaj_operacje(a,b,funkcja))