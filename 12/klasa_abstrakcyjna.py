from abc import ABC, abstractmethod

class Shape(ABC):  # biblioteka ABS tworzy klasę abstrakcyjną która jest tylko definicją, ale nie ma implementacji
    @abstractmethod #klasa nie ma ciałą, każde dziecko które będzie dziedziczyć tą klasę będzie musiało podać wypełnienie - funkcję
    def area(self): # abstract method
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r = r
        self.pi = 3.14

    def area(self):
        return self.pi * self.r**2

    def __repr__(self):
        return f'Circle = {self.area()}'

c = Circle(10)
print(c)
