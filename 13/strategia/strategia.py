from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik

def main():
    rycerze = []
    lucznicy = []

    for num in range(4):
        rycerz = Rycerz()
        rycerze.append(rycerz)

    print(rycerze)

    for rycerz in rycerze:
        rycerz.maszeruj(2000)

    rycerze.append(Rycerz())

    for rycerz in rycerze:
        rycerz.atakuj()

    print(rycerze)


    for num in range(3):
        lucznik = Lucznik()
        lucznicy.append(lucznik)

    armia = rycerze + lucznicy
    print(armia)

    for wojownik in armia:
        wojownik.atakuj()

    print(armia)

if __name__ == '__main__':
    main()