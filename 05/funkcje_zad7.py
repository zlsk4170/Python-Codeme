# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą,
# MasterCard, a może AmericanExpress.

# Co wiemy o tych numerach tych kart?
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
# American Express card numbers start with 34 or 37 and have 15 digits.

def card():
    card_length = [13,15,16]
    while True:
        card_number = input('Podaj nr karty: ')
        if card_number.isdigit() and len(card_number) in card_length:
            break
        else:
            print('To nie jest nr karty')
    return card_number

def Visa(card_number):
    if card_number[0] == '4':
        if len(card_number) == 13 or len(card_number) == 16:
            return True
    return False

def MC(card_number):
    if int(card_number[0:2]) in range(51,56) or int(card_number[0:4]) in range(2221,2721) and len(card_number) == 16:
        return True
    return False

def AE(card_number):
    if card_number[0:2] == '34' or card_number[0:2] == '37' and len(card_number) == 15:
        return True
    return False


def result():
    num = card()
    display = {}
    display['AE'] = AE(num)
    display['MC'] = MC(num)
    display['Visa'] = Visa(num)
    print(display)

result()