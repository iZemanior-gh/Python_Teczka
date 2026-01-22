import re
from pathlib import Path


def parsuj_log(sciezka_pliku:str | Path) -> dict:
    sciezka = Path(sciezka_pliku)
    if not sciezka.exists():
        print(f'Blad: Plik {sciezka} Nie Istnieje')
        return {'Adresy IP': [], 'Kody_Statusu': []}

    zawartosc = sciezka.read_text(encoding='utf-8')

    wzorzec_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}'
    wzorzec_status = r'(\d{3})'

    adresy_ip = re.findall(wzorzec_ip, zawartosc)
    kody_statusu = re.findall(wzorzec_status, zawartosc)

    return {'Adresy IP': adresy_ip, 'Kody Statusu': kody_statusu}

wynik = parsuj_log("log.txt")
print('--- Wynik Parsowania Loginu ---')
print(f'Znaleziono Adresy IP: {wynik['Adresy IP']}')
print(f'Kody Statusu: {wynik["Kody Statusu"]}')