# Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd

tuple = (1,'a',{13},(1,3,4),False)

try:
    user_index = int(input('Podaj indeks aby wyświetlić zawartość krotki -> '))
    print(tuple[user_index])
    user_input = input('Podaj nową wartość krotki -> ')
    tuple[user_index] = user_input
except ValueError:
    print('Podana wartość musi być liczbą')
except IndexError:
    print('Wartość poza zakresem')
except TypeError:
    print('Nie można zmieniać zawartości krotki')