'''Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową.
Użyj funkcji format(), by wyświetlić zdanie zawierające te wartości.'''


num = input('Podaj liczbę: ')
txt = input('Podaj tekst: ')

print('Oto zdanie zawierające Twój tekst: "{0}" i Twoją liczbę: "{1}"'.format(txt,num))
print(f'Oto Twój tekst "{txt}" i liczba "{num}"')