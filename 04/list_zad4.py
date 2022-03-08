# Pobierz od użytkownika parzystą listę elementów.
# Sprawdź czy 2 środkowe elementy są takie same.

while True:
    max = int(input('Podaj z ilu elementów będzie składała się Twoja lista. Podana liczba musi być parzysta -> '))

    if max % 2 == 0:

        list = []
        for i in range(1,max+1):
            num = int(input(f'Podaj liczbę nr {i}: ' ))
            list.append(num)
        środek = int(len(list)/2)

        if list[środek-1] == list[środek]:
            print('Środkowe elementy listy są takie same')
            break
        else:
            print('Środkowe elementy listy są różne')
            break

    else:
        print('Nieprawidłowa wartość')
        print()