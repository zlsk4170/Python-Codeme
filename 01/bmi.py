waga = int(input('Podaj swoją wagę w kg: '))
wzrost = int(input('Podaj swój wzrost w cm: '))/100

BMI = waga /(wzrost **2)

print(f'Twoje BMI wynosi: {round(BMI,2)}')