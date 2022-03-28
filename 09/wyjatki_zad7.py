# Wróć do pierwszego zadania z lekcji o plikach,
# zmodyfikuj go tak, aby to użytkownik podawał nazwę pliku z cytatami.
# Pamiętaj, by użytkownik po wykonaniu błędnej akcji (np. literówki w nazwie pliku) miał możliwość poprawić swój błąd.

import random


def select_random_quote():
    while True:
        try:
            new_file_local = input('Podaj ścieżkę do swego pliku .txt: ')
            with open(new_file_local) as f:
                quote = random.choice(f.readlines())
                quote = quote.strip()
                quote = quote.split('-')
                break
        except:
            print('Błędny plik')
    return quote

def display(text):
    return print('\n',30*'*', '\n',text[0].center(30),'\n',text[1].center(30),'\n',30*'*')


def display_random_quote():
    random_text = select_random_quote()
    display(random_text)

display_random_quote()