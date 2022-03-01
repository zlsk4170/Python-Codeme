# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

num1 = input('Podaj pierwszą liczbę całkowitą: ')
num2 = input('Podaj drugą liczbę całkowitą: ')

suma = int(num1) + int(num2)

if suma > 100:
    print('Suma dwóch liczb wynosi: ', suma)
else:
    print('Koniec')