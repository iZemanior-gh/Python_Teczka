from portfel import NiewystarczajaceSrodki


def dodaj(x,y):
    return (x+y)

def dzielenie(x,y):
    if y == 0:
        raise ValueError
    return x/y

def srednia(liczby:list[float]) -> float | None:
    if liczby is None:
        return None
    else:
        return liczby/len(liczby)
