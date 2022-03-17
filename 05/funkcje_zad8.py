# Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
# Program zacznie ze stworzonym słownikiem o trzech kluczach:
    # marka (str)
    # model (str)
    # rocznik (int)
# Wypisze ten słownik na ekran (bez żadnego formatowania)
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.


def display_car():
    print(car)

def isold():
    if 2022 - int(car['rocznik']) > 25:
        print('Gratulacje! Twój samochód', car['marka'], car['model'], 'może być zarejestrowany jako zabytek.')
    else:
        print('Twój samochód', car['marka'], car['model'], 'jest jeszcze zbyt młody')

def modify_year(year):
    car['rocznik'] = year


car = {
    'marka':'Ford',
    'model':'Mondeo',
    'rocznik':1990
}

display_car()
isold()

modify_year(2000)

display_car()
isold()