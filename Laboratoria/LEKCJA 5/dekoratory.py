def moj_dekorator(funkcja_do_udekorowania):
    def wrapper():
        print('Cos Przed Wywolaniem Funkcji ...')
        funkcja_do_udekorowania()
        print('Cos Po Wywolaniu Funkcij')

    return wrapper


@moj_dekorator
def powiedz_czesc():
    print('Czesc')



powiedz_czesc()