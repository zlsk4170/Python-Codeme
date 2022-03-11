# Napisać funkcję, która sprawdza czy liczba jest parzysta.

def even(liczba):
    wynik = liczba % 2
    return wynik

def result(wynik):
    if wynik == 0:
        print(f'Liczba parzysta')
    else:
        print(f'Liczba nieparzysta')


n = int(input('Podaj liczbe: '))
result(even(n))