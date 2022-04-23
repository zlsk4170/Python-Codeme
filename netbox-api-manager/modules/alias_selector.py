from termcolor import colored

def define_alias():
    while True:
        list = ['cables','devices','interfaces','locations','manufacturers','regions','sites','define custom request']
        enumerate_list = enumerate(list,1)
        for count,item in enumerate_list:
            print(colored(f'{count} - {item}','blue'))
        try:
            user_choice = int(input())
            if user_choice == 1:
                return '/dcim/cables/','default'
            elif user_choice == 2:
                return '/dcim/devices/','default'
            elif user_choice == 3:
                return '/dcim/interfaces/','default'
            elif user_choice == 4:
                return '/dcim/locations/','default'
            elif user_choice == 5:
                return '/dcim/manufacturers/','default'
            elif user_choice == 6:
                return '/dcim/regions/','default'
            elif user_choice == 7:
                return '/dcim/sites/','default'
            elif user_choice == 8:
                print(colored('Enter your custom API request in the format: /<model_name>/<parameter>/','blue'))
                print(colored('example: /dcim/sites/','blue'))
                own = input()
                return f'{own}','custom'
            else:
                raise ValueError
        except ValueError:
            print(colored('Wrong value given. Try again.','red'))

