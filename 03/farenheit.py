# Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

print('Z pętlą while')
F = 0
while F <= 200:
    c = 5/9 * (F - 32)
    print(f'{F} F -> {round(c,2)} C')
    F = F + 20

print('**********************')

print('Z pętlą for')
F_range = list(range(0,220,20))
for F in F_range:
    c = 5/9 * (F - 32)
    print(f'{F} F -> {round(c,2)} C')



# podsumowujące nr 3
# jedna z 2 gier