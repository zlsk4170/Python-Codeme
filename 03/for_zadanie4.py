# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).

num = int(input('Podaj liczbę N mniejszą od 8 -> '))

if num > 8:
    print('Liczba poza zakresem')

else:
    zakres = list(range(1,num+1))
    silnia = 1

    for item in zakres:
        silnia *= item
    print(f'Silnia liczb {zakres} wynosi {silnia}')


