slowo = input(' Podaj Dowolne Slowo:  ')
ls = 0
samogloski = 'aeiouy'
for litera in slowo.lower():
    if litera in samogloski:
        ls =+ 1

print(ls)
#liczy kazda samogloske w podanym slowie, dodaje do licnzika, na koniec wyswietla slowo a pod nim licznik
#zle liczy