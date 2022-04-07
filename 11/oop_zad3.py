# Stwórz własną implementację kolejki FIFO.
# Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta,
# dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).
# Utwórz kilka obiektów klasy Queue z różnymi parametrami.

class Queue():

    def __init__(self,queue):
        self.queue = queue

    def show(self):
        print(f'Oto zawartość kolejki: {self.queue}')

    def isempty(self):
        return len(self.queue) == 0

    def put(self,item):
        print(f'Dodałem element: {item}')
        self.queue.append(item)

    def get(self):
        if self.isempty():
            return print('Brak elementów')
        else:
            return self.queue.pop(0)

kolejka = ['a','b','c','d']
obj1 = Queue(kolejka)

obj1.show()
obj1.isempty()
obj1.put('olala')
obj1.show()
print(obj1.get())
obj1.show()
print(obj1.get())
obj1.show()
print(obj1.get())
obj1.show()
print(obj1.get())
obj1.show()
print(obj1.get())
obj1.show()
print(obj1.get())
obj1.show()