# Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch znaków i zwracający ten sam tekst zmieniony na wielkie litery.
# Utwórz funkcję zwracającą tekst
# Utwórz dekorator przyjujący tę funkcję
# Wywołaj funkcję, by sprawdzić, że decorator działa

def uppercase_decorator(any_function):

    def inside_function():
        txt = any_function().upper()
        print(txt)

    return inside_function

def quote_generator():
    return 'To jest jakiś tekst'

quote = uppercase_decorator(quote_generator)
quote()


def uppercase_decorator(any_function):

    def inside_function():
        txt = any_function().upper()
        print(txt)

    return inside_function

@uppercase_decorator
def quote_generator():
    return 'To jest jakiś tekst'

quote_generator()