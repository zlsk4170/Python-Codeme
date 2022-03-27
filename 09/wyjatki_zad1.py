# Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy.
# Złap wyjątki jakie mogą się przy tej okazji wydarzyć.

list = [(1,1),True,10,'aa',0,1.0]

try:
    for item in list:
        result = 10/item
        print(result)
except (TypeError,ZeroDivisionError):
    print('Coś poszło nie tak')