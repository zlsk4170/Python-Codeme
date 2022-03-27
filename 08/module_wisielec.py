import random

def give_random_word():
    words = ['TRAIN','PROBABILITY','ESSENTIAL','STREET','PYTHON','EVENTUALLY']
    random_word = random.choice(words)
    return random_word

def hide_random_word(random_word_local):

    letter_list = list(random_word_local)
    hidden_list = letter_list

    print('TRY TO GUESS THE HIDDEN WORD! \n')

    for i in range(len(letter_list)):
        hidden_list[i] = ' * '

    print(''.join(hidden_list))
    return hidden_list

def give_nb_of_rounds():

    while True:
        ile = input('\nHOW MANY ROUNDS DO YOU WANT TO PLAY? -> ')
        if ile.isdigit():
            ile = int(ile)
            break
        else:
            print('Wrong value given. Number expected! \n')

    return ile

def show_you_won():
    message_won = str(40*'*')+str('\nCONGRATULATIONS. YOU HAVE MADE IT!\n')+str(40*'*')
    return message_won

def show_you_lost(random_word_local):
    message_lost = str(40*'-')+str('\nGAME OVER. ') + str('THE HIDDEN WORD WAS: ') + str('"') + random_word_local + str('"')
    return message_lost


def game_engine(max_rounds_local,random_word_local,hidden_word_local,show_you_won_local,show_you_lost_local):

    round = 1
    while round <= max_rounds_local:
        print(f'ROUND {round}')
        input_letter = input('PUT ONE LETTER OR HIDDEN PASSWORD: -> ')
        input_letter = input_letter.upper()

        if input_letter == random_word_local:
            print(show_you_won_local)
            break

        if input_letter in random_word_local:
            for i in range(len(random_word_local)):
                if random_word_local[i] == input_letter:
                    hidden_word_local[i] = input_letter
            str = ''.join(hidden_word_local)
            print(str)

            if str == random_word_local:
                print(show_you_won_local)
                break
        else:
            str = ''.join(hidden_word_local)
            print(str)
        round += 1
    else:
        print(show_you_lost_local)