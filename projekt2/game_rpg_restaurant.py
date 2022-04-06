import name_generator as hero, random, json

class Player():

    def __init__(self,user_name,products,results):
        self.user_name = user_name
        self.products = products
        self.results = results

    def show_mission(self,user_name):
        print()
        print(f'{user_name} took a job position as a cook in an average New York restaurant.')
        print('Your manager fully trusts you. He gave you 1000USD budget to start your job.')
        print('Check the products available in the restaurant, if needed, go for shopping and cook meals for your clients.')
        print('Try to balance the budget, increase the prestige of your restaurant and do not loose trust of your manager.')
        print('If something goes wrong...you may be fired!')
        print()

    def take_action(self):
        while True:
            print('Select the action: ')
            print('1 -> check available products')
            print('2 -> go for shopping')
            print('3 -> cook a meal')
            print('4 -> enroll to a training')
            print('5 -> show current score')
            print('0 -> go to main menu')
            try:
                user_choice = int(input())
                if user_choice == 1:
                    return 1
                elif user_choice == 2:
                    print('Time to do some shopping.')
                    return 2
                elif user_choice == 3:
                    return 3
                elif user_choice == 4:
                    return 4
                elif user_choice == 5:
                    return 5
                elif user_choice == 0:
                    print('You are in the main menu.')
                    return 0
                else:
                    raise ValueError
            except ValueError:
                print('Wrong input. Give a number.')

    def show_products(self,user_name,products):
        self.products = products
        print(f'Products left: {products}')
        while True:
            print('1 - go for shopping')
            print('0 - return to previous menu')
            try:
                user_choice = int(input())
                if user_choice == 1:
                    print(f'{user_name} decided to do some shopping.')
                    return 1
                if user_choice == 0:
                    print('Return to the previous menu:')
                    return 0
                else:
                    raise ValueError
            except ValueError:
                print('Wrong input. Select the value from list.')

    def do_shopping(self, user_name):
        while True:
            print(f'Where should {user_name} buy products?')
            print('1 - go to fresh market')
            print('2 - go to the big store')
            print('0 - return to previous menu')
            try:
                user_choice = int(input())
                if user_choice == 1:
                    print(f'{user_name} is going to buy food directly from farmers.')
                    return 1
                elif user_choice == 2:
                    print(f'{user_name} is going to the big food store.')
                    return 2
                elif user_choice == 0:
                    print('Return to the previous menu:')
                    return 0
                else:
                    raise ValueError
            except ValueError:
                print('Wrong input. Select the value from list.')

    def buy_from_farmers(self,user_name):
        while True:
            print(f'The farmer says: "Hello {user_name}. How can I help you?"')
            print('1 - buy 10 pieces of vegetables [10 USD}')
            print('2 - buy 10 pieces of meat [50 USD]')
            print('0 - that\'s all, thank you')
            try:
                user_choice = int(input())
                if user_choice == 1:
                    print('Your boss says: "You spent too much money! Next time go to the supermarket!')
                    print('Boss satisfaction: -10')
                    return 1,10,10,'VEGETABLES',-10
                elif user_choice == 2:
                    print('Your boss says: "You spent too much money! Next time go to the supermarket!')
                    print('Boss satisfaction: -10')
                    return (2,10,50,'MEAT',-10)
                elif user_choice == 0:
                    print('Return to the previous menu:')
                    return (0,0,0,0,0)
                else:
                    raise ValueError
            except ValueError:
                print('Wrong input. Select the value from list.')

    def buy_from_store(self,user_name):
        while True:
            print(f'{user_name} came into a big supermarket."')
            print('1 - buy 10 pieces of vegetables [5 USD}')
            print('2 - buy 10 pieces of meat [40 USD]')
            print('0 - that\'s all thank you')
            try:
                user_choice = int(input())
                if user_choice == 1:
                    print('Your boss says: "You spent less money then I expected. Good job!"')
                    print('Boss satisfaction: +5')
                    return 1,10,5,'VEGETABLES',5
                elif user_choice == 2:
                    print('Your boss says: "You spent less money then I expected. Good job!"')
                    print('Boss satisfaction: +5')
                    return 2,10,40,'MEAT',5
                elif user_choice == 0:
                    print('Return to the previous menu:')
                    return 0,0,0,0,0
                else:
                    raise ValueError
            except ValueError:
                print('Wrong input. Select the value from list.')


    def buy_product(self,farm,amount,cost,product_name,satisfaction_value):
        self.farm = farm
        self.products[product_name] += amount
        self.results["MONEY"] -= cost
        self.results["SATISFACTION"] += satisfaction_value


    def select_meal(self):
        meal = ["Beef with vegetables","Hamburger","Vege plate"]
        random_meal = random.choice(meal)
        print(f'Your client ordered: {random_meal}')
        if random_meal == meal[0]:
            print('Vegetables used: 20, Meat used: 20')
            return ('VEGETABLES','MEAT',-20,-20)
        elif random_meal == meal[1]:
            print('Vegetables used: 0, Meat used: 20')
            return ('VEGETABLES','MEAT',0,-20)
        elif random_meal == meal[2]:
            print('Vegetables used: 30, Meat used: 0')
            return ('VEGETABLES','MEAT',-30,0)


    def prepare_meal(self,product_name1,product_name2,amount1,amount2):
        self.products[product_name1] += amount1
        self.products[product_name2] += amount2


    def generate_client_satisfaction(self):
        random_satisfaction = random.randint(1,100)
        if random_satisfaction < 50:
            print('Client paid the bill, but he did not like your meal. Your boss is angry!')
            print('Money earned: +20, Boss satisfaction: -30, Restaurant rate: -20')
            return (20,-30,-20)
        else:
            print('Client paid the bill and he enjoyed the meal. He gave you extra tip. Your boss is happy!')
            print('Money earned: +30, Boss satisfaction: +10, Restaurant rate: +10')
            return (30,10,10)


    def calculate_round_result(self,bill,satisfaction_level,client_grade):
        self.results["MONEY"] += bill
        self.results["SATISFACTION"] += satisfaction_level
        self.results["GRADE"] += client_grade
        print('1 - return to previous menu')
        while True:
            try:
                user_choice = int(input())
                if user_choice == 1:
                    print('Return to the previous menu:')
                    return 1
                else:
                    raise ValueError
            except ValueError:
                print('Wrong input. Select the value from list.')


    def go_for_training(self):
        self.results["SATISFACTION"] += -20
        self.results["GRADE"] += 20
        print(f'Your cook decided to take additional training')
        print('Restaurant was closed for 1 week. Your boss was angry, but your clients are happy.')
        print('Boss satisfaction: -20, Restaurant rate: +20')
        print('1 - return to previous menu')
        while True:
            try:
                user_choice = int(input())
                if user_choice == 1:
                    print('Return to the previous menu:')
                    return 1
                else:
                    raise ValueError
            except ValueError:
                print('Wrong input. Select the value from list.')

    def show_current_results(self,products,results,name):
        self.products = products
        self.results = results
        print('****************************************************************')
        print(f'Products left: {products}')
        print(f'Current score: {results}')
        print('****************************************************************')
        if products['VEGETABLES'] <= 0 or products['MEAT'] <=0:
            print(f'Your cook {name} used all products!')
            print('GAME OVER')
            return
        if results['MONEY'] <= 0:
            print(f'Your cook {name} have no money left!')
            print('GAME OVER')
            return
        if results['SATISFACTION'] <= 0:
            print(f'Your cook {name} dissapointed your boss!')
            print('GAME OVER')
            return
        if results['GRADE'] <= 0:
            print(f'Your cook {name} ruined restaurant reputation!')
            print('GAME OVER')
            return
        while True:
            try:
                print('1 - save results')
                print('0 - return to previous menu')
                user_choice = int(input())
                if user_choice == 1:
                    return 1
                if user_choice == 0:
                    return 0
                else:
                    raise ValueError
            except ValueError:
                print('Wrong input. Select the value from list.')




