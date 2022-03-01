# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

txt = input('Podaj ciąg znaków o długości > 5: ')
if len(txt) > 5:
    if 'a' in txt:
        txt1 = txt.replace('a','z')
        print(txt1)
else:
    print('Ciąg znaków jest za krótki')