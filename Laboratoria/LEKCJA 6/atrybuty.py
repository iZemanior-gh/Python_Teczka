class Gracz:
        liczba_graczy = 0
        def __init__(self, imie, hp):
            self.imie = imie
            self.hp = hp
            Gracz.liczba_graczy += 1
            print(f' Do Gry Dolacza {self.imie}')

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

print(f' Liczba Graczy: = {Gracz.liczba_graczy} =')
gracz_1 = Gracz('Aragorn', 100)
gracz_2 = Gracz('Nyga', 100)
gracz_3 = Gracz('Skurwiel', 100)


print(f' Aktualna Liczba Graczy = {Gracz.liczba_graczy} =')

