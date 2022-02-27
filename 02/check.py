
'''
Czy 23 + 3 będzie się równać 15 + 12 ?

Czy dzielenie 29 przez 7 bez reszty wynosi 5?

Czy 27 podzielone przez 8 daje resztę 3?

Wyświetl True, jeżeli liczba jest parzysta.
'''

print((23+3) == (15+12))

print((29//7==5))

print(27%8 == 3)

liczba = int(input('Podaj liczbe: '))

print(liczba % 2 == 0)