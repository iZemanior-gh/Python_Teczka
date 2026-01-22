def generuj_raport(**szczegoly):
    print(f'----Dynamiczny Raport------')
    if not szczegoly:
        print('Brak danych  ')
    else:
        for klucz,wartosc in szczegoly.items():
            print(f'{klucz.capitalize()}: {wartosc}')

print('---------------------')

generuj_raport(status='Aktywny', punkty='158', zalogowany=True)
generuj_raport(imie='Anna', kraj='Polska')
generuj_raport()