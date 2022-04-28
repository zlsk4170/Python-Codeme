import requests
import json
import ui
from termcolor import colored
from mods import credentials
from mods import define_alias

class Netbox():

    def __init__(self):
        self.base_url, self.token = credentials()
        self.headers = {
            'authorization': f'token {self.token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def check_status(self):
        status = requests.get(url=f'{self.base_url}/status/',headers=self.headers,verify=False)
        return status


    def display_main_menu(self):
        while True:
            print(colored('\nSelect the action: ','blue'))
            lista = ['open API docs','display Netbox objects','create new Netbox objects','update Netbox objects','delete Netbox objects','exit']
            enumerate_list = enumerate(lista,1)
            for count,item in enumerate_list:
                print(colored(f'{count} - {item}','blue'))
            try:
                user_choice = int(input())
                if user_choice == 1:
                    url = self.base_url + '/docs/'
                    webbrowser.open(url)
                    continue
                if 1 < user_choice < 6:
                    return user_choice
                if user_choice == 6:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(colored('Wrong value given. Try again.','red'))


    def display_menu_get(self):
        print(colored('Select Netbox object to display:','blue'))
        user_choice,param = define_alias()
        return user_choice, param


    def display_menu_post(self):
        print(colored('New objects are created from the bulk files stored in the folder [data_models].','blue'))
        print(colored('Use existing files or create your own bulk file before executing the POST request.','blue'))
        print(colored('file name example: regions_bulk.json','blue'))
        print(colored('\nSelect Netbox object to create:','blue'))
        user_choice,param = define_alias()
        return user_choice, param


    def display_menu_patch(self):
        print(colored('Objects are updated based on the id files stored in the folder [data_models].','blue'))
        print(colored('Use existing object id files or create your own file before executing the PATCH request.','blue'))
        print(colored('file name example: aa.json','blue'))
        print(colored('\nSelect Netbox object to update:','blue'))
        user_choice,param = define_alias()
        return user_choice, param


    def display_menu_delete(self):
        print(colored('Objects are deleted based on the id files stored in the folder [data_models].','blue'))
        print(colored('Use existing object id files or create your own file before executing the DELETE request.','blue'))
        print(colored('file name example: aa.json','blue'))
        print(colored('\nSelect Netbox object to delete:','blue'))
        user_choice,param = define_alias()
        return user_choice, param


    def get_default(self,selection):
        """
        This function shows objects described in the menu
        """
        self.sub_url = selection
        try:
            req = requests.get(url=f'{self.base_url}{self.sub_url}',headers=self.headers,verify=False)
            if req.status_code == 200:
                print(colored(f'Success! API path used: {selection}','green'))
                results = req.json()['results']
                ui.show_results(selection,results)
                return json.dumps(results,indent=4),req.status_code
            else:
                return colored(f'Something went wrong. Error code: {req.status_code}','red')
        except Exception as error:
            return print(colored(f'{error}','red'))


    def get_custom(self,selection):
        """
        This function shows objects based on user API alias
        """
        self.sub_url = selection
        try:
            req = requests.get(url=f'{self.base_url}{self.sub_url}',headers=self.headers,verify=False)
            if req.status_code == 200:
                results = req.json()['results']
                print(json.dumps(results,indent=4))
                print(colored(f'Success! API path used: {selection}','green'))
                return json.dumps(results,indent=4),req.status_code
            else:
                return colored(f'Something went wrong. Error code: {req.status_code}','red')
        except Exception as error:
            return print(colored(f'{error}','red'))


    def post(self,selection):
        """
        This function creates new objects from JSON file
        """
        self.sub_url = selection

        file_name = input(colored('Give the file name [<object>_bulk]: ','blue'))
        try:
            with open(f'data_models/{file_name}') as file:
                data = json.load(file)
            req = requests.post(url=f'{self.base_url}{self.sub_url}',json=data,headers=self.headers,verify=False)
            if req.status_code == 201:
                return colored(f'Netbox object is successfully created','green')
            else:
                return colored(f'Something went wrong. Error code: {req.status_code}','red')
        except Exception as error:
            return colored(f'{error}','red')


    def patch(self,selection):
        """
        This function updates existing objects with IDs given in the JSON file
        """
        self.sub_url = selection
        file_name = input(colored('Give the JSON file name: ','blue'))
        try:
            with open(f'data_models/{file_name}') as file:
                data = json.load(file)
            req = requests.patch(url=f'{self.base_url}{self.sub_url}',json=data,headers=self.headers,verify=False)
            if req.status_code == 200:
                return colored('\nNetbox object is successfully updated','green')
            else:
                return colored(f'\nSomething went wrong. Error code: {req.status_code}','red')
        except Exception as error:
            return colored(f'{error}','red')


    def delete(self,selection):
        """
        This function deletes existing objects with IDs given in the JSON file
        """
        self.sub_url = selection
        file_name = input(colored('Give the JSON file name: ','blue'))
        try:
            with open(f'data_models/{file_name}') as file:
                data = json.load(file)
            req = requests.delete(url=f'{self.base_url}{self.sub_url}',json=data,headers=self.headers,verify=False)
            if req.status_code == 204:
                return colored('\nNetbox object is successfully deleted','green')
            else:
                return colored(f'\nSomething went wrong. Error code: {req.status_code}','red')
        except Exception as error:
            return colored(f'{error}','red')


    def save(self,data):
        """
        This function allows to save the data to a file
        """
        while True:
            try:
                print(colored('\nSave raw JSON data to file? [y/n]','blue'))
                user_input = input()
                user_input = user_input.lower()
                if user_input == 'y':
                    file_name = input(colored('Define the file name: ','blue'))
                    with open(f'saved_files/{file_name}','w') as file:
                        file.write(data)
                    print(colored(f'Success! Data saved to a file: /saved_files/"{file_name}"','green'))
                    print(colored(f'You are forwarded to the main menu:','blue'))
                    break
                elif user_input == 'n':
                    print(colored(f'You are forwarded to the main menu.','blue'))
                    break
                else:
                    raise ValueError
            except ValueError:
                print(colored('Wrong value given. Try again.','red'))
                continue