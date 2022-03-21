# Wyświetl 3 losowe cytaty

import random

def create_file():
    file = 'quotes.txt'
    with open(file,'w') as f:
        f.write('to be or not to be - autor1')
        f.write('\neven a worm will turn - autor2')
        f.write('\nnever give up - autor3')
        f.write('\nrelax - autor4')
        f.write('\ndo not be affraid - autor5')
        f.write('\nkeep smiling - autor6')
        f.write('\nthis is your best day ever - autor7')

    return file

def select_three_random(new_file_local):
    with open(new_file_local) as f:
        content = f.readlines()
        for i in range(3):
            random_quote = random.choice(content)
            random_quote = random_quote.strip()
            print(random_quote)


new_file = create_file()
select_three_random(new_file)