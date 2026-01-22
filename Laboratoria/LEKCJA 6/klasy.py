class Gracz:
    def __init__(self, imie, hp):
        self.imie = imie
        self.hp = hp

    def __str__(self):
        return f'{self.imie} {self.hp}'

    def __repr__(self):
        return f'{self.imie} {self.hp}'

    def pokaz_status(self):
        print(f'{self.imie} {self.hp}')

    def otrz_obr(self,ilosc):
        self.hp -= ilosc
        print(f' {self.imie} Otrzymuje {ilosc} Obrazen')
        if self.hp < 0:
            print(' {self.imie} Pokonany')

gracz_1 = Gracz(imie='Aragorn', hp=100)




gracz_1.pokaz_status()
gracz_1.otrz_obr(20)

print(gracz_1)
