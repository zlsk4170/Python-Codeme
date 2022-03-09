# Stwórz krotkę liczb całkowitych.
# Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks.

my_tuple = (1,2,3,5,6,9,44,234,23,22,111)

num = int(input('Podaj dowolną liczbę całkowitą -> '))

if num in my_tuple:
    print('Indeks liczby', num, 'to', my_tuple.index(num))