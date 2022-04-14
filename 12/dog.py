class Dog():

    vaccinated = True

    def __init__(self,name,colour,breed):
        self.name = name
        self.colour = colour
        self.breed = breed

    def bark(self,sound='bu'):
        return f'Szczekaj {self.name} {sound}'

azor = Dog('Azor','Czarny','Pudel')
reksio = Dog('Reksio','Biały','Jamnik')

print(azor.__dict__)
print(reksio.name)
print(reksio.bark('hau hau'))
print(azor.vaccinated)
