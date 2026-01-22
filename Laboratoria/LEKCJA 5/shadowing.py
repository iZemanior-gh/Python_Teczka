x = 'Jestem Globalny'

def funkcja_zew():
    x = 'Jestem Otaczajacy'


    def funkcja_wew():
        x = 'Jestem Lokalny'
        print(x)

    funkcja_wew()
    print(x)

funkcja_zew()
print(x)