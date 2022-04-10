# Stwórz abstrakcyjną klasę Pojazdy.
# Utwórz potomne klasy pojazdy np. Samochód, Rower, Autobus, Ciężarówki.
# Dodaj opisy zgodne z tym jak te pojazdy są klasyfikowane.
# Jaki rodzaj dokumentu jest potrzebny, by kierować poszczegolnym pojazdem.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def desc(self):
        pass

    @abstractmethod
    def require_driving_licence(self):
        pass


class Car(Vehicle):
    def desc(self):
        return 'Car is good'

    def require_driving_licence(self):
        return 'cat. B'

    def __repr__(self):
        return f'Car - licence {self.require_driving_licence()}'

class Bike(Vehicle):
    def desc(self):
        return 'I love my bike ....'

    def require_driving_licence(self):
        return 'bike card'

    def __repr__(self):
        return f'Bike - licence {self.require_driving_licence()}'

class Bus(Vehicle):
    def desc(self):
        return 'Driving the bus requires more skills'

    def require_driving_licence(self):
        return 'cat. D'

    def __repr__(self):
        return f'Bus - licence {self.require_driving_licence()}'

class Truck(Vehicle):
    def desc(self):
        return 'Driving the truck is difficult'

    def require_driving_licence(self):
        return 'cat. C'

    def __repr__(self):
        return f'Truck - licence {self.require_driving_licence()}'



suzuki = Car()
print(suzuki)
print(suzuki.desc())

romet = Bike()
print(romet)
print(romet.desc())

mercedes = Bus()
print(mercedes)
print(mercedes.desc())