def odczytywanie():
    odczyt = open('C:/Users/skipp/Desktop/pyth.txt', 'r')
    print(odczyt.read())
    odczyt.close()

pisanie = open('C:/Users/skipp/Desktop/pyth.txt', 'w')
pisanie.write('Pierwszy Wpis \n'
        'Wszystko Dziala \n')
pisanie.close()

odczytywanie()

dopisywanie = open('C:/Users/skipp/Desktop/pyth.txt', 'a')
dopisywanie.write('Drugi Wpis \n')
dopisywanie.close()

odczytywanie()