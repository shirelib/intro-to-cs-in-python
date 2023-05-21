from hw5.Animal import Animal


class Reptiles(Animal):

    def __init__(self, nick_name, price, power, type):
        Animal.__init__(self, nick_name, price, power, type)

    def move(self):
        # moving when playing halves the power
        self._set__power(self._get__power()/2)

    def __ge__(self, other):
        # if both are reptiles
        if isinstance(other, Reptiles):
            self.move()
            other.move()
            return Animal.__ge__(self, other)
        # if the other one isn't a reptile
        else:
            if self._get__power() > other._get__power():
                return True
            else:
                return False


