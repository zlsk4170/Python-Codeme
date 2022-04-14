from abc import ABC, abstractmethod

class Animal():
    @abstractmethod
    def poop(self):
        print('***********')

class Horse(Animal):
    def poop(self):
        return 'cc'

class Unicorn(Animal):
    def poop(self):
        return 'dd'

def vet(animal):
    print('robie badanie --->',animal.poop())


def main():
    print('Chodźmy do weterynarza')
    konik = Horse()
    jednorozec = Unicorn()
    vet(konik)
    vet(jednorozec)


main()
# różne obiekty z różnych klas mogą posiadać takie same metody
# wiele obiektów mogą korzystać z
