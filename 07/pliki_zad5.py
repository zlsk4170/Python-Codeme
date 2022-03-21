# Wykorzystaj plik zawierający fragment Pana Tadeusza.
# Znajdź najdłuższe słowo występujące w zadanym fragmencie.

def get_text():
    with open('pan.txt',encoding='utf-8') as f:
        content = f.read()
    return content

def clean_text(text):

    extras = '.!,():'
    for symbol in extras:
        text = text.replace(symbol,'')
    return text

def find_longest_word(text):

    text = text.split()
    
    longest_word = ''
    for current_word in text:
        if len(current_word) > len(longest_word):
            longest_word = current_word

    return longest_word


txt = get_text()
cleaned_txt = clean_text(txt)
search_world = find_longest_word(cleaned_txt)
print(search_world)