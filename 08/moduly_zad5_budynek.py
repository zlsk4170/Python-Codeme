# Stwórz moduł obliczający pola różnych figur.
# W nowym pliku utwórz skrypt, który na podstawie podanych składowych kształtów pomieszczeń
# oraz ich wymiarów zwraca powierzchnię budynku.

import module_pola as area


def flat():
    rooms = int(input('Podaj ilość pomieszczeń: '))
    return rooms

def room():
    shape = input('Podaj ksztalt pomieszczenia [k,p,t]: ')
    return shape

def room_area(shape):
    if shape == 'k':
        bok = float(input('Podaj dlugość boku: '))
        pow1 = area.kwadrat(bok)
        return pow1
    if shape == 'p':
        bok1 = float(input('Podaj dlugosc boku "a": '))
        bok2 = float(input('Podaj dlugosc boku "b": '))
        pow2 = area.prostokat(bok1,bok2)
        return pow2
    if shape == 't':
        a = float(input('Podaj dlugosc podstawy trojkata "a": '))
        h = float(input('Podaj wysokosc "h": '))
        pow3 = area.trojkat(a,h)
        return pow3


def main():
    flat_area = 0
    rooms = flat()
    for i in range(rooms):
        shape_room = room()
        flat_area = flat_area + room_area(shape_room)
    print(f'Powierzchnia mieszkania wynosi: {flat_area} m2')

if __name__ == '__main__':
    main()