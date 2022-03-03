# Stwórz grę ciepło zimno.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

computer = random.randint(1,100)
print('Komputer wylosował liczbę zakresu od 1 do 100, spróbuj odgadnąć ją w 6 próbach. Powodzenia!')
human = int(input('Ustaw referencyjną liczbę od której rozpoczniemy sprawdzanie -> '))


if human != computer:

    ref0 = abs(computer-human)
    lista = [ref0]

    for i in range(1,7):
        print('Runda', i)
        human = int(input('Podaj liczbę -> '))

        if human == computer:
            print('Udało Ci się, gratulacje! Koniec gry')
            break

        ref1 = abs(computer-human)
        lista.append(ref1)

        if lista[i] > lista[i-1]:
            print('zimno')
        if lista[i] < lista[i-1]:
            print('ciepło')
        if lista[i] == lista[i-1]:
            print('Taka sama wartość jak poprzednio.Wybierz inną liczbę')
        if i == 6:
            print(f'Nie udało Ci się. Poszukiwana liczba to {computer}. Koniec gry.')
else:
    print('Udało Ci się, gratulacje! Koniec gry.')