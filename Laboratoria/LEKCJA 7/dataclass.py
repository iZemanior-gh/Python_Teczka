from dataclasses import dataclass

@dataclass
class PunktData:
    x: int
    y: int

p1 = PunktData(10,20)
p2 = PunktData(10,20)
p3 = PunktData(10,30)

print(f'===Dataclass Test===')
print(p1)
print(f'Czy p1 = p2?: {p1==p2}')
print(f'Czy p1 = p3?: {p1==p3}')