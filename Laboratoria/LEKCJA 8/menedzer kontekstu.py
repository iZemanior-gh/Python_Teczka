import time

class MiernikCzasu:
    def __enter__(self):
        self.start = (time.perf_counter())
        print('Rozpoczynam Pomiar')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.koniec = (time.perf_counter())
        czas = self.koniec - self.start
        print(f'Czas Trwania To {czas}')

with MiernikCzasu():
    suma = sum(n for n in range(10_000_000))