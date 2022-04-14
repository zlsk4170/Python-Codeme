#ETAP 2
# Stwórz klasę Lucznik kopiując klasę Rycerz i wklejając ją poniżej.
# Następnie wprowadz w skopiowanej klasie następujące modyfikacje:
# Łucznik zaczyna z mniejszą ilością punktów życia: 40 zamiast 60.
# We wszystkich komunikatach zamiast 'Rycerz' wpisz 'Łucznik'.
# Metoda atakuj ma wypisywać komunikat 'Łucznik: Wypuściłem strzałę!' a wypuszczenie strzały ma dodawać Łucznikowi 0.4 punktu doświadczenia.
# Przetestuj działanie tej klasy podobnie, jak to miało miejsce przy klasie Rycerz.
# Rozszerzenie (opcjonalne): Łucznik ma ograniczoną ilość strzał w kołczanie.
# Dodaj do klasy odpowiedni atrybut, a następnie zmodyfikuj funkcję atakuj tak, aby Łucznik z każdym strzałem tracił jedną strzałę.
# Gdy strzały się skończą, uniemożliw strzelanie i zmień komunikat.

class Lucznik():
    def __init__(self):
        self.zycie = 40
        self.doswiadczenie = 0
        self.strzaly = 1

    def __repr__(self):
        return f'Lucznik: hp = {self.zycie}, exp = {self.doswiadczenie}'

    def maszeruj(self,dystans):
        print(f'Przeszedłem {dystans}m')
        self.doswiadczenie += dystans * 0.2

    def atakuj(self):
        if self.strzaly > 0:
            self.doswiadczenie += 0.4
            self.strzaly -= 10
            print('Wypuściłem strzałę!')

        else:
            print('Lucznik nie mógł oddać strzału, bo nie ma już wolnych strzał')
