def check_bmi(bmi):
    if bmi < 18.5:
        return 'niedowaga'
    elif 25 <= bmi <= 30:
        return 'nadwaga'
    elif bmi > 30:
        return 'otyłość'
    else:
        return 'ok'

def bmi_value(weight,height):
    bmi = weight/(height **2)
    print(f'Twoje bmi wynosi', round(bmi,2))
    return bmi

