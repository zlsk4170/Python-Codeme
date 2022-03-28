# Wywołaj błąd związany z otwarciem pliku.
# Spróbuj odczytać plik, który nie istnieje.
# Spróbuj odczytać wartość z pliku otwartym w trybie w
# Spróbuj utworzyć plik, który już istnieje w trybie x
# Obsłuż w dowolny sposób każdy z powyższych błędów.

import io, os

def menu():

    choice = (1,2,3)

    print('Co chcesz zrobić:')
    print('1 - otwórz plik')
    print('2 - odczytaj zawartość pliku')
    print('3 - utwórz plik')

    while True:
        try:
            user = int(input('Wybierz liczbę: '))
            if user in choice:
                if user == 1:
                    return 1
                if user == 2:
                    return 2
                if user == 3:
                    return 3
        except:
            print('Błędna wartość')

def exist():
    path = input('Podaj nazwe pliku: ')
    try:
        with open(path,encoding='utf-8') as file:
            if os.stat(path).st_size ==0 or os.stat(path).st_size !=0:
                return path
    except:
        print('Plik nie istnieje')


def read(path):
    with open(path,encoding='utf-8') as file:
        if os.stat(path).st_size ==0 or os.stat(path).st_size !=0:
            print(file.read())

def main():
    choice = menu()
    if choice == 1:
        try:
            ifexist = exist()
            read(ifexist)
        except:
            pass

    if choice == 2:
        try:
            path = exist()
            with open(path,'w') as file:
                content = file.read()
                print(content)
        except io.UnsupportedOperation:
            print('Plik otwarty do zapisu. Odczyt w tym trybie niemożliwy.')
        except:
            pass
    if choice == 3:
        path = input('Podaj nazwe pliku: ')
        try:
            with open(path,'x') as file:
                file.write('')
        except FileExistsError:
            print('Nie można utworzyć pliku który już istnieje.')

main()