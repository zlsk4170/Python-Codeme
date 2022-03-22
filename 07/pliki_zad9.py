# Korzystając z Google dowiedz się więcej o kodowaniu ASCII.
# Utwórz plik, który tworzy prostą zaszyfrowaną wiadomość.
# Każdą literę tekstu zapisuje za pomocą dziesiętnych wartości kodów ASCII.
# Przykładowo literze A odpowiada numer 65. Zapoznaj się z metodami ord() oraz char().
# Pamiętaj o dodaniu znaku podziału. Utwórz drugi skrypt, który rozszyfruje wiadomość

def encode_message():
    message = input('Wprowadź jakieś zdanie: ')
    message = list(message)
    cipher_message = []
    for letter in message:
        cipher_letter = str(ord(letter))
        cipher_message.append(cipher_letter)
    cipher_message = '-'.join(cipher_message)
    print(f'Oto Twoja wiadomość w kodzie ASCII: {cipher_message}')
    return cipher_message

def create_file(cipher_message):
    with open('cipher_file.txt','w') as file:
        file.write(cipher_message)
        return 'cipher_file.txt'

def open_file(ciphered_file):
    with open(ciphered_file) as file:
        ciphered_text = file.read()
        return ciphered_text

def decode_message(cipher_text):
    split_text = cipher_text.split('-')
    decoded_message = []
    for num in split_text:
        num = int(num)
        decoded_num = chr(num)
        decoded_message.append(decoded_num)
    decoded_text = ''.join(decoded_message)
    return decoded_text

def main():
    ciphered_message = encode_message()
    ciphered_file = create_file(ciphered_message)
    read_file = open_file(ciphered_file)
    original_text = decode_message(read_file)
    print(f'Oto Twoja oryginalna wiadomość: {original_text}')

main()