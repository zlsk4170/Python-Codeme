import sys
import urllib3
from termcolor import colored
from mods import Netbox


def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    print(colored('\nThis programs allows to send API requests to Netbox IPAM and DCIM','blue'))
    nb = Netbox()
    try:
        status = nb.check_status()
        if status.status_code == 200:
            print(colored(f'Connection status with Netbox -> OK','green'))
        elif status.status_code == 403:
            print(colored('\nUnauthorized access attempt','red'))
            sys.exit()
    except Exception:
        print(colored('\nFailed to establish a connection with Netbox','red'))
        sys.exit()

    while True:
        start = nb.display_main_menu()
        if start == 2:
            user_choice,param = nb.display_menu_get()
            if param == 'default':
                get_data,get_status_code = nb.get_default(user_choice)
                if get_status_code == 200:
                    nb.save(get_data)
            else:
                get_data,get_status_code = nb.get_custom(user_choice)
                if get_status_code == 200:
                    nb.save(get_data)
            continue
        if start == 3:
            user_choice,param = nb.display_menu_post()
            post_data = nb.post(user_choice)
            print(post_data)
            continue
        if start == 4:
            user_choice,param = nb.display_menu_patch()
            patch_data = nb.patch(user_choice)
            print(patch_data)
            continue
        if start == 5:
            user_choice,param = nb.display_menu_delete()
            delete_data = nb.delete(user_choice)
            print(delete_data)
            continue
        else:
            break


if __name__ == '__main__':
    main()