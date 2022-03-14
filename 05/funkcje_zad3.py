# Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c)

def maximum_of(a,b,c):
    zestaw = [a,b,c]
    maximum = zestaw[0]
    for i in range(len(zestaw)):
        if zestaw[i] > maximum:
            maximum = zestaw[i]
    return maximum

print(maximum_of(23,332,4))