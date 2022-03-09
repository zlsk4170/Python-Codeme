# Utwórz listę lists_to_dict zawierającą listy 2 elementowe.
# Przekształć ją w słownik dict_from_list.

lists_to_dict = [('a',1),('b',2),('c',6)]
dict_from_list = dict(lists_to_dict)
print(dict_from_list)

for key, value in dict_from_list.items():
    print(key,':', value)