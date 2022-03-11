# Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów
# (wykorzystać funkcje z pkt 2)

def even():
    even_list = []
    for item in input_data():
        if item % 2 == 0:
            even_list.append(item)
    return even_list

def input_data():
    ile = int(input('Ile liczb chcesz wprowadzic? '))
    x = []
    for i in range(ile):
        liczba = int(input('Podaj liczbe: '))
        x.append(liczba)
    return x

wynik = even()
print(f'Liczby parzyste to: {wynik}')
