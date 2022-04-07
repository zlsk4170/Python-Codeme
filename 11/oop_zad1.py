# Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
# atrybuty: imię, kolor sierści, rasę
# metody: szczekaj, machaj ogonem
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.

class Pies():
    def __init__(self,name,colour,breed):
        self.name = name
        self.colour = colour
        self.breed = breed

    def szczekaj(self):
        return f'Szczekaj {self.name}'

    def machaj(self):
        return f'Machaj ogonem {self.colour} {self.name}'

obj1 = Pies('Azor','Czarny','Pudel')
obj2 = Pies('Reksio','Biały','Jamnik')

print(obj1.name)
print(obj1.szczekaj())
print(obj1.machaj())