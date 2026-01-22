import json

moje_dane ={
    'ulubiony_kolor': 'żółty',
    'najgorsza_rasa': 'czarna'
}

def zapisz_jako_json(dane: dict | list, sciezka_pliku: str ):
    try:
        with open(sciezka_pliku, 'w', encoding='utf-8') as f:
            json.dump(moje_dane, f, ensure_ascii=False, indent=4)
        print(f'Sukces, Zapisano Do Pliku: {sciezka_pliku}')
    except IOError as e:
        print(f'Blad Podczas Zapisywania Pliku {e}')


if __name__ == '__main__':
    zapisz_jako_json(moje_dane, 'dane.json')