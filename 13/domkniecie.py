

def stars_decorator(txt): # txt to parametr

    def inside_function():
        print('*'* 20)
        print(txt.center(20))
        print('*'* 20)
    return inside_function


quote = stars_decorator('Bla bla') # definiujemy parametr który wejdzie w txt
quote()