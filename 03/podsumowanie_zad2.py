# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt = input('Wpisz cokolwiek: ')

# zakładam parzystość pozycji liczb z punktu widzenia użytkownika, a nie programisty

print('*******with string slicing******')
even = txt[1::2]
print(even)

print('*******with for loop*******')
for index,letter in enumerate(txt):
    if index%2 != 0:
        print(letter,end='')

