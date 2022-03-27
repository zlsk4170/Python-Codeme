# Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie z cyfr od 0-9. Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
# Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
# Zaimportuj generator bezpośrednio do programu.

import random

def menu():
    print('W jaki sposób chcesz uzyskać sekwencję znaków?')
    print('1 - pozwalam wylosować komputerowi')
    print('2 - chcę sam podać')
    user_choice = input()
    return user_choice

def generate_num_sequence(user_choice):

    if user_choice == str(2):
        seq = input('Podaj własną sekwencję znaków: ')
        return str(seq)
    elif user_choice == str(1):
        seq_length = random.randint(10,100)
        num_range = list(range(0,10))
        seq = ''
        for i in range(1,seq_length):
            num = str(random.choice(num_range))
            seq = seq+num
        print(seq)
        return str(seq)
    else:
        print('Wartość nieprawidłowa.')


def find_longest_duplicates(seq):
    temp_list = []
    longest_list = []

    for index, char in enumerate(seq):
        if index == 0:
            temp_list = [char]
            longest_list = [char]
        else:
            if char == seq[index-1]:
                temp_list.append(char)
            else:
                if len(longest_list) < len(temp_list):
                    longest_list = temp_list
                temp_list = [char]

    return longest_list