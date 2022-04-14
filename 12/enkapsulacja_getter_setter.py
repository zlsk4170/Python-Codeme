class Point:

    def __init__(self,num):
        self.__x = '0'
        self.num = num

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x


p1 = Point(10)
print(p1.num)
# print(p1.__x) # nie zadziała, atrybut prywatny! potrzebujemy getter lub setter gdy chcemy nadpisać

print(p1.get_x())

p1.set_x(5)
print(p1.get_x())