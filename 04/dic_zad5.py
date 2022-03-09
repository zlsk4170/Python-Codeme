# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
#
# Zadbaj o sposób wyświetlania np.:
# szybko : 5
# zbudź : 1

txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""


txt = txt.replace(',', '')
txt = txt.lower()
lista = txt.split()


count = {}

for item in lista:
    if item not in count:
        count[item] = 1
    else:
        count[item] += 1

for k, v in count.items():
    print(k, ':', v)