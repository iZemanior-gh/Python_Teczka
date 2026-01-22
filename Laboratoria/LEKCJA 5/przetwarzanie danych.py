imiona = ['anna', 'piotr', 'zofia']

zduzej = list(map( lambda x: x.capitalize() , imiona))
print(zduzej)

oceny = [5,3,2,5,4,2,3,4]
powyzej = list(filter(lambda x : x>=4, oceny))
print(powyzej)