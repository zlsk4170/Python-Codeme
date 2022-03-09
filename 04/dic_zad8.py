# Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej.
# Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

my_dict = {
    'Poland': ['Julia','Anne','Elizabeth','Agness','Catherine','Sophia','Olivia','Amellia','Izabella','Lucy'],
    'France': ['Anne','Beatrice','Celine','Annette','Audrey','Sophia','Brigitte','Amellia','Gisele','Denice'],
    'England': ['Olivia','Amelia','Isla','Ava','Mia','Isabella','Sophia','Rosy','Lilly','Merry'],
    'Germany': ['Emilia','Emma','Lena','Lina','Julia','Ida','Leoni','Lea','Sophia','Rita'],
    'Italy': ['Sophia','Julia','Aurora','Alice','Ginevra','Greta','Ida','Rosy','Annette','Lucy'],
    'Spain': ['Sophia','Adela','Isabella','Isla','Martina','Greta','Celine','Gisele','Maya','Catalina'],
    'Czechia': ['Helena','Gita','Hanka','Inka','Anne','Blanka','Irma','Jana','Kamila','Lena'],
    'Norway': ['Anne','Anita','Astrid','Eli','Eva','Linda','Merry','Ingeborg','Sigrid','Rosy'],
    'Belgium': ['Merry','Nathalie','Catherine','Eva','Alice','Ida','Rita','Nicole','Christine','Denice'],
    'Austria': ['Helga','Rita','Catherine','Sigrid','Alice','Julia','Sarah','Nicole','Lena','Gisele']
}

lista = list(my_dict.values())

all_names = []
for row in lista:
    for item in row:
        all_names.append(item)

dict_counter = {}
for item in all_names:
    if item not in dict_counter:
        dict_counter[item] = 1
    else:
        dict_counter[item] += 1

for key,value in dict_counter.items():
    if value >= 3:
        print(key,'->',value)
