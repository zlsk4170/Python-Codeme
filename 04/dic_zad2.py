# Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe.
# Przekształć ją w słownik dict_from_tuples.

tuples_to_dict = (('a',1),('b',2),('c',3))
dict_from_tuples = dict(tuples_to_dict)
print(dict_from_tuples)

for key,value in dict_from_tuples.items():
    print(key,':',value)