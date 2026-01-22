import pytest
from kalkulator import dodaj, dzielenie
from portfel import Portfel


#def test_dodawanie():
#    assert dodaj(2,3) == 5

#def test_ujemne():
#    assert dodaj(-2,-3) == -5

def test_dzielenie():
    with pytest.raises(ValueError):
        dzielenie(10,0)

def test_poprawne():
    assert dzielenie(10,2) == 5

@pytest.fixture
def pusty_portfel():
    return Portfel()

def test_salda(pusty_portfel):
    assert pusty_portfel.saldo == 0

def test_wplaty(pusty_portfel):
    pusty_portfel.wplac(20)
    assert pusty_portfel.saldo != 0

@pytest.mark.parametrize('x,y, Oczekiwany_Wynik',[
    (2,3,5),
    (-2, -2,-4),
    (-2, 5, 3),
    (2,0, 2)
])

def test_dodawania(x, y, Oczekiwany_Wynik):
    assert dodaj(x,y) == Oczekiwany_Wynik

