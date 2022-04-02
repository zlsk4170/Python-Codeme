import random

def main_menu():
    while True:
        print('Select the number: ')
        print('1 -> start new game')
        print('2 -> save game')
        print('3 -> quit game')
        try:
            user_choice = int(input())
            if user_choice == 1:
                print('Let\'s go!')
                return define_hero()
            elif user_choice == 2:
                print('Game saved')
                return 2
            elif user_choice == 3:
                print('GAME OVER')
                break
            else:
                raise ValueError
        except ValueError:
            print('Wrong input. Give a number.')

def define_hero():
    while True:
        print('How would you like to define a name of your hero?')
        print('1 - my own choice')
        print('2 - random choice')
        try:
            user_choice = int(input())
            if user_choice == 1:
                print('Give the name:')
                user_name = input()
                print(f'Your name is: {user_name}')
                intro(user_name)
                return user_name
            if user_choice == 2:
                while True:
                        print('Select sex: [M/F]')
                        try:
                            sex = input()
                            sex = sex.upper()
                            if sex == 'M':
                                name_male_random = ['Cook John','Cook Zumg Yann']
                                user_name = random.choice(name_male_random)
                                print(f'Your name is: {user_name}')
                                intro(user_name)
                                return user_name
                            if sex == 'F':
                                name_female_random = ['Cook Anne','Cook Melanie']
                                user_name = random.choice(name_female_random)
                                print(f'Your name is: {user_name}')
                                intro(user_name)
                                return user_name
                            else:
                                raise ValueError
                        except ValueError:
                            print('Wrong input')

            else:
                raise ValueError
        except ValueError:
            print('Wrong value. Select the number from the list')


def intro(user_name):
    print()
    print(f'{user_name} took a job position as a cook in an average New York restaurant.')
    print('Your manager fully trusts you. He gave you 1000USD budget to start your job.')
    print('Check the products available in the restaurant, if needed, go for shopping and cook meals for your clients.')
    print('Try to balance the budget, increase the prestige of your restaurant and do not loose trust of your manager.')
    print('If something goes wrong...you may be fired!')
    print()
    menu1(user_name)

def result(user_name):
    budget = 1000
    trust = 100
    prestige = 50
    print('*****************************************')
    print(f'BUDGET = {budget}, TRUST = {trust}, PRESTIGE = {prestige}')
    print('*****************************************')
    while True:
        print('1 - return to previous menu')
        try:
            user_choice = int(input())
            if user_choice == 1:
                print('Return to the previous menu:')
                menu1(user_name)
                return budget, trust, prestige
            else:
                raise ValueError
        except ValueError:
            print('Wrong input. Select the value from list.')



def menu1(user_name):
    while True:
        print('Select the action: ')
        print('1 -> check available products')
        print('2 -> go for shopping')
        print('3 -> cook a meal')
        print('4 -> enroll to a training')
        print('5 -> show result')
        print('0 -> go to main menu')
        try:
            user_choice = int(input())
            if user_choice == 1:
                print(f'{user_name} is verifying available products.')
                storage(user_name)
                return 1
            elif user_choice == 2:
                print('Time to do some shopping.')
                shopping(user_name)
                return 2
            elif user_choice == 3:
                print('Time to get the orders and cool some meal for your clients.')
                return 3
            elif user_choice == 4:
                print('Time to learn how to cook better.')
                return 4
            elif user_choice == 5:
                print('These are your current results.')
                result(user_name)
                return 5
            elif user_choice == 0:
                print('Let\'s go to the main menu.')
                main_menu()
                break
            else:
                raise ValueError
        except ValueError:
            print('Wrong input. Give a number.')

def storage(user_name):
    vegetable = 0
    meat = 0
    fish = 0
    dairy = 0
    spices = 0
    drink = 0
    products = [f'VEGETABLES = {vegetable}, MEAT = {meat}, FISH = {fish}, DAIRY = {dairy}, SPICES = {spices}, DRINKS = {drink}']
    print(products)
    while True:
        print(f'What would you like {user_name} to do next?')
        print('1 - go for shopping')
        print('0 - return to previous menu')
        try:
            user_choice = int(input())
            if user_choice == 1:
                print(f'{user_name} decided to do some shopping.')
                shopping(user_name)
                # return 1
            elif user_choice == 0:
                print('Return to the previous menu:')
                menu1(user_name)
                # return 0
            else:
                raise ValueError
        except ValueError:
            print('Wrong input. Select the value from list.')

        return (vegetable,meat,fish,dairy,spices,drink)

def shopping(user_name):
    while True:
        print(f'Where should {user_name} buy products?')
        print('1 - go to fresh market')
        print('2 - go to the big store')
        print('0 - return to previous menu')
        try:
            user_choice = int(input())
            if user_choice == 1:
                print(f'{user_name} is going to buy food directly from farmers.')
                shopping_farmers(user_name)
                return 1
            elif user_choice == 2:
                print(f'{user_name} is going to the big food store.')
                shopping_store()
                return 2
            elif user_choice == 0:
                print('Return to the previous menu:')
                menu1(user_name)
                return 0
            else:
                raise ValueError
        except ValueError:
            print('Wrong input. Select the value from list.')

def shopping_farmers(user_name):
    while True:
        print(f'The farmer says: "Hello {user_name}. How can I help you?"')
        print('1 - buy 10 pieces of vegetables [10 USD}')
        print('2 - buy 10 pieces of meat [50 USD]')
        print('3 - buy 10 pieces of fish [60 USD]')
        print('4 - buy 10 pieces of dairy [30 USD]')
        print('5 - buy 10 pieces of spices [20 USD]')
        print('6 - buy 10 bottles of juice [20 USD]')
        print('0 - that\'s all thank you')
        try:
            user_choice = int(input())
            if user_choice == 1:
                return buy_vege_farmers()
            elif user_choice == 2:
                return 2
            elif user_choice == 3:
                return 3
            elif user_choice == 4:
                return 4
            elif user_choice == 5:
                return 5
            elif user_choice == 6:
                return 6
            elif user_choice == 0:
                print('Return to the previous menu:')
                shopping(user_name)
            else:
                raise ValueError
        except ValueError:
            print('Wrong input. Select the value from list.')


def buy_vege_farmers():
    print('You paid 10 USD for 10 pieces of vegetables.')
    vegetables = 10
    cost = -10
    return vegetables, cost

def main():
    main_menu()

if __name__ == "__main__":
    main()