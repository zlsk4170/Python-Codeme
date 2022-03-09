# Usuń duplikat z podanej listy i utwórz na jej bazie krotkę.
# Znajdź minimalną i maksymalną liczbę w krotce.

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
print('Oto lista pierwotna: ', example_list)

for item in example_list:
    if example_list.count(item) > 1:
        example_list.remove(item)
print('Oto lista bez duplikatów: ', example_list)

my_tuple = tuple(example_list)
print('Oto tuple z listy: ', my_tuple)

print('Oto największa liczba z tuple: ', max(my_tuple))
print('Oto najmniejsza liczba z tuple: ', min(my_tuple))