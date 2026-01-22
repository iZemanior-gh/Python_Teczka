kontakty = {}

while True:
    wybor = input(' Co chcesz zrobic?:  ').lower()
    if wybor == 'dodaj kontakt':
        nowy_nazw = input('Podaj nazwe:  ')
        nowy_num = input('Podaj numer:  ')
        kontakty.update({nowy_nazw: nowy_num})
        print(kontakty)

    elif wybor == 'wyswietl kontakt':
        sprawdzenie = input('Podaj kontakt do sprawdzenia:  ')
        if sprawdzenie in kontakty:
            print(kontakty[sprawdzenie])
        else:
            print('Nie ma takiego kontaktu ')

    elif wybor == 'usun kontakt':
        usun = input('Podaj kontakt do usunieca: ')
        if usun in kontakty:
            kontakty.pop(usun)
            print(' Usunieto! ')
        else:
            print('Nie ma takiego kontaktu ')

    elif wybor == 'wyswietl wszystko':
        print('---MOJE KONTAKTY---')
        for nowy_nazw, nowy_num in kontakty.items():
            print(f'{nowy_nazw}: {nowy_num}')   
        print('---KONIEC LISTY---')

    else:
        break