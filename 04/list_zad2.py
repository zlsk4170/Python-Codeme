# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

list = []
for i in range(1,11):
    num = int(input(f'Podaj liczbę nr {i}: ' ))
    if num % 2 != 0:
        list.append(num)
print('Lista zawierająca liczby nieparzyste:', list)

