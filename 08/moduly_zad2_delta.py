# Stwórz moduł, który przechowuje wzór na deltę.
# Skorzystaj z wbudowanego modułu math.
# W nowym pliku wykorzystaj moduł.

import moduly_delta as delta

def main():

    b = float(input('Give "b" value: '))
    a = float(input('Give "a" value: '))
    c = float(input('Give "c" value: '))

    delta_value = delta.calculate_delta(b,a,c)
    return print(f'Delta is equal: ',round(delta_value,2))

main()

if __name__ == '__main__':
    main()