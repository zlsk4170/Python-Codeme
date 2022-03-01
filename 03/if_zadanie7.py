# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

waga = int(input('Podaj swoją wagę w kg: '))
wzrost = int(input('Podaj swój wzrost w cm: '))/100

BMI = waga /(wzrost **2)
print(f'Twoje BMI wynosi: {round(BMI,2)}')

if BMI < 18.5:
    print('niedowaga')
elif 25 <= BMI <= 30:
    print(nadwaga)
elif BMI > 30:
    print('otyłość')
else:
    print('Twoje BMI jest prawidłowe')