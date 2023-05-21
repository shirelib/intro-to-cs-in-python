from hw5.Reptiles import Reptiles


class Snake(Reptiles):

    def __init__(self, nick_name, price, power, type="Snake"):
        Reptiles.__init__(self, nick_name, price, power, type)

    def move(self):
        # moving boosts power for a snake (as long as the result of the boost isn't above 100)
        if self._get__power()*2.5 <= 100:
            self._set__power(self._get__power()*2.5)
