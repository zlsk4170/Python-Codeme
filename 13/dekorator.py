def stars_decorator(function_as_param): #dekorator to funkcja która jako parametr przyjmuje inną funkcję, wczesniej mielismy txt teraz mamy funkcje

    def inside_function():
        print('*'* 20)
        print(function_as_param().center(20))
        print('*'* 20)

    return inside_function


def quote_generator(): # to bedzie wnetrze naszej funkcji wewnetrznej
    return 'Mądry cytat'

@stars_decorator #tym wskazujemy że ta funkcja ma przejść przez dekorator, będziemy mogli wywołać bezpośrednio przez tę funkcję
def daily_news():
    return 'breaking news'



quote = stars_decorator(quote_generator) # podajemy nazwe funkcji jako parametr, dostajemy jako wynik tej funkcji nazwe funkcji zagniezdzonej
quote() # teraz wykonujemy funkcje zagniezdzona

# news = stars_decorator(daily_news)
# news()

daily_news() # dzięki @stars_decorator możemy od razu wywołać tą samą funkcję zamiast pisać tego co powyżej