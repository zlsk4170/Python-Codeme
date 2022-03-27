# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje oraz czy jest niepusty.
import os

def check_file():

    path = input('Podaj nazwe/ścieżkę do pliku: ')
    try:
        with open(path) as file:
            if os.stat(path).st_size == 0:
                return path, True
            else:
                print(f'Oto zawartość pliku:\n',file.read())
                print(f'Plik niepusty jest chroniony przed zapisem')
    except FileNotFoundError:
        print('Nazwa pliku nieprawidłowa')


def save_file():
    plik = check_file()
    while plik == None:
        break
    else:
        with open(plik[0],'w') as file:
            content = input('Wprowadź nową zawartość do pliku: ')
            print('Proces zapisu zakończony powodzeniem')
            return file.write(content)