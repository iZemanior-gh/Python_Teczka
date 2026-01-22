znajomi_anny = ['Piotr' , 'Zofia', 'Marek', 'Anna']
znajomi_piotra = ['Anna', 'Marek', 'Krzysztof', 'Ewa']

zbior_anny = set(znajomi_anny)
zbior_piotra = set(znajomi_piotra)

print(zbior_anny.intersection(zbior_piotra))
print(zbior_anny & zbior_piotra)