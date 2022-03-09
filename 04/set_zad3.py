# Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

tup1 = (1,2,3,4)
tup2 = (5,6,7,8,9)

list1 = list(tup1)
list1_even = list1[0:len(list1):2]
print(list1_even)

list2 = list(tup2)
list2_odd = list2[1:len(list2):2]
print(list2_odd)

sum = list1_even + list2_odd
print(sum)

new_set = set(sum)
print(new_set)