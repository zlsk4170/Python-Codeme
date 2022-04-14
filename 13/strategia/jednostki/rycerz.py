#ETAP 1:
# Stwórz klasę Rycerz o następujących cechach:
# Klasa posiada dwa atrybuty:
#    zycie ustawione przy inicjalizacji na 60
# doswiadczenie ustawione przy inicjalizacji na 0
# Klasa posiada zaimplementowaną metodę __repr__, która zwróci tekst: ‘Rycerz: hp=(zycie), exp=(doswiadczenie)’
# Klasa posiada metodę maszeruj, która:
# przyjmuje jeden argument: dystans (dystans w metrach, który przebył Rycerz)
# wypisze na ekran komunikat 'Rycerz: Przeszedłem (liczba) m'
# Rycerz za każdy metr, który przeszedł, dostaje 0.2 punktu doświadczenia. Metoda ma dodać do doświadczenia rycerza odpowiednią liczbę punktów.
# Klasa posiada metodę atakuj, która:
# wypisze na ekran komunikat: 'Rycerz: Machnąłem mieczem!'
# doda Rycerzowi 0.3 punktu doświadczenia za jego ruch
# Przetestuj napisany kod:
# Utwórz blok if __name__ == '__main__': i kolejne wyrażenia pisz w jego wnętrzu
# Stwórz obiekt klasy Rycerz i wyświetl
# Wydaj rozkaz maszerowania, a następnie ataku
# Ponownie wyświetl Rycerza na ekran

class Rycerz():
    def __init__(self):
        self.zycie = 60
        self.doswiadczenie = 0

    def __repr__(self):
        return f'Rycerz: hp = {self.zycie}, exp = {self.doswiadczenie}'

    def maszeruj(self,dystans):
        print(f'Przeszedłem {dystans}m')
        self.doswiadczenie += dystans * 0.2

    def atakuj(self):
        print('Machnąłem mieczem!')
        self.doswiadczenie += 0.3