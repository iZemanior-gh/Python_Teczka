class IgnorujBledy:
    def __init__(self, bledy_do_ignorowania):
        self.bledy_do_ignorowania = bledy_do_ignorowania

    def __enter__(self):
        pass

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        if typ_bledu is not None:
            if issubclass(typ_bledu, self.bledy_do_ignorowania):
                print(f"Zignorowano błąd typu: {typ_bledu.__name__}: {wart_bledu}")
                return True
        return False


print("--- Test 1: Ignorowanie ValueError ---")
with IgnorujBledy((ValueError, TypeError)):
    print("Próbuję wykonać: int('abc')")
    x = int("abc")
    print("Ta linia się nie wykona, bo wiersz wyżej wystąpił błąd.")

print("-> Program nie wykrzaczył się i działa dalej!\n")

print("--- Test 2: Przepuszczenie ZeroDivisionError ---")
try:
    with IgnorujBledy((ValueError, TypeError)):
        print("Próbuję wykonać: 1 / 0")
        y = 1 / 0
except ZeroDivisionError:
    print("-> Sukces! Błąd ZeroDivisionError został wyrzucony normalnie (nie został stłumiony).")