def main_menu():
    while True:
        print('Select the number: ')
        print('1 -> start new game')
        print('2 -> load results')
        print('0 -> quit game')
        try:
            user_choice = int(input())
            if user_choice == 1:
                return 1
            if user_choice == 2:
                return 2
            elif user_choice == 0:
                print('GAME OVER')
                return 0
            else:
                raise ValueError
        except ValueError:
            print('Wrong input. Give a number.')

def load_results():
    with open('results.txt') as file:
        line1 = file.readline().strip('\n').replace('\'','\"')
        line2 = file.readline().strip('\n').replace('\'','\"')
        js1 = json.loads(line1)
        js2 = json.loads(line2)
        print('Results loaded from the file')
        return js1["VEGETABLES"], js1["MEAT"], js2["MONEY"], js2["SATISFACTION"], js2["GRADE"]

def save_results(products,results):
    with open('results.txt','w') as file:
        file.write(str(f'{products} \n'))
        file.write(str(f'{results}'))
        print('Results save to a file: results.txt')


def algorythm(results,products):
    name = hero.generate_name()
    cook = Player(name,products,results)
    cook.show_mission(name)
    while True:
        action = cook.take_action()
        if action == 1:
            show_prod = cook.show_products(name,products)
            while True:
                if show_prod == 1:
                    do_shop = cook.do_shopping(name)
                    if do_shop == 1:
                        farm,amount,cost,product_name,satisfaction_value = cook.buy_from_farmers(name)
                        if farm == 1:
                            cook.buy_product(farm,amount,cost,product_name,satisfaction_value)
                            continue
                        if farm == 2:
                            cook.buy_product(farm,amount,cost,product_name,satisfaction_value)
                            continue
                        if farm == 0:
                            break
                    if do_shop == 2:
                        farm,amount,cost,product_name,satisfaction_value = cook.buy_from_store(name)
                        if farm == 1:
                            cook.buy_product(farm,amount,cost,product_name,satisfaction_value)
                        if farm == 2:
                            cook.buy_product(farm,amount,cost,product_name,satisfaction_value)
                        if farm == 0:
                            break
                if show_prod == 0:
                    break
        if action == 2:
            while True:
                do_shop = cook.do_shopping(name)
                if do_shop == 1:
                    farm,amount,cost,product_name,satisfaction_value = cook.buy_from_farmers(name)
                    if farm == 1:
                        cook.buy_product(farm,amount,cost,product_name,satisfaction_value)
                    if farm == 2:
                        cook.buy_product(farm,amount,cost,product_name,satisfaction_value)
                    if farm == 0:
                        break
                if do_shop == 2:
                    farm,amount,cost,product_name,satisfaction_value = cook.buy_from_store(name)
                    if farm == 1:
                        cook.buy_product(farm,amount,cost,product_name,satisfaction_value)
                    if farm == 2:
                        cook.buy_product(farm,amount,cost,product_name,satisfaction_value)
                    if farm == 0:
                        break
                if do_shop == 0:
                    break
        if action == 3:
            product_name1,product_name2,amount1,amount2 = cook.select_meal()
            cook.prepare_meal(product_name1,product_name2,amount1,amount2)
            bill,satisfaction_level,client_grade = cook.generate_client_satisfaction()
            round = cook.calculate_round_result(bill,satisfaction_level,client_grade)
            if round == 1:
                continue
        if action == 4:
            train = cook.go_for_training()
            if train == 1:
                continue
        if action == 5:
            show = cook.show_current_results(products,results,name)
            if show == 1:
                save_results(products,results)
                continue
            if show == 0:
                continue
            break
        if action == 0:
            break


def main():
    while True:
        main = main_menu()
        if main == 1:
            results = {"MONEY":1000,"SATISFACTION": 100,"GRADE":50}
            products = {"VEGETABLES":10,"MEAT":10}
            algorythm(results,products)
        if main == 2:
            vege,meat,budget,satisf,rate = load_results()
            results = {"MONEY":budget,"SATISFACTION": satisf,"GRADE":rate}
            products = {"VEGETABLES":vege,"MEAT":meat}
            algorythm(results,products)
            continue
        if main == 0:
            break

if __name__ == "__main__":
    main()
