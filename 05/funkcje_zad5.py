# Stwórz grę ciepło zimno.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random


def sukces():
    print('Udało Ci się, gratulacje! Koniec gry')

def ref0():
    ref0 = abs(computer-human0)
    ref = [ref0]
    return ref

def game():

    ref = ref0()

    for i in range(1,7):
        print('Runda', i)
        human1 = int(input('Podaj liczbę -> '))

        if human1 == computer:
            sukces()
            break

        ref1 = abs(computer-human1)
        ref.append(ref1)

        if ref[i] > ref[i-1]:
            print('zimno')
        if ref[i] < ref[i-1]:
            print('ciepło')
        if ref[i] == ref[i-1]:
            print('Taka sama wartość jak poprzednio.Wybierz inną liczbę')
        if i == 6:
            print(f'Nie udało Ci się. Poszukiwana liczba to {computer}. Koniec gry.')



print('Komputer wylosował liczbę zakresu od 1 do 100, spróbuj ją odgadnąć w 6 próbach.')
print('Jeśli w kolejnych próbach będziesz się zbliżał do poszukiwanej liczby komputer wyświetli: "ciepło"')
print('Jeśli będziesz się oddalał od poszukiwanej liczby, komputer wyświetli: "zimno". Powodzenia!')

computer = random.randint(1,100)
human0 = int(input('Ustaw referencyjną liczbę od której rozpoczniemy sprawdzanie -> '))

if human0 == computer:
    sukces()
else:
    game()