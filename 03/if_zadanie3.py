'''Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry,
ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi
'''

op1 = int(input('Jaka jest Twoja ocena książki? [1-10] '))
op2 = int(input('Jaka jest Twoja ocena książki? [1-10] '))
op3 = int(input('Jaka jest Twoja ocena książki? [1-10] '))

avr = (op1+op2+op3)/3

if avr > 7:
    print('bardzo dobra')
elif 4 < avr >= 7:
    print('przeciętna')
else:
    print('Nie warta uwagi')