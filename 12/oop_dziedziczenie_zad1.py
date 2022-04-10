# Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek.
# Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
# Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta.
# Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.


class Animals():
    def __init__(self):
        print('Jestem zwierzęciem')

    def desc(self):
        print('Zwierzęta to nie ludzie')

class Mammals(Animals):
    def __init__(self):
        print('Jestem ssakiem')
    def desc(self):
        super().desc()
        print('Ssaki należą do zwierząt')

class Cat(Mammals):
    def __init__(self):
        print('Jestem kotem')

    def desc(self):
        print('Kot jest ssakiem i zwierzęciem')

class Dog(Mammals):
    def __init__(self):
        print('Jestem psem')

    def desc(self):
        print('Pies jest ssakiem i zwierzęciem')

class Human(Mammals):
    def __init__(self):
        super().__init__()
        print('Jestem czlowiekiem')

    def desc(self):
        super().desc()
        print('Człowiek to ssak')


jan = Human()
# reksio = Dog()
# bonifacy = Cat()

print(jan.desc())
