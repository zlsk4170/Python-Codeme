# Utwórz plik na pulpicie zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii.
# Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
# Quote of the day is:
#
# **************************************
# be or not to be?
# **************************************

# zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami#
# plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora

import random, os

def create_file():
    file = 'quotes.txt'
    with open(file,'w') as f:
        f.write('to be or not to be - autor1')
        f.write('\neven a worm will turn - autor2')
        f.write('\nnever give up - autor3')
        f.write('\nrelax - autor4')
        f.write('\ndo not be affraid - autor5')

    return file

def select_random_quote(new_file_local):
    # new_file_local = input('Podaj ścieżkę do swego pliku .txt: ')
    with open(new_file_local) as f:
        quote = random.choice(f.readlines())
        quote = quote.strip()
        quote = quote.split('-')
    return quote

def display(text):
    return print('\n',30*'*', '\n',text[0].center(30),'\n',text[1].center(30),'\n',30*'*')


def display_random_quote():
    new_file = create_file()
    random_text = select_random_quote(new_file)
    display(random_text)
    size = os.stat(new_file).st_size
    print(f'File size is equal:',size,'bytes')

display_random_quote()