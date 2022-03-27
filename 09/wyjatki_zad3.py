# Stwórz listę 10 elementową (różne typy!).
# Pozwól użytkownikowi podać dowolny index.
# Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

try:
    list = [0,(1,2),'aaa',12,False,12,{'aa':True},'w','aff','Fake']
    indeks = int(input('Podaj index listy: '))
    result = 1/list[indeks]
    print(result)
except TypeError as te:
    print(f'błędna wartość na liście',te)
except ZeroDivisionError as zd:
    print(f'Dzielenie przez zero',zd)
except ValueError as ve:
    print('Podałeś błędną wartość',ve)
except IndexError as ie:
    print('Indeks poza zakresem',ie)