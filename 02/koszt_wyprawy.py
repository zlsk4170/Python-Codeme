"""
Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
Załóżmy, że spalanie na 100km wynosi 6.4 l, trasa to 120km, litr benzyny kosztuje 5.04 zł.
"""

fuel_consumption = 6.4
unit_price = 5.04
distance = 120

total_cost = distance/100 * unit_price * fuel_consumption
print(total_cost)
print()

# Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

fuel_consumption = float(input('Podaj zużycie paliwa na 100km [l]: '))
unit_price = float(input('Podaj cenę 1 l paliwa [zł]: '))
distance = float(input('Podaj dystans [km]: '))
total_cost = distance/100 * unit_price * fuel_consumption
print(f'Koszt wyprawy wynosi: {round(total_cost,2)} zł')
