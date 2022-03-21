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
        f.write('\nkeep smiling - autor6')

    return file

def select_five_lines(new_file_local):
    with open(new_file_local) as f:
        for i in range(5):
            line = f.readline().strip()
            print(line)


new_file = create_file()
select_five_lines(new_file)