# Oblicz średnią arymetyczną z kilku liczb.
# Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią.
# Program powinen być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

import sys

def ile_liczb():
    while True:
        try:
            ile = int(input('Podaj z ilu liczb mam obliczyć średnią: '))
            return ile
        except Exception as e:
            print('Podaj liczbe całkowitą')
            with open('error.txt','w') as file:
                file.write(str(sys.exc_info()[0])+str(e))


def srednia(ile):

    suma = 0

    for i in range(1,ile+1):
        try:
            liczba = float(input(f'Podaj liczbę nr {i}: '))
            suma = liczba + suma
        except Exception as e:
            print('To nie jest liczba')
            with open('error.txt','w') as file:
                file.write(str(sys.exc_info()[0])+str(e))

    avr = suma/ile
    print(f'Średnia to: {avr}')
    return avr

def main():
    liczby = ile_liczb()
    srednia(liczby)

if __name__ == '__main__':
    main()