print()
print('"Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1."')
print()
s1 = input('Podaj pierwszy wyraz: ')
center = int(len(s1)/2)
s2 = input('Podaj drugi wyraz: ')

nowy_wyraz = s1[:center]+s2+s1[center:]
print('Nowy łańcuch zawierający drugi wyraz w środku pierwszego to: ', nowy_wyraz)