# Zapytaj użytkownika o numer od 1 do 100,
# jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.

num = int(input('Podaj numer od 1 do 100 -> '))
hidden = 45

if num == hidden:
    print('gratulacje!')
else:
    print('pudło!')