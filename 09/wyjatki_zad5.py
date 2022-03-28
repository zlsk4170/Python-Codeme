# W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
# Co jeśli użytkownik poda wartość 60 kg ?
# Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.

import module_bmi as bmi

def dane():
    while True:
        try:
            weight = float(input('Podaj swoją wagę w kg: '))
            height = float(input('Podaj swój wzrost w cm: '))/100
        except: #jeżeli pojawi się błąd wraca na początek pętli
            print('Podaj liczbę')

        else: #jeżeli nie ba błędu idzie dalej
            if weight > 598 or height > 2.08:
                raise ValueError('Nieprawdopodobne wartości') #wywoła błąd
            return weight, height #return kończy funkcję, nie wraca już na początek pętli

def show_advice(message):
    filename = str(message) + '.txt'
    with open(filename,encoding='utf-8') as file:
        print(file.read())

def main():
    while True:
        try:
            w,h = dane()
        except ValueError as error: #jeżeli pojawi się błąd wraca na początek pętli
            print(error)
        else: # gdy nie ma błędu wykona:
            value = bmi.bmi_value(w,h)
            message = bmi.check_bmi(value)
            print(message)
            show_advice(message)
            break #gdyby nie było break to powrót na początek pętli

if __name__ == '__main__':
    main()