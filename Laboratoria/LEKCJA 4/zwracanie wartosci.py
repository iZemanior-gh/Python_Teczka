def rozdzial_imie_nazwisko(iin):
    rozdzielone = iin.split()
    return rozdzielone

iin = input('Podaj imie i nazwisko:  ')

kredencjaly = rozdzial_imie_nazwisko(iin)
print(kredencjaly)