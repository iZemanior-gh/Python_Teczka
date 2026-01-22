pkt = int(input(' Ile Miales Punktow?:  '))

if pkt <= 50:
    print(' Ocena 2.0')
elif 51 <= pkt <= 60:
    print(' Ocena 3.0')
elif 61 <= pkt <= 70:
    print(' Ocena 3.5')
elif 71 <= pkt <= 80:
    print(' Ocena 4.0 ')
elif 81 <= pkt <= 90:
    print(' Ocena 4.5')
elif 91 <= pkt <= 100:
    print(' Ocena 5.0 ')

else:
    print( ' Oszust ')