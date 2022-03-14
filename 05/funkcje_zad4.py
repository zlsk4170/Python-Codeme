# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def check(zakres):
    if num in zakres:
        return True

num = 45
start = int(input('Podaj początek zakresu: '))
end = int(input('Podaj koniec zakresu: '))
zakres = range(start,end+1)

wynik = check(zakres)

if wynik == True:
    print(f'tak, liczba {num} znajduje się w zadanym zakresie')
else:
    print(f'nie, liczba {num} jest z poza zakresu')
