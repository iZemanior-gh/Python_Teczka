def generuj_raport(imie, stanowisko="Pracownik", miasto="Nieznane"):
    raport = (f"Raport:\n - Imię: {imie}\n - Stanowisko: {stanowisko}\n - Miasto: {miasto}")
    return raport

raport_anny = generuj_raport('Anna', stanowisko="Student")
raport_piotra = generuj_raport('Piotr', miasto='Bielsko')


print(raport_anny)
print('\n')
print(raport_piotra)



"""
print("Test 1: tylko imię")
generuj_raport("Anna")

print("\nTest 2: imię i miasto z (użyciem argumentu nazwanego)")
generuj_raport("Piotr", miasto="Gdańsk")

print("\nTest 3: Wszystkie dane w dowolnej kolejności")
generuj_raport(stanowisko="Manager", imie="Zofia", miasto="Kraków")

"""