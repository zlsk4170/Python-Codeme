# Utworz klasę Kraj, która zawiera informację o
# powierzchni. ludności, jaki język jest urzędowy, jakie miasto jest stolicą.
# Utwórz klika obiektów klasy Kraj, stwórz listę obiektów klasy kraj, wyświetl elementy na liście krajów.

class Country():
    def __init__(self,name,area,population,language,capital):
        self.name = name
        self.area = area
        self.population = population
        self.language = language
        self.capital = capital

    def __repr__(self):
        return f'{self.name} --> Area:{self.area}, Population:{self.population}, Lanugage:{self.language}, Capital:{self.capital}'

poland = Country('Poland','326000','37000000','polish','Warsaw')
germany = Country('Germany','357000','83000000','german','Berlin')

list = []
list.append(poland)
list.append(germany)

for item in list:
    print(item.__repr__())

