slownik = {
    'imie': 'Bartosz',
    'nazwisko' : 'Zemanek',
    'stanowisko' : 'Student'
}

print(f' {slownik['imie']} {slownik['nazwisko']}')
print(slownik['stanowisko'])

slownik['miasto'] = 'Krakow'

print(slownik)

slownik['miasto'] = 'Bielsko-Biala'
print(slownik)

