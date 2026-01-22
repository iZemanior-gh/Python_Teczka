class NiepoprawnaIloscProduktuError(ValueError):
    pass

def dodaj_do_koszyka(produkt, ilosc):
    try:
        if ilosc <= 0:
            raise NiepoprawnaIloscProduktuError('Ilość Produktów Niewłaściwa')
        else:
            print(f'{produkt}: {ilosc} szt.')
    except NiepoprawnaIloscProduktuError as e:
        print(f'Błąd: {e}')


dodaj_do_koszyka('marchew', -1)
dodaj_do_koszyka('marchew', 3)
