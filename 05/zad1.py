def circle_area(promien):
    pi = float(3.14)
    area = pi * promien **2
    return area

radius = int(input('Podaj promien: '))
print(f'Promien kola wynosi {circle_area(radius)}')
