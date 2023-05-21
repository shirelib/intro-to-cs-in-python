from hw5.Mammal import Mammal


class Dog(Mammal):

    def __init__(self, nick_name, price, power, type="Dog"):
        Mammal.__init__(self, nick_name, price, power, type)

    def speak(self):
        return str(Mammal.speak(self)) + " woof woof"

    def win(self):
        return self.speak() + " " + str(Mammal.win(self))

    



