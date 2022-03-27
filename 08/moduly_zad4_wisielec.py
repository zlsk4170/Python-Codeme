# Stwórz grę wisielec “bez wisielca”.
# Komputer losuje wyraz z dostępnej w programie listy wyrazów.
# Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
# Użykownik podaje literę.
# Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
# “Trafione!” oraz napis ze znanymi literami.
# W przeciwnym wpadku pokaż komunikat:
# “Nie trafione, spróbuj jeszcze raz!”.
# Możesz ograniczyć liczbę prób do np. 10.


import module_wisielec as wisielec

def main():
    random_word = wisielec.give_random_word()
    hidden_word = wisielec.hide_random_word(random_word)
    max_rounds = wisielec.give_nb_of_rounds()
    message_you_won = wisielec.show_you_won()
    message_you_lost = wisielec.show_you_lost(random_word)
    wisielec.game_engine(max_rounds,random_word,hidden_word,message_you_won,message_you_lost)


if __name__ == "__main__":
    main()