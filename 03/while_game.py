# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie
# (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 12

while True:
    num = int(input('Podaj liczbę od 0 do 20: '))
    if num != secret_num:
        print('Try again')

    else:
        print('You won! Game over')
        break