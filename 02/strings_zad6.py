txt = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than comple.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

print('Liczba wystąpień słowa better -> ', txt.count('better'))
print()

print('Usunięcie z tekstu symbolu gwiazdki -> ')
txt1 = txt.replace('*','')
print(txt1)
print()

print('Zamiana jednego wystąpienia explain na understand -> ')
txt2 = txt1.replace('explain','understand',1)
print(txt2)
print()

print('Usunięcie spacji i połączenie wszystkich słów myślnikiem -> ')
txt3 = txt2.replace(' ','-')
print(txt3)
print()

print('Podziel tekst na osobne zdania za pomocą kropki -> ')
print()
txt4 = txt.replace('\n','')
txt5 = txt4.split('.')
print(txt5)