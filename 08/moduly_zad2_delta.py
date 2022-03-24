import moduly_delta as delta

def give_delta():

    b = float(input('Give "b" value: '))
    a = float(input('Give "a" value: '))
    c = float(input('Give "c" value: '))

    delta_value = delta.calculate_delta(b,a,c)
    return print(f'Delta is equal: ',round(delta_value,2))

give_delta()