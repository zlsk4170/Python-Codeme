# Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

my_tuple = ('hello','dog',123,True,'dog','monkey','hello')

lista = []
for item in my_tuple:
    counter = my_tuple.count(item)
    if counter > 1:
        if lista.count(item) == 0:
            lista.append(item)

my_new_tuple = tuple(lista)
print(my_new_tuple)










