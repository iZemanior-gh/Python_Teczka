import json
from pydantic import BaseModel, ValidationError

# --- KROK A: Przygotuj dane (Automatyczne utworzenie pliku produkt.json) ---
dane_startowe = {
    "nazwa_produktu": "Smartfon XYZ",
    "id_produktu": "prod-12345",
    "cena": "1999.99",  # Celowo jako string, Pydantic to przekonwertuje na float
    "dostepny": True,
    "tagi": ["elektronika", "nowość"],
    "specyfikacja": {
        "procesor": "SuperChip 1000",
        "ram_gb": 8
    }
}

with open("produkt.json", "w", encoding="utf-8") as f:
    json.dump(dane_startowe, f, indent=4)
    print("Utworzono plik: produkt.json")


# --- KROK B: Zdefiniuj modele Pydantic ---
class SpecyfikacjaModel(BaseModel):
    procesor: str
    ram_gb: int


class ProduktModel(BaseModel):
    nazwa_produktu: str
    id_produktu: str
    cena: float
    dostepny: bool
    tagi: list[str]
    specyfikacja: SpecyfikacjaModel


# --- KROK C: Napisz funkcję walidującą ---
def wczytaj_i_waliduj_produkt(sciezka: str) -> ProduktModel | None:
    try:
        # 1. Otwórz plik
        with open(sciezka, "r", encoding="utf-8") as f:
            dane = json.load(f)

        # 2. Parsuj i waliduj (używamy parse_obj zgodnie z poleceniem)
        produkt = ProduktModel.parse_obj(dane)

        print("\n✅ Walidacja zakończona sukcesem!")
        return produkt

    except FileNotFoundError:
        print(f"\n❌ Błąd: Nie znaleziono pliku '{sciezka}'")
        return None
    except json.JSONDecodeError:
        print(f"\n❌ Błąd: Plik nie zawiera poprawnego formatu JSON")
        return None
    except ValidationError as e:
        print(f"\n❌ Błąd walidacji danych Pydantic:\n{e}")
        return None


# --- KROK D: Przetestuj ---
if __name__ == "__main__":
    # Wywołanie funkcji
    wynik = wczytaj_i_waliduj_produkt("produkt.json")

    # Jeśli otrzymaliśmy obiekt, wyświetlamy atrybuty
    if wynik:
        print("-" * 30)
        print(f"Nazwa: {wynik.nazwa_produktu}")
        print(f"Cena: {wynik.cena} zł (Typ: {type(wynik.cena)})")
        print(f"Procesor: {wynik.specyfikacja.procesor}")
        print(f"RAM: {wynik.specyfikacja.ram_gb} GB")
        print("-" * 30)