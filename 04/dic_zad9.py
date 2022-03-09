# 5 użytkowników poproś o podanie 4 przedmiotów szkolnych,
# sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot.
# (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)

zbiorcza_lista = []
for i in range(1,6):
    user = input(f'Użytkowniku nr {i} podaj 4 przedmioty szkolne oddzielając je przecinkiem: ')
    lista = user.replace(',',' ')
    lista = lista.lower()
    lista = lista.split()
    zbiorcza_lista.append(lista)

count = {}
for row in zbiorcza_lista:
    for item in row:
        if item not in count:
            count[item] = 1
        else:
            count[item] += 1


print('Następujące przedmioty powtarzają się na listach: ')
for k,v in count.items():
    if v > 1:
        print(k)

for k,v in count.items():
    if v == max(count.values()):
        print('Najpopularniejszy przedmiot to: ',k)


