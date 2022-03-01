# Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

numbers = list(range(1,11))
print(numbers)

suma = 0
for item in numbers:
    suma = suma + item
    print(suma,end=' ')

