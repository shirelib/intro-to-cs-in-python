import copy


class Animal:

    def __init__(self, nick_name, price, power, type):
        self.nick_name = nick_name
        if price <= 0:
            raise ValueError
        self.price = float(price)
        if not (power > 0 and power <= 100):
            raise ValueError
        self.__power = float(power)
        self.type = type

    def __repr__(self):
        return "Name: {}, Price: {} NIS, Power: {}".format(self.nick_name, self.price, self.__power)

    def _get__power(self):
        return copy.copy(self.__power)

    def _set__power(self, new_power):
        if new_power > 0 and new_power <= 100:
            self.__power = float(new_power)

    def win(self):
        return "{} winner".format(self.nick_name)

    def loss(self):
        return "{} loser".format(self.nick_name)

    def __ge__(self, other):
        try:
            if self.__power >= other.__power:
                return True
            else:
                return False
        except Exception:
            raise ValueError

    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False
        elif self.nick_name == other.nick_name:
            return True
        else:
            return False                        #

    def get_type(self):
        return self.type
