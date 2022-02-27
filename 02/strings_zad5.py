print('Weryfikacja czy wprowadzone wyrażenie jest palindromem [True/False]')
print()

txt = input('Wprowadź zdanie: ')
lower = txt.lower()
txt_join = lower.replace(' ','')

palindrom = txt_join == txt_join[::-1]
print(palindrom)