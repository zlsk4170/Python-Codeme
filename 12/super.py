class Animal():

    def __init__(self):
        print("I'm animal")

    def show_desc(self):
        print('To jest klasa Animal')


class Wolf(Animal):
    paw = 4

    def __init__(self):
        print("I'm wolf")


class Dog(Wolf):

    def __init__(self,name,colour,breed):
        self.name = name
        self.colour = colour
        self.breed = breed

    def show_desc(self):
        super().show_desc() # gdy nazwy metod sa takie same super() pozwala skorzystać nam z metody rodzica, wykona nam dwa
        super().__init__() # tylko klasa wyżej
        print('To jest klasa Dog')

wolf = Wolf()
wolf.show_desc()
print(wolf.paw)
reksio = Dog('Reksio','Biały','Jamnik')
print(reksio.paw)
reksio.show_desc()