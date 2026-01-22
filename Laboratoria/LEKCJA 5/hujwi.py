liczba = [1 , 2 , 3]

kwadrat  =  list(map( lambda x : x**2, liczba))
print(kwadrat)

parzysta = (list(filter( lambda x: x % 2 == 0, liczba)))
print(parzysta)