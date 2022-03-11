def check_bmi():
    if bmi() < 18.5:
        return print('niedowaga')
    elif 25 <= bmi() <= 30:
        return print('nadwaga')
    elif bmi() > 30:
        return print('otyłość')
    else:
        return 'Twoje BMI jest prawidłowe'

def bmi():
    BMI = weight/(height **2)
    return BMI

weight = int(input('Podaj swoją wagę w kg: '))
height = int(input('Podaj swój wzrost w cm: '))/100
check_bmi()