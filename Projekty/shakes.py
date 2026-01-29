

"""
walka jak w szejksach razem z statami, wybierasz klase z abilitka,
woj, zwiad, mag, co walke dostajesz 10%hp leczenia i wybierassz losowa state jedna z trzech
do podniesienia
"""

Dostepne = ['Wojownik', 'Mag', 'Zwiadowca']
Klasa = input('Wybierz Swoja Klase:  ').capitalize()

#Wybieranie Klasy Az Do Wybrania Poprawnej
def wybieranie(Klasa):
    while True:
        if Klasa in Dostepne:
            return Klasa
        else:
            print('Niepoprawna Klasa, Wybierz Jeszcze Raz')
            Klasa = input().capitalize()
            continue

Klasa = wybieranie(Klasa)

Wojownik ={
    'Sila' : 250,
    'Zrecznosc' : 100,
    'Inteligencja' : 50,
    'Wytrzymalosc' : 1000,
    'Szczescie' : 100,
    'Armor' : 200
}

Zwiadowca ={
   'Sila' : 100,
   'Zrecznosc' : 250,
   'Inteligencja' : 100,
   'Wytrzymalosc' : 500,
   'Szczescie' : 200,
   'Armor' : 100
}

Mag ={
    'Sila' : 50,
    'Zrecznosc' : 50,
    'Inteligencja' : 200,
    'Wytrzymalosc' : 250,
    'Szczescie' : 250,
    'Armor' : 50
}

#Liczenie Dmg
def dmg(Klasa):

    if Klasa == 'Wojownik':
        obrazenia = Wojownik['Sila'] * 2
        return obrazenia
    elif Klasa == 'Zwiadowca':
        obrazenia =  Zwiadowca['Zrecznosc'] * 2
        return obrazenia
    elif Klasa == 'Mag':
        obrazenia = Mag['Inteligencja'] * 2
        return obrazenia

obrazenia = dmg(Klasa)


def HP(Klasa):
    if Klasa == 'Wojownik':
        HP = Wojownik['Wytrzymalosc'] * 1.25
        return HP
    elif Klasa == 'Zwiadowca':
        HP = Zwiadowca['Wytrzymalosc'] * 1.25
        return HP
    elif Klasa == 'Mag':
        HP = Mag['Wytrzymalosc'] * 1.25
        return HP

PZ = HP(Klasa)

def pancerz(Klasa):
    if Klasa == 'Wojownik':
        Pancerz = Wojownik['Armor']
        return Pancerz
    elif Klasa == 'Zwiadowca':
        Pancerz = Zwiadowca['Armor']
        return Pancerz
    elif Klasa == 'Mag':
        Pancerz = Mag['Armor']
        return Pancerz

ARM = pancerz(Klasa)

def kryt(klasa):
    if Klasa == 'Wojownik':
        sz_k = Wojownik['Szczescie'] / 10
        return sz_k
    elif Klasa == 'Zwiadowca':
        sz_k = Zwiadowca['Szczescie'] / 10
        return sz_k
    elif Klasa == 'Mag':
        sz_k = Mag['Szczescie'] / 10
        return sz_k

sz_k = kryt(Klasa)

#Postac
print(f'-- Wybrana Klasa To: {Klasa} -- \n'
      f'Zadawane Obrazenia: {obrazenia} \n'
      f'Twoje zdrowie: {PZ} \n'
      f'Pancerz: {ARM} \n'
      f'Szansa Na Kryta: {sz_k}%')


#Armor Zmniejsza Obrazenia O Wartosc Int Armora

print('\n \n')


n = 1
PZ_E = 1000
Obr_E = 250
pokonani = 0

while True:
    print(f' == Tura {n} == \n'
          f'Aktualnie Zdrowie: {PZ}')

    print(f'Zdrowie Przeciwnika: {PZ_E}')
    akcja = input(' Atak/Obrona:  ').capitalize()



    if akcja == 'Obrona':
        PZ = ((PZ - Obr_E / 2) + ARM )
    else:
        PZ = (PZ - Obr_E) + ARM
        PZ_E = PZ_E - obrazenia



    if PZ <= 0: #Przegrana
        print(' Przegrano ')
        break

    if PZ_E <= 0: #Wygrana
        pokonani += 1
        print(f' Pokonano Przeciwnika \n'
              f' Pozostale HP {PZ} \n'
              f' Pokonano: {pokonani} Przeciwnikow!')
        kontynuacja = input('Kontynuowac? ').capitalize()

        if kontynuacja == 'Tak':
            PZ = PZ + PZ/10
            PZ_E = 1000
            continue
        else:
            break
    n += 1









