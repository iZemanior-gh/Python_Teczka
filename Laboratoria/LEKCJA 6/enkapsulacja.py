class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self._hp = hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = nowa_wartosc


