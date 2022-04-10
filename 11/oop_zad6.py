# Utwórz klasę Pracownik.
# Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
# Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
# Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
# Pracownik powinien mieć pole typu boolowskiego zawierające status studenta.
# Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
# Wszyscy pracownicy mają wspólną nazwę firmy.
# Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.

class Pracownik():
    company_name = "adidas"

    def __init__(self,first_name,last_name,job,salary,seniority,student):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.salary = salary
        self.seniority = seniority
        self.student = student

    def give_pay_rise(self):
        rate = 10
        pay_raise = self.salary * rate/100
        new_salary = self.salary + pay_raise
        return new_salary

    def calculate_tax(self):
        tax_rate = 18
        tax = self.salary * tax_rate/100
        return tax

    def calculate_health_contribution(self):
        if self.student == False:
            health_rate = 9
            health_contribution = self.salary * health_rate/100
            return health_contribution
        else:
            health_contritution = 0
            return health_contritution

    def create_email(self):
        consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','w','z','x']
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()
        consonants_in_first_name = []
        consonants_in_last_name = []

        for letter in self.first_name:
            if letter in consonants:
                consonants_in_first_name.append(letter)
        consonants_in_first_name = ''.join(consonants_in_first_name)

        for letter in self.last_name:
            if letter in consonants:
                consonants_in_last_name.append(letter)
        consonants_in_last_name = ''.join(consonants_in_last_name)
        email = consonants_in_first_name + '.' + consonants_in_last_name + '@' + self.company_name + '.pl'
        return email

pracownik1 = Pracownik('Jan','Kowalski','driver',4000,10,False)

print(f'Pensja pracownika: {pracownik1.salary}')
print(f'Należny podatek: {pracownik1.calculate_tax()}')
print(f'Należna składka zdrowotna: {pracownik1.calculate_health_contribution()}')
print(f'Pensja pracownika po podwyżce: {pracownik1.give_pay_rise()}')
print(f'Adres email: {pracownik1.create_email()}')
