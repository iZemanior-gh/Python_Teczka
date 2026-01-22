plik = open('wiek.txt', 'w')
plik.write('25')
plik.close()

def oblicz_rok_urodzenia(sciezka_do_pliku):
    try:
        with open(sciezka_do_pliku, 'r') as file:
            tekst = file.read()
            wiek = int(tekst)
            rok_urodzenia = 2025 - wiek
            return rok_urodzenia

    except FileNotFoundError:
        print("BŁĄD: Nie Znaleziono Pliku!")
    except ValueError:
        print("BŁĄD: Zawartość Pliku Nie Jest Liczba!")

    finally:
        plik.close()

print("--- SCENARIUSZ 1 (OK) ---")
wynik = oblicz_rok_urodzenia('wiek.txt')
if wynik is not None:
    print(f'Rok Urodzenia To: {wynik}')

print("\n--- SCENARIUSZ 2 (Brak pliku) ---")
wynik2 = oblicz_rok_urodzenia('niestniejacy.txt')
if wynik2 is not None:
    print(f'Rok Urodzenia To: {wynik2}')



print("\n--- SCENARIUSZ 3 (Błędne dane) ---")
plik = open('wiek.txt', 'w')
plik.write('abc')

wynik3 = oblicz_rok_urodzenia('wiek.txt')
if wynik3 is not None:
    print(f'Rok Urodzenia To: {wynik3}')