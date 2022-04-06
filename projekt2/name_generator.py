import random

def generate_name():
    print('How would you like to define a name of your hero?')
    print('1 - my own choice')
    print('2 - random choice')
    while True:
        try:
            user_choice = int(input())
            if user_choice == 1:
                print('Give the name:')
                user_name = input()
                print(f'Your name is: {user_name}')
                return user_name
            if user_choice == 2:
                while True:
                    print('Select sex: [M/F]')
                    try:
                        sex = input()
                        sex = sex.upper()
                        if sex == 'M':
                            name_male_random = ['Cook John','Cook Zumg Yann','Cook Lao Phy']
                            user_name = random.choice(name_male_random)
                            print(f'Your name is: {user_name}')
                            return user_name
                        if sex == 'F':
                            name_female_random = ['Cook Anne','Cook Melanie','Cook Elizabeth']
                            user_name = random.choice(name_female_random)
                            print(f'Your name is: {user_name}')
                            return user_name
                        else:
                            raise ValueError
                    except ValueError:
                        print('Wrong input')
            else:
                raise ValueError
        except ValueError:
            print('Wrong value. Select the number from the list')

if __name__ == "__main__":
    main()