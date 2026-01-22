lista = []

while True:
    zakupy = input('Dodaj zakupy do listy  ').lower()
    if zakupy == 'koniec':
        break
    else:
        lista.append(zakupy)


lista.sort()
for  index, produkt in enumerate(lista, start=1):
    print(f'{index}. {produkt.capitalize()}')

