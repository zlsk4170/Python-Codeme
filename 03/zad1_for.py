# Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację:
# “Great, we are ready!”


# list =['latarka','plecak','woda']
#
# for item in list:
#     print(item)
# print('Great, we are ready')

przedmiot1 = input('Jaki przedmiot zabierasz: ')
przedmiot2 = input('Jaki przedmiot zabierasz: ')
przedmiot3 = input('Jaki przedmiot zabierasz: ')

list =[przedmiot1,przedmiot2,przedmiot3]

for item in range(len(list)):
    print(item, list[item])
print('Great, we are ready')