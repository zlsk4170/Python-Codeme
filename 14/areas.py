def rectangle(a,b):
    # if not (isinstance(a, (int,float)) and isinstance(b, (int,float))):
    #     raise ValueError('Bok musi być wartością numeryczną')
    check(a)
    check(b)
    return a * b
    # try:
    #     if float(a) and float(b):
    #         return a * b
    # except ValueError:
    #     raise ValueError('To nie są liczby')

def triangle(a,h):
    check(a)
    check(h)
    return 0.5 *a*h

def is_account_active():
    #coś tam
    return True

def trapezoid(a,b,h):
    check(a)
    check(b)
    check(h)
    return (a+b)*h//2

def check(value):
    if not isinstance(value, (int,float)):
        raise ValueError('To nie są liczby')