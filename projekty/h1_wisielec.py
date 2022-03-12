# Użytkownik ma za zadanie odgadnąć hasło, które ukryte jest w programie.
# Program pokazuje ile liter ma hasło i te litery, które zostały już odgadnięte
# Użytkownik podaje po jednej literze. Użytkownik ma ograniczoną ilość prób.
# W każdym momencie, zamiast podania litery użytkownik może spróbować odgadnąć całe hasło.

import random

words = ['train','probability','essential','street','python','eventually']
random_word = random.choice(words)
letter_list = list(random_word)
hidden_list = letter_list

print('TRY TO GUESS THE HIDDEN WORD! \n')

for i in range(len(letter_list)):
    letter_list[i] = ' * '

str_hidden_list = ''
print(str_hidden_list.join(letter_list), '\n')


while True:
    ile = input('HOW MANY ROUNDS DO YOU WANT TO PLAY? -> ')
    if ile.isdigit():
        ile = int(ile)
        break
    else:
        print('Wrong value given. Number expected! \n')


round = 1
while round <= ile:
    print(f'ROUND {round}')

    input_letter = input('PUT ONE LETTER OR HIDDEN PASSWORD: -> ')

    if input_letter == random_word:
        print('\n',35*'*','\n CONGRATULATIONS. YOU HAVE MADE IT!\n',35*'*')
        break

    if input_letter in random_word:
        for i in range(len(random_word)):
            if random_word[i] == input_letter:
                hidden_list[i] = input_letter
        str_hidden_list = ''
        print(str_hidden_list.join(hidden_list))

        if str_hidden_list.join(hidden_list) == random_word:
            print('\n',35*'*','\n CONGRATULATIONS. YOU HAVE MADE IT!\n',35*'*')
            break

    else:
        print(str_hidden_list.join(hidden_list))

    round += 1
else:
    print('\n',40*'-','\n GAME OVER. THE HIDDEN WORD WAS:', random_word)


