# Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

lista = list(days.values())

single_elem = []

for item in lista:
    counter = lista.count(item)
    if counter == 1:
        single_elem.append(item)
print(single_elem)