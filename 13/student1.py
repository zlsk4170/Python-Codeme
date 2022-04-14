class Student:
    university = 'university'
    min_avg = 4.7

    def __init__(self,name,last,grades):
        self.name = name
        self.last = last
        self.grades = grades

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return f'{self.last}.{self.name}@university.com'

    def grand_schoolarship(self):
        if self.grades > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Nie tym razem')

    # def set_new_avg(self,new_value):
    #     self.min_avg = new_value

    @classmethod
    def set_new_avg(cls,new_value):
        cls.min_avg = new_value


obj_anna = Student('anna','kowalska',4.75)
obj_mirek = Student('mirek','lobuz',4.23)

obj_anna.grand_schoolarship()
obj_mirek.grand_schoolarship()

obj_mirek.set_new_avg(4.2) # jeśli zmienimy to przez wywołanie obiektu to zmiana będzie tylko dla tego obiektu
obj_mirek.grand_schoolarship()

print(obj_anna.min_avg) # w efekcie anna ma inną średnią niż mirek
print(obj_mirek.min_avg) # w efekcie anna ma inną średnią niż mirek to jest nie dobrze

#poprzez dekoratora @classmethod możemy sprawić że wszystkie obiekty otrzymają tą samą zmianę zmianę

print('*******')
Student.set_new_avg(4.1)
print(obj_anna.min_avg)
print(obj_mirek.min_avg)