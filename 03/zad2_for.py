# Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55


suma = 0
for num in range(1,11):
    suma = suma + num
    print(suma)


list = range(1,11)
suma = 0
for num in list:
    suma = suma + num
    print(suma)

