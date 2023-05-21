from hw5.Reptiles import Reptiles


class Turtle(Reptiles):

    def __init__(self, nick_name, price, power, type="Turtle"):
        Reptiles.__init__(self, nick_name, price, power, type)

    def loss(self):
        return str(Reptiles.loss(self)) + " I always lose"
