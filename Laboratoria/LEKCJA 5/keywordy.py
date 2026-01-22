def wyslij_email(adres, temat,  tresc, *,  priorytet='normalny'):
    print (f'adres: {adres} \n'
           f'temat: {temat} \n'
           f'tresc: {tresc} \n'
           f'priorytet: {priorytet}')


wyslij_email(
    'anna@pk',
    'spotkanie',
    'czesc jutor',
    priorytet='wysoki'
)

#sprawdzic co robi ten * ('keyword') w porownaniu do zwyklego i input