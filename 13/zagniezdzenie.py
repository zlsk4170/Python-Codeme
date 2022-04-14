def example_function():

    def nested_function():  #funkcja lokalna
        print('Jestem w srodku zagnieżdżenia')

    return nested_function #bierzemy tylko nazwę


new_function = example_function()

new_function() # wywołujemy nazwę funkcji zagnieżdżonej, pod new_function kryje się nested_function