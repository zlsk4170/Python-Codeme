# Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
# W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
# ponownie wyświetl zmieniony słownik
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.



def display_car():
    print(car)

def isold():
    age = 2022 - int(car['rocznik'])
    oryginal = car['czy_oryginalny']
    if age < 25:
        print('Twój samochód', car['marka'], car['model'], 'jest jeszcze zbyt młody')
    if oryginal==False:
        print('Twój samochód', car['marka'], car['model'], 'ma zbyt mało oryginalnych części')
    if age >=25 and oryginal == True:
        print('Gratulacje! Twój samochód', car['marka'], car['model'], 'może być zarejestrowany jako zabytek.')


def modify_year(year):
    car['rocznik'] = year

def add_original(bool):
    car.update({'czy_oryginalny':bool})


car = {
    'marka':'Ford',
    'model':'Mondeo',
    'rocznik':1990
}

modify_year(2000)
add_original(False)
display_car()
isold()