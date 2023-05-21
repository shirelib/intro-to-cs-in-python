from hw5.Dog import Dog
from hw5.Cat import Cat
from hw5.Snake import Snake
from hw5.Turtle import Turtle
from hw5.Parrot import Parrot


class AnimalFactory(object):

    @staticmethod
    def create(type_animal, nick_name, price, power):

        # input check
        if not price > 0:
            raise ValueError
        else:
            price = float(price)
        if not (power > 0 and power <= 100):
            raise ValueError
        else:
            power = float(power)

        # creator
        if type_animal == 'Dog':
            new_dog = Dog(nick_name, price, power)
            print("Dog created")
            return new_dog
        elif type_animal == 'Cat':
            new_cat = Cat(nick_name, price, power)
            print("Cat created")
            return new_cat
        elif type_animal == 'Snake':
            new_snake = Snake(nick_name, price, power)
            print("Snake created")
            return new_snake
        elif type_animal == 'Turtle':
            new_turtle = Turtle(nick_name, price, power)
            print("Turtle created")
            return new_turtle
        elif type_animal == 'Parrot':
            new_parrot = Parrot(nick_name, price, power)
            print("Parrot created")
            return new_parrot
