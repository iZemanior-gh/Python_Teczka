def prosty_generator():
    print('Zaraz Zwroce Pierwsza Wartosc...')
    yield 'Pierwsza Wartosc'
    print('Druga Wartosc:...')
    yield 'Druga Wartosc'


gen = prosty_generator()

print(next(gen))
print(next(gen))