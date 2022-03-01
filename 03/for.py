txt = 'kot'

for letter in txt:
    print('-',letter)
    # print('-', end='')


list = ['Adam','Jan','Kasia']
for item in list:
    print('Hello',item)

for item in range(2,10,2):
    print("krok", item)


list = ['Ala', 'Julia', 'Rubi']
for index in range(3):
    print(index,':',list[index])


txt = "string"
for letter in txt:
    if letter == 'i':
        break
    print(letter)
print('Jestem poza pętlą')

txt = "string"
for letter in txt:
    if letter == 'i':
        continue
    print(letter)
print('Jestem poza pętlą')