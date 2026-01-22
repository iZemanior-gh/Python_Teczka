
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def __str__(self):
        return f'{self.imie} {self.hp}'

    def __repr__(self):
        return f'{self.imie} {self.hp}'

    def przedstaw_sie(self):
        print(f' Jestem {self.imie}, Mom {self.hp}')

class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f'Moja Silo To {self.sila}')

    def atak(self):
        print(f' Cios: {self.imie} Atakuje Z Sila {self.sila}')


Aragorn = Gracz('Aragorn', 100)
Wojagorn = Wojownik('Wojagorn', 125, 17)

Aragorn.przedstaw_sie()
Wojagorn.przedstaw_sie()

Wojagorn.atak()
#Aragorn.atak() Nie Ma Sily
