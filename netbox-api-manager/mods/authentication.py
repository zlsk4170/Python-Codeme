from termcolor import colored

def credentials():
    while True:
        print()
        ip_address = input(colored('Give IP address to Netbox application --> ','blue'))
        try:
            if ip_address.startswith('https://'):
                ip_address = ip_address.replace('https://','')
            if ip_address.startswith('http://'):
                ip_address = ip_address.replace('http://','')

            ip_part = ip_address.split('.')

            if len(ip_part) != 4:
                raise ValueError

            for num in ip_part:
                if not isinstance(int(num), int):
                    raise ValueError
                if int(num) < 0 or int(num) > 255:
                    raise ValueError
        except ValueError:
            print(colored(f'IP address is incorrect','red'))
            continue
        break

    base_url = 'https://' + ip_address + '/api'
    token = input(colored('Give your personal token --> ','blue'))

    return base_url, token