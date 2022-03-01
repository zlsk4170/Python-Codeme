# Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3
# bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

num = int(input('Podaj liczbe całkowita: '))
if num % 3 == 0:
    print(f'Twoja liczba {num} jest podzielna przez 3')
else:
    print('Liczba nie jest podzielna przez 3')