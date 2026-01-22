
wzrost = int(input(' Ile Masz Wzrostu?:  '))
if wzrost < 140:
    print(' Nie Mozesz Wejsc Na Kolejke ')


if wzrost >= 140:
    wiek = int(input(' Ile Masz Lat?:  '))
    if wiek >= 18:
        print(' Mozesz Wejsc Na Kolejke')
    elif wiek < 18:
        zgoda = input(' Czy Masz Zgode Opiekuna?:  (Tak/ Nie):  ').lower()
        if zgoda == 'tak':
            print(' Mozesz Wejsc Na Kolejke')
        else:
            print(' Nie Masz Wstepu Na Kolejke ')


