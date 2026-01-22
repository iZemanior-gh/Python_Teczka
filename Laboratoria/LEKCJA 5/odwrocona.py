def generuj_raport(imie, stanowisko='Pracownik', miasto='Nieznane'):
    print(' \n ----------Raport Uzytkownika ---------------- \n'
          f'  Imie: {imie} \n'
          f'  Stanowisko: {stanowisko} \n'
          f'  Miasto: {miasto} \n'
          f'---------------------------------------------------')


dane_pracownika = {
    'imie' : 'Jan',
    'miasto' : 'Poznan'
}

generuj_raport(**dane_pracownika)