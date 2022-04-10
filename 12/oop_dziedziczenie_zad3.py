#Zadanie inspirowane popkulturą: https://www.youtube.com/watch?v=Ct6BUPvE2sM
#Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple.
# Logiki to nie ma, więc dodaj wg uznania.

class Pinapple():
    def __init__(self):
        return 'Pinapple'


class Pen():
    def __init__(self):
        a = super().__init__()
        b = 'Pen'
        return a+b


class PenPinapple(Pen,Pinapple):
    def __init__(self):
        print(super().__init__())

obj1 = PenPinapple()