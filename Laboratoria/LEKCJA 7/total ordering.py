from functools import total_ordering


class BrakPunktowZyciaError(Exception):
    def __init__(self, wiadomosc="Gracz nie ma wystarczającej liczby HP!"):
        super().__init__(wiadomosc)


@total_ordering
class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def __str__(self):
        return f'{self.imie} {self.hp}'

    def __repr__(self):
        return f'{self.imie} {self.hp}'

    def przedstaw_sie(self):
        print(f'Jestem {self.imie}, Mam {self.hp} HP')

    def __eq__(self, other):
        if not isinstance(other, Gracz):
            return NotImplemented
        return self.imie == other.imie

    def __lt__(self, other):
        if not isinstance(other, Gracz):
            return NotImplemented
        return self.hp < other.hp


class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f'Moja Sila To {self.sila}')

    def atak(self):
        if self.hp <= 0:
            raise BrakPunktowZyciaError(f"{self.imie} jest martwy i nie może atakować!")
        print(f'>> Cios: {self.imie} Atakuje Z Sila {self.sila}')


Nowicjusz = Gracz('Nowicjusz', 50)
Weteran = Gracz('Weteran', 100)
Klon = Gracz('Nowicjusz', 999)

print(f' --------- TEST PORÓWNAŃ ---------')
print(f'1. {Nowicjusz} <  {Weteran}: {Nowicjusz < Weteran}')  # True (50 < 100)
print(f'2. {Nowicjusz} >  {Weteran}: {Nowicjusz > Weteran}')  # False (Magia total_ordering!)
print(f'3. {Nowicjusz} <= {Weteran}: {Nowicjusz <= Weteran}')  # True
print(f'4. {Nowicjusz} >= {Weteran}: {Nowicjusz >= Weteran}')  # False
print(f'5. {Nowicjusz} == {Klon}:  {Nowicjusz == Klon}')  # True (Bo mają to samo imię!)
print(f'6. {Nowicjusz} != {Weteran}: {Nowicjusz != Weteran}')  # True