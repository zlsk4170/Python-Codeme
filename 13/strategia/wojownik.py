#ETAP 3
# Klasy Rycerz i Lucznik to wojownicy.
# Stwórz klasę Wojownik, z której będą dziedziczyć klasy Rycerz oraz Lucznik.
# Klasa bazowa posiada zaimplementowaną metodę __repr__, która zwróci tekst: 'Wojownik: hp=(zycie), exp=(doswiadczenie)'
# Klasa bazowa posiada metodę maszeruj, która wypisze na ekran komunikat Wojownik: Przeszedłem (liczba) m'


class Wojownik(Rycerz,Lucznik):
    def __init__(self):
        self.doswiadczenie = 0

    def __repr__(self):
        name = self.__class__.__name__
        return f'Wojownik {name}: hp = {self.zycie}, exp = {self.doswiadczenie}'

    def maszeruj(self,dystans):
        name = self.__class__.__name__
        self.doswiadczenie += dystans * 0.2
        print(f'{name}: Przeszedłem {dystans}m')

