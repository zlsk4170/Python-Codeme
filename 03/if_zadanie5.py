# Stwórz zmienną password.
# Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.


password = input('Podaj hasło składające się z liter i cyfr, przynajmniej jednej dużej i małej litery oraz o długości conajmniej 8 znaków: ')

if len(password) <= 8:
    print('Hasło za krótkie')
elif password.islower():
    print('W haśle brakuje dużej litery')
elif password.isupper():
    print('W haśle brakuje małej litery')
elif password.isalpha():
    print('W haśle brakuje cyfr')
elif password.isdigit():
    print('W haśle brakuje liter')
else:
    print('Hasło prawidłowe')