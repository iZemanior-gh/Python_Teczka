import re
from pathlib import Path

def analizuj_czas_logow(sciezka_pliku: str | Path) -> timedelta | None:
    sciezka = Path(sciezka_pliku)
    if not sciezka.exists():
        return None

    zawartosc = sciezka.read_text(encoding='utf-8')

    wzorzec_daty = r'[(d{2}\)]'
    daty_jako_string = re.findall(wzorzec_daty, zawartosc)

    if not daty_jako_string: