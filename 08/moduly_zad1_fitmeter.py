# Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py. Zaimportuj module do pliku moduly_zad1_fitmeter.py.
# Nowy plik będzie informował użytkownika o jego aktualnym BMI i na podstawie wyniku (niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.
# Utwórz plik bmi.py zawierający metodę obliczania bmi. Metoda zwraca wartości: niedowaga, waga normalna, nadwaga, otyłość.
# Utwórz 4 pliki .txt zawierające porady.
# Utwórz plik moduly_zad1_fitmeter.py, który zaimportuje moduł bmi.
# moduly_zad1_fitmeter.py pobierze wagę i wzrost pacjenta i przekaże do odpowiedniej funkcji z modułu bmi.
# Na podstawie zwróconej wartości moduly_zad1_fitmeter.py wyświetli odpowiednie porady dla pacjenta

import moduly_zad1_bmi as bmi

def dane():
    weight = int(input('Podaj swoją wagę w kg: '))
    height = int(input('Podaj swój wzrost w cm: '))/100
    return weight, height

def show_advice(message):
    filename = str(message) + '.txt'
    with open(filename,encoding='utf-8') as file:
        print(file.read())

def main():
    w,h = dane()
    value = bmi.bmi_value(w,h)
    message = bmi.check_bmi(value)
    print(message)
    show_advice(message)

if __name__ == '__main__':
    main()
