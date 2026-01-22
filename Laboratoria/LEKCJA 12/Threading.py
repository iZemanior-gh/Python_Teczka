import requests
import threading
import time

def pobierz_kurs(waluta):
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json"
    print(f"Start pobierania: {waluta}")

    response = requests.get(url)
    data = response.json()
    mid = data['rates'][0]['mid']

    print(f"Kurs {waluta}: {mid}")
    print(f"Koniec pobierania: {waluta}")

waluty = ['EUR', 'USD', 'CHF', 'GBP', 'JPY']

print("--- Wersja Sekwencyjna ---")
start_time_seq = time.perf_counter()

for waluta in waluty:
    pobierz_kurs(waluta)

end_time_seq = time.perf_counter()
print(f"Czas całkowity (sekwencyjnie): {end_time_seq - start_time_seq:.4f} s")

print("\n--- Wersja Wielowątkowa ---")
start_time_thread = time.perf_counter()

watki = []

for waluta in waluty:
    watek = threading.Thread(target=pobierz_kurs, args=(waluta,))
    watki.append(watek)
    watek.start()

for watek in watki:
    watek.join()

end_time_thread = time.perf_counter()
print(f"Czas całkowity (wielowątkowo): {end_time_thread - start_time_thread:.4f} s")