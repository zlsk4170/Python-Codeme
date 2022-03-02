# Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

values = ('k','p','n')
round = 1
wins = 0
lost = 0
draw = 0


max_rounds = int(input('Podaj ilość rund: '))

print('Wybierz kamien (k), papier (p) lub nożyce (n). Aby zakończyć wprowadź "koniec"')

while round <= max_rounds:
    print('Runda',round)
    human = input('Twój wybór: ')
    if human == 'koniec':
        break
    if human not in values:
        print('Podano wartość niedozwoloną')
        continue

    computer = random.choice(values)
    print('Komputer wybrał:', computer)

    if human == computer:
        print('Remis')
        draw += 1
    if human == 'k' and computer == 'n':
        wins += 1
        print('Wygrałeś')
    if human == 'p' and computer == 'k':
        wins += 1
        print('Wygrałeś')
    if human == 'n' and computer == 'p':
        wins += 1
        print('Wygrałeś')
    if human == 'k' and computer == 'p':
        lost += 1
        print('Przegrałeś')
    if human == 'p' and computer == 'n':
        print('Przegrałeś')
        lost += 1
    if human == 'n' and computer == 'k':
        print('Przegrałeś')
        lost += 1
    round += 1

print()
print(f'Wygrane: {wins}, Przegrane: {lost}, Remis: {draw}')