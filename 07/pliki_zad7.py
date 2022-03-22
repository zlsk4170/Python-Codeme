# Wisielec. Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc.
# Poproś użytkownika o podanie kategorii przed rozpoczęciemy gry.
# Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy.
# Rozgrywka powinna być maksymalnie intuicyjna.

import random

def get_list():
    """ This function reads the content of the file: word categories and associated words """
    with open('categories.txt') as file:
        content = file.read()
        content = content.splitlines()
        content_list = []
        for item in content:
            temp = ''.join(item)
            temp = temp.split(':')
            content_list.append(temp)
        return content_list

def get_categories(content_list):
    """This function creates the list with word categories"""
    content_category = []
    for item in content_list:
        content_category.append(item[0])
    return content_category

def user_category(content_category):
    """This function asks user to select the word category from the list"""
    categories = content_category
    while True:
        user_input = input(f'Wybierz kategorię z listy {categories} \n')
        user_input = user_input.lower()
        if user_input in categories:
            return user_input
        else:
            print('Błędna wartość!')

def get_random_word_from_category(content_category,select_category,content_list):
    """This function selects a random word from a list of words belonging to the category selected by user"""
    indeks = content_category.index(select_category)
    words = content_list[indeks][1]
    words_list = words.split(',')
    random_word = random.choice(words_list)
    random_word = random_word.upper()
    return random_word



def hide_random_word(random_word_local):
    """This function hides the random word"""
    letter_list = list(random_word_local)
    hidden_list = letter_list

    print('TRY TO GUESS THE HIDDEN WORD! \n')

    for i in range(len(letter_list)):
        hidden_list[i] = ' * '

    print(''.join(hidden_list))
    return hidden_list

def give_nb_of_rounds():
    """This function asks user how many rounds he wants to play"""
    while True:
        ile = input('\nHOW MANY ROUNDS DO YOU WANT TO PLAY? -> ')
        if ile.isdigit():
            ile = int(ile)
            break
        else:
            print('Wrong value given. Number expected! \n')

    return ile

def show_you_won():
    """This function displays the message when the user won the game"""
    message_won = str(40*'*')+str('\nCONGRATULATIONS. YOU HAVE MADE IT!\n')+str(40*'*')
    return message_won

def show_you_lost(random_word_local):
    """This function displays the message when the user lost the game"""
    message_lost = str(40*'-')+str('\nGAME OVER. ') + str('THE HIDDEN WORD WAS: ') + str('"') + random_word_local + str('"')
    return message_lost


def game_engine(max_rounds_local,random_word_local,hidden_word_local,show_you_won_local,show_you_lost_local):
    """This is the algorythm for the game"""
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

def main():
    """This function stats the game"""
    content_list = get_list()
    content_category = get_categories(content_list)
    select_category = user_category(content_category)
    random_word = get_random_word_from_category(content_category,select_category,content_list)
    hidden_word = hide_random_word(random_word)
    max_rounds = give_nb_of_rounds()
    message_you_won = show_you_won()
    message_you_lost = show_you_lost(random_word)
    game_engine(max_rounds,random_word,hidden_word,message_you_won,message_you_lost)

main()




