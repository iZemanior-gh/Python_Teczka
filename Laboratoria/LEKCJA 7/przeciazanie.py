
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

    def __eq__(self, other):
        return self.imie == other.imie

    def __lt__(self, other):
        return self.hp < other.hp


class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f'Moja Silo To {self.sila}')

    def atak(self):
        print(f' Cios: {self.imie} Atakuje Z Sila {self.sila}')

    def __add__(self, other):
        if isinstance(other, Wojownik):
            nowe_hp = self.hp + other.hp
            nowa_sila = self.sila + other.sila
            nowe_imie = f'Sojusz {self.imie} i {other.imie}'
            return Wojownik(imie=nowe_imie, hp=nowe_hp, sila=nowa_sila)
        else:
            raise TypeError("Można dodawać tylko obiekty klasy Wojownik")


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


Druzyna = [Aragorn, Wojagorn, Makaron,]

print(f' ---------------Druzyna---------------------')

for x in Druzyna:
    x.przedstaw_sie()
    print('-' * 20)


print(f'===Testing=== ')

print(Aragorn)
print(f'PORÓWNANIE (Aragorn == Aragorn): {Aragorn == Aragorn}')
print(f'Czy Wiecej HP? (Aragorn < Wojagorn): {Aragorn < Wojagorn}')

