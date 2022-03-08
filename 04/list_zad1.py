# 1▹ Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Elementy na liście posortuj alfabetycznie, a następnie wyświetl.

list = ['latarka','mapa','bidon','namiot','kompas','kanapki']

list.sort()


for i, item in enumerate(list):
    print(i+1, item)