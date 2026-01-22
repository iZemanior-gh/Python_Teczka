

while True:
    komenda = input(' Podaj Swoja Komende:  ').lower()
    if komenda == 'koniec':
        break
    if komenda.startswith('#'):
        print(' To Nie Jest Komenda')
        continue
    print('Wykonano Komende:  ' + komenda)
