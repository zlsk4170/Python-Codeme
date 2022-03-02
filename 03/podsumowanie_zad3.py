#W podanym przez użytkownika ciągu wejściowym policz
# wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

txt = input('Wpisz cokolwiek: ')

counter_lower, counter_upper, counter_digit, counter_alnum = 0,0,0,0

for letter in txt:
    if letter.islower():
        counter_lower = counter_lower + 1
    if letter.isupper():
        counter_upper = counter_upper + 1
    if letter.isdigit():
        counter_digit = counter_digit + 1
    if not letter.isalnum():
        counter_alnum = counter_alnum + 1

print('Liczba małych liter =', counter_lower)
print('Liczba dużych liter =', counter_upper)
print('Liczba cyfr =', counter_digit)
print('Liczba znaków specjalnych = ', counter_alnum)

