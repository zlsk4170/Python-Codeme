# Pomyśl co sprawia, że ssak jest ssakiem?
# Utwórz klasę ssaki.
# Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.

class Mammals():

    limbs = 4
    fur = True
    lungs = True

    def __init__(self,colour,weight):
        self.colour = colour
        self.weight = weight

    def give_sound(self):
        print(f'Wydaje dźwięk')

wolf = Mammals('grey',80)
horse = Mammals('brown',250)
cat = Mammals('white',4)

print(wolf.weight)
horse.give_sound()
print(cat.colour)
print(horse.fur)
