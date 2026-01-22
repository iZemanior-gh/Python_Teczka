from pathlib import Path
from datetime import date

folder_raportow = Path('raport_dzienne')

sciezka = folder_raportow / str(date.today()) / 'raport.txt'

sciezka.parent.mkdir(parents=True, exist_ok=True)

tresc = f'raport z dnia {date.today()} \n wszystko w porzadku'
sciezka.write_text(tresc, encoding='utf-8')

print(f'\n ===Atrybuty Sciezki === \n'
      f'Nazwa: {sciezka.name} \n'
      f'Folder Nadrzedny: {sciezka.parent} \n'
      f'Rozszerzenie: {sciezka.suffix} \n'
      f'Sciezka Absolutna: {sciezka.resolve()}')