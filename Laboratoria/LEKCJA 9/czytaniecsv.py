import csv


def wczytaj_pracownikow(sciezka_pliku: str) -> list:
    wyniki = []
    try:
        with open(sciezka_pliku, 'r', newline='', encoding='utf-8') as f:
            czytnik = csv.DictReader(f)
            for nr_wiersza, wiersz in enumerate(czytnik, 2):
                try:
                    wiersz['pensja'] = int(wiersz['pensja'])
                    wyniki.append(wiersz)
                except ValueError:
                    print(f'Ostrzezenie: Pominieto Wiersz: {nr_wiersza}'
                          f'Z Powodu Bledu Formatu Pensji')
                except KeyError:
                    print(f'Ostrzezenie: Pominieto Wiersz {nr_wiersza}'
                          f'Z Powodu Braku Kolumny ''Pensja')
    except FileNotFoundError:
        print(f'Blad: Plik "{sciezka_pliku}" Nie Zostal Znaleziony')

    return wyniki

