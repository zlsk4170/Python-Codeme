# Based on a user's order, work out their final bill.
# Small pizza: 15$
# Medium pizza: 20$
# Large pizza: 25$
# Pepperoni for Small Pizza: +2$
# Pepperoni for Medium or Large Pizza: +3
# Extra cheese for any size pizza: +1
#
# Your final bill is: X$

pizza = {
    's':15,
    'm':20,
    'l':25
}

pepperoni = {
    'small':2,
    'other':3,
}

extra_cheese = {
    'y':1,
    'n':0
}

while True:
    size = input('Select the size of pizza [s/m/l] -> ')
    if size in pizza.keys():
        pizza_cost = pizza[size]
        break
    print('Wrong value given')
    continue


while True:
    add_pepp = input('Would you like to add extra pepperoni? [y/n] -> ')
    if add_pepp == 'n':
        pepperoni_cost = 0
        break
    if add_pepp == 'y':
        if size == 's':
            pepperoni_cost = pepperoni['small']
            break
        if size =='m' or 'l':
            pepperoni_cost = pepperoni['other']
            break
    print('Wrong value given')
    continue


while True:
    cheese = input('Would you like to add extra cheese? [y/n] -> ')
    if cheese in extra_cheese.keys():
        cheese_cost = extra_cheese[cheese]
        break
    print('Wrong value given')
    continue

bill = pizza_cost + pepperoni_cost + cheese_cost

print(f'Your final bill is: {bill}$')