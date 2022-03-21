# Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych.
# Sprawdź dla każdej kart jej typ.
# Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.

# otwarcie pliku
# przeczytanie linijka po linijce, weryfikacja
# wyniki do oddzielnych plików


def read_card_list():
    with open('cards.txt') as f:
        content = f.readlines()
        card_list = []
        for number in content:
            stripped_number = number.strip()
            card_list.append(stripped_number)
    return card_list


def visa_list(card_list):
    visa_cards = []
    for card_number in card_list:
        if card_number[0] == '4':
            if len(card_number) == 13 or len(card_number) == 16:
                visa_cards.append(card_number)
    return visa_cards

def mc_list(card_list):
    mc_cards = []
    for card_number in card_list:
        if int(card_number[0:2]) in range(51,56) or int(card_number[0:4]) in range(2221,2721) and len(card_number) == 16:
            mc_cards.append(card_number)
    return mc_cards

def ae_list(card_list):
    ae_cards = []
    for card_number in card_list:
        if card_number[0:2] == '34' or card_number[0:2] == '37' and len(card_number) == 15:
            ae_cards.append(card_number)
    return ae_cards

def create_files(visa_list,mc_list,ae_list):
    with open("visa_cards.txt",'w') as f:
        content_visa = str(visa_list)
        visa = f.write(content_visa)

    with open("mc_cards.txt",'w') as f:
        content_mc = str(mc_list)
        mc = f.write(content_mc)

    with open("ae_cards.txt",'w') as f:
        content_ae = str(ae_list)
        ae = f.write(content_ae)

    return (visa, mc, ae)


c = read_card_list()
v, m, a = create_files(visa_list(c),mc_list(c),ae_list(c))
print('Utworzyłem oddzielne pliki z numerami kart Visca, MasterCard i AmericanExpress')