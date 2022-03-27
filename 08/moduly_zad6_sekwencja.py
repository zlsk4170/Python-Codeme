# Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
# Wejście:
# var = ‘banannnnannnnnnnnnanananananaaaana’
# Wyjście
# ‘nnnnnnnnn’, 9
# Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie z cyfr od 0-9. Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
# Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
# Zaimportuj generator bezpośrednio do programu.

import module_generator as generator

def main():
    show_menu = generator.menu()
    gen_seq = generator.generate_num_sequence(show_menu)
    result = generator.find_longest_duplicates(gen_seq)
    if len(result) == 1:
        print('Losowa sekwencja nie posiada sąsiadująch znaków tego samego typu')
    else:
        print(f'Najdłuższa sekwencja tych samych znaków to: {result}. Ilość znaków: {len(result)}')

if __name__ == '__main__':
    main()
