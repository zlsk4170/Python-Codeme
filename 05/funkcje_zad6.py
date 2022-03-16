# Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

def how_many_rounds():
    while True:
        max_rounds = input('Podaj ilość rund: ')
        if not max_rounds.isdigit():
            print('Podaj wartość liczbową.')
        else:
            return (int(max_rounds))

def user():
    values = ('k','p','n')
    print('Wybierz kamien (k), papier (p) lub nożyce (n). Aby zakończyć wprowadź "koniec"')
    user_value = input('Twój wybór: ')
    if user_value == 'koniec':
        return 'Koniec gry'
    if user_value not in values:
        print('Podano wartość niedozwoloną')
    else:
        return user_value


def computer():
    values = ('k','p','n')
    comp_value = random.choice(values)
    print('Komputer wybrał:', comp_value)
    return comp_value


def check_draw(user_value, comp_value):
    if user_value == comp_value:
        print('Remis')
        return 1

def check_wins(user_value,comp_value):
    if (user_value == 'k' and comp_value == 'n') or (user_value == 'p' and comp_value == 'k') or (user_value == 'n' and comp_value == 'p'):
        print('Wygrałeś')
        return 1

def check_lost(user_value,comp_value):
    if (user_value == 'k' and comp_value == 'p') or (user_value == 'p' and comp_value == 'n') or (user_value == 'n' and comp_value == 'k'):
       print('Przegrałeś')
       return 1

def run_game():

    draw = 0
    win = 0
    lost = 0

    for i in range(1,how_many_rounds()+1):
        print('Runda',i)
        u = user()

        if u == 'Koniec gry':
            print('Koniec gry')
            break

        c = computer()

        if check_draw(u,c) == 1:
            draw +=1

        if check_wins(u,c) == 1:
            win +=1

        if check_lost(u,c) == 1:
            lost +=1

    print()
    print('WYNIKI')
    print('Liczba remisów:', draw)
    print('Liczba wygranych:', win)
    print('Liczba przegranych:', lost)

run_game()