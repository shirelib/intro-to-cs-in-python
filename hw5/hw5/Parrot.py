from hw5.Bird import Bird


class Parrot(Bird):

    def __init__(self, nick_name, price, power, type="Parrot"):
        Bird.__init__(self, nick_name, price, power, type)
        self.fly = True