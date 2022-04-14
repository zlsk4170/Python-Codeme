import datetime
from holidays import Poland

class Student:
    university = 'university'
    min_avg = 4.7

    def __init__(self, name, last, grades):
        self.name = name
        self.last = last
        self.grades = grades
        # self.nickname = name + '***'

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    def email(self):
        return f'{self.last}.{self.name}@{self.university}.com'

    @property #dzięki temu możemy sprawić ze funkcja bedzie się zachowywać jak parametr
    def nickname(self):
        return self.name + '****'

    @property
    def fullname(self): # to jest domyslnie getter
        return f'{self.name.capitalize()} {self.last.capitalize()}'

    @fullname.setter # rozszerzamy funkcję fullname o setter, aby mozna go bylo zmienić pozniej
    def fullname(self,name_last):
        self.name, self.last = name_last.split()

    @fullname.deleter # rozszerzamy o usuwanie
    def fullname(self):
        self.name, self.last = None,None

    def grand_scholarship(self):
        if self.grades > self.min_avg:
            print("You get scholarship")
        else:
            print("Not this time")

    @classmethod
    def set_new_avg(cls, new_value):
        cls.min_avg = new_value

    @classmethod #metody klasowe - działa dla wszystkich obiektów w klasie, a nie tylko dla jednego jeśli wywołujemy dla niego metodę
    def set_new_university(cls,new_name):
        cls.university = new_name

    @staticmethod #to metoda która istnieje niezaleznie od klasy, rownie dobrze moglaby być zewnętrzną metodą, ale używamy ją na tyle często że oplaca nam się wsadzić tą metodę wewnątrz klasy
    # nie korzysta z zadnych parametrów tej klasy
    def get_salary_net_under_26(salary_gross):
        if salary_gross < 85000:
            return salary_gross
        else:
            return 85000 + (salary_gross - 85000) * 0.83

    # @staticmethod
    # def academic_day(day):
    #     # if day.weekday() == 5 or day.weekday() == 6:
    #     return not day.weekday() in [5,6] # można to wszystko skrócić bo pytamy o True, False
        #     return False
        # else:
        #     return True

    @staticmethod
    def is_academic_day(day):
        is_weekend = day.weekday() in [5,6]
        free_days_pl = Poland()
        is_free_day = day in free_days_pl

        return not is_weekend and not is_free_day


obj_anna = Student('anna', 'kowalska', 4.72)
obj_michal = Student('michal', 'nowak', 4.69)
print(obj_anna.min_avg)
print(obj_michal.min_avg)

obj_michal.grand_scholarship()

obj_michal.set_new_avg(4.5)
obj_michal.grand_scholarship()

print(obj_anna.min_avg)
print(obj_michal.min_avg)

print('*************')
Student.set_new_avg(4.1) #możemy wywołać w ten sposób, poprzez dekoratora @classmethod możemy sprawić że wszystkie obiekty otrzymają tą samą zmianę zmianę
print(obj_anna.min_avg)
print(obj_michal.min_avg)

obj_michal.set_new_university('politechnika') #można też wywołać poprzez jeden obiekt, poprzez dekoratora @classmethod możemy sprawić że wszystkie obiekty otrzymają tą samą zmianę zmianę
print(obj_anna.university)
print(obj_michal.university)
print(obj_michal.email())

annual_salary = obj_michal.get_salary_net_under_26(4300 * 12)
print(annual_salary)


today = datetime.date.today()
print(today)

trech_kroli = datetime.datetime.strptime('2022-01-06', '%Y-%m-%d')
print('Czy dzisiaj są zajęcia? ', Student.is_academic_day(today))


#**********property
obj_ann = Student('anna','smith',4.0)
print(obj_ann.nickname)
obj_ann.name = 'ann'
print(obj_ann.nickname) #nickname pozostał ten sam, bo obiekt powstaje tylko raz przy tworzeniu więc initializer przechodzi tylko raz przy inicjalizacji
#anna ma błędny nickname
print(obj_ann)

#teraz należy wywołać tę metodę
# print(obj_ann.nickname()) #zmiast wstawiać nawiasy można użyć @property który sprawi że nickname zostanie potraktowany jak zwykły parametr, nie trzeba tego wywoływać jako metody
print(obj_ann.nickname) # dzięki @property zmieniliśmy to na parametr, a nie funkcję

#zmiana stanu cywilnego
print(obj_ann.fullname)

obj_ann.fullname = 'Anna Snow' # normalnie w @property nie można tego zrobić, ale properies ma w sobie setter który możemy wykorzystać

print(obj_ann.name)
print(obj_ann.last)

print('Usuwam bo RODO')
del obj_ann.fullname #usuwamy za pomocą deletera
print(obj_ann.name)
print(obj_ann.last)