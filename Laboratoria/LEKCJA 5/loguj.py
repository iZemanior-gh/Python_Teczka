def loguj(funkcja):
    def wrapper():
        print('Start Funkcji : ')
        funkcja()
        print('Po Funkcji:  ')
    return wrapper

@loguj
def yo():
    print( 3 + 5)

yo()