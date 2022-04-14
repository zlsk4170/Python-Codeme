class Account():
    def __init__(self,name):
        self.name = name
        self.__account = '11111' #oznacza atrybut prywatny


client = Account('Jan')
print(client.__account) #nie zadziała bo prywatny

# parametr prywatny można zmienić tylko poprzez funkcję