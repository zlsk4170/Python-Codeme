class Electronics():
    def __init__(self):
        print("I'm electronics")


class Watch(Electronics):
    def __init__(self):
        print("I'm a watch")
        super().__init__()


class Phone(Electronics):
    def __init__(self):
        print("I'm a phone")
        super().__init__()


class Smartwatch(Watch,Phone):
    def __init__(self):
        print("I'm a smartwatch")
        super().__init__()

abc = Smartwatch()