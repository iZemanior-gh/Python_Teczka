def licz_do_trzech():
    yield '1'
    yield '2'
    yield '3'

gen = licz_do_trzech()

for x in gen:
    print(f'Generator Wygenerowal: {x}')