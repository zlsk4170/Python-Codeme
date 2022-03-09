# Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
# wypełnioną wynikami mnożenia wiersz × kolumna.

row = list(range(1,11))
column = list(range(1,11))


for item in row:
    for value in column:
        print(item*value, end='\t')
    print()

