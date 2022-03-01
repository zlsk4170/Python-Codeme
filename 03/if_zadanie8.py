# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

num1 = input('Podaj pierwszą liczbę całkowitą: ')
num2 = input('Podaj drugą liczbę całkowitą: ')
num3 = input('Podaj trzecią liczbę całkowitą: ')

lista = (num1, num2, num3)
max = max(lista)
print('Największa liczba to:',max)

order = sorted(lista,reverse=True)
print('Liczby posortowane od największej do najmniejszej',order)

