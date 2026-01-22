
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def __str__(self):
        return f'{self.imie} {self.hp}'

    def __repr__(self):
        return f'{self.imie} {self.hp}'

    def przedstaw_sie(self):
        print(f'Jestem {self.imie}, Mom {self.hp}HP')

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f'Moja Silo To {self.sila}')

    def atak(self):
        print(f' Cios: {self.imie} Atakuje Z Sila {self.sila}')


class Mag(Gracz):
    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f'Moja Mana To {self.mana}')

Aragorn = Gracz('Aragorn', 100)
Wojagorn = Wojownik('Wojagorn', 125, 17)
Makaron = Mag('Makaron', 75, 19)


class Ekwipunek:
    def __init__(self, przedmioty=[]):
        self.przedmioty = przedmioty

    def dodaj(self, przedmioty):
        self.przedmioty.append(przedmioty)

    def pokaz(self, przedmioty):
        for x in self.przedmioty:
            print(f'    -  {x}')