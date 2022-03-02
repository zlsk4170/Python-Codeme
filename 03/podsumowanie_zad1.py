# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

string = input('Wprowadź imiona oddzielając je przecinkiem: ')
lista = string.split(',')

for element in lista:
    name = element.replace(' ','')
    print('Witaj',name)
