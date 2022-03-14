# Nie korzystając z funkcji wbudowanej min(),
# napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

def minimum_of(a,b,c):
    zestaw = [a,b,c]
    minimum = zestaw[0]
    for i in range(len(zestaw)):
         if zestaw[i] < minimum:
            minimum = zestaw[i]
    return minimum

wynik = minimum_of(23,332,4)
print(wynik)