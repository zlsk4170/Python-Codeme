# Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

# input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
# output:
#
# [4, 3, 2, 1]
# [14, 13, 12, 11]
# [24, 23, 22, 21]


lista = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

length = len(lista)
new_length = int(length/3)

lista1 = lista[0:new_length]
lista2 = lista[new_length:2*new_length]
lista3 = lista[2*new_length:3*new_length]

print(lista1[::-1])
print(lista2[::-1])
print(lista3[::-1])