import pickle

class StanGry:
    def __init__(self, nazwa, punkty, ekwipunek):
        self.nazwa_gracza = nazwa
        self.punkty = punkty
        self.ekwipunek = ekwipunek

    def __repr__(self):
        print(self.nazwa_gracza, self.punkty, self.ekwipunek)

stan1 = StanGry('Krzysiek', -10, ['autyzm'])

stan1.__repr__()

with open('stan1.pkl', 'wb') as f:
    pickle.dump(stan1, f)

with open('stan1.pkl', 'rb') as f:
    stan1odczyt = pickle.load(f)

