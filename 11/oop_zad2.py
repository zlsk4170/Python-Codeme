# Utwórz klasę dla storczyków.
# Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
# Utwórz dowolne atrybuty i metody.
# Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.

class Storczyki():

    type = 'plants'

    def __init__(self,colour,flowering_time,species):
        self.colour = colour
        self.flowering_time = flowering_time
        self.species = species

    def show(self):
        return {self.colour},{self.flowering_time},{self.species}

    def update_colour(self):
        print(f'Current colour: {self.colour}')
        new_colour = input('Define a new colour: ')
        self.colour = new_colour
        return self.colour

storczyk1 = Storczyki('grey','June','king size')
storczyk2 = Storczyki('red','June','king size')
print(storczyk1.update_colour())
print(storczyk2.show())
print(storczyk1.type)