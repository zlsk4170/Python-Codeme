# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def suma():
    return sum(input_data())

def input_data():
    ile = int(input('Ile liczb chcesz wprowadzic? '))
    x = []
    for i in range(ile):
        liczba = int(input('Podaj liczbe: '))
        x.append(liczba)
    return x

wynik = suma()
print(f'Suma liczb wynosi {wynik}')