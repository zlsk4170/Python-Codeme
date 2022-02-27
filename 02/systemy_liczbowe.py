# Na kartce papieru oblicz jak twój wiek będzie reprezentowany binarnie. Sprawdź czy to samo zwróci Python.

print('Mój wiek w zapisie binarnym wynosi: ', bin(45))

'''
Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym. 
Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).
'''
bin = 1001111
string_bin = str(bin)

decimal = (int(string_bin[-1]))*2**0 + (int(string_bin[-2]))*2**1 + (int(string_bin[-3]))*2**2 + (int(string_bin[-4]))*2**3 + (int(string_bin[-5]))*2**4 + (int(string_bin[-6]))*2**5 + (int(string_bin[-7]))*2**6
print('Wartość w systemie dziesiętnym dla liczby 1001111 zapisanej w systemie binarnym wynosi: ', decimal)

# Dla liczb hex_num = 1DB i oct_num = 2063 zwróć wartość w systemie dziesiętynym.

hex = 0x1DB
oct = 0o2063
print('Wartość w systemie dziesiętnym dla liczby 0x1DB zapisanej w systemie hex wynosi: ', int(hex))
print('Wartość w systemie dziesiętnym dla liczby 2063 zapisanej w systemie oct wynosi: ',int(oct))