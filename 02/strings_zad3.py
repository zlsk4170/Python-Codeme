print()
print('Do zmiennej quote przypisz zdanie: „Honesty is the first chapter in the book of wisdom.”, a następnie:')
print()

print('* Policz wszystkie znaki w napisie')
quote = "Honesty is the first chapter in the book of wisdom."
print('Ilość wyszystkich znaków w napisie wynosi: ->', len(quote))
print()

print('* Nie modyfikując zmiennej wyświetl słowo wisdom ->', quote[-7:-1])
print()

print('* Wyświetl tylko pierwszą połowę tekstu ->')
center = int(len(quote)/2)
print(quote[:center])
print()

print('* Wyświetl tylko kropke ->', quote[-1])
print()

print('* Wyświetl od połowy tylko co trzecią literę cytatu ->', quote[center::3])
print()

print('* Wyświetl "Hnsyi h is hpe ntebo fwso."" ->', quote[::2])
print()

print('* Wyświetl cały cytat odwrotnie ->', quote[::-1])
print()

print('* Zamień wisdom na słowo friendship ->', quote.replace('wisdom','friendship'))
print()