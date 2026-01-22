wiek = int(input(' Podaj Swoj Wiek '))

if wiek < 13:
    print(' jestes dzieckiem')
elif wiek > 13 and wiek < 18:
    print(' jestes nastolatkiem ')
elif wiek > 18 and wiek < 64:
    print(' jestes dorosly ')
else:
    print(' jestes seniorem ')