from hw5.Animal import Animal


class Bird(Animal):

    def __init__(self, nick_name, price, power, type):
        Animal.__init__(self, nick_name, price, power, type)
        self.fly = False

    def __ge__(self, other):
        if not isinstance(other, Bird):
            return Animal.__ge__(self, other)
        elif self.fly and other.fly:
            return Animal.__ge__(self, other)
        elif self.fly and not other.fly:
            return True
        else:
            return False


