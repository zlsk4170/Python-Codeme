print('Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron')

title = input('Podaj tytuł książki: ')
author = input('Podaj nazwisko autora: ')
pages = input('Podaj liczbe stron: ')
print()

print('* Sprawdź czy tytuł i nazwisko składają się tylko z liter -> ', title.isalpha() and author.isalpha())
print('* Sprawdź czy liczba stron jest wartością liczbową -> ',pages.isdigit())
print()

print('* Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich')
print(title.capitalize())
print(author.capitalize())
print()

print('* Połącz dane w jeden ciąg book za pomocą spacji')
book = title.capitalize() + ' ' + author.capitalize() + ' ' + pages
print(book)
print()

print('* Policz liczbę wszystkich znaków w napisie book')
print('Liczba wszystkich znaków w napisie book wynosi ->', len(book))