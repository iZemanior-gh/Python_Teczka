class BrakPunktowZyciaError(Exception):
    def __init__(self, wiadomosc="Gracz nie ma wystarczającej liczby HP!"):
        super().__init__(wiadomosc)


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
        else:
            print(f'>> Cios: {self.imie} Atakuje Z Sila {self.sila}')



Aragorn = Gracz('Aragorn', 100)
Wojagorn = Wojownik('Wojagorn', 125, 17)
MartwyWojownik = Wojownik('Szkielet', 0, 5)

Druzyna = [Aragorn, Wojagorn, MartwyWojownik]

print(f' ---------------Druzyna---------------------')

for x in Druzyna:
    print('-' * 20)
    x.przedstaw_sie()

    if isinstance(x, Wojownik):
        try:
            x.atak()
        except BrakPunktowZyciaError as e:
            print(f'!!! BŁĄD: {e}')