# Utwórz dowolną tablicę n x n zawierającą dowolny znak,
# a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją



n = int(input('Podaj rozmiar tabeli n x n, n = '))

tablica = [['-']*n]*n

for raw in tablica:
    for item in raw:
        print(item, end=' ')
    print()