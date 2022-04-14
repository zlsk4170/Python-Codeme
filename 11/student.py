class Student():
    university = 'UAM'
    def __init__(self, firstname,lastname,subject):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject

    def email(self):
        return f'{self.firstname}.{self.lastname}@{self.university}.pl'.lower()

obj_anna = Student('Anna','Kowalska','Architektura')
obj_jan = Student('Jan','Nowak','Biology')

print(obj_anna.email)
print(obj_jan.email)
# print(obj_jan.__dict__)
# print(Student.__dict__)
print(obj_jan.email())
print(Student.email(obj_jan))