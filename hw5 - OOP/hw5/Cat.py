from hw5.Mammal import Mammal


class Cat(Mammal):

    def __init__(self, nick_name, price, power, type="Cat"):
        Mammal.__init__(self, nick_name, price, power, type)

    def speak(self):
        return str(Mammal.speak(self)) + " meow"
