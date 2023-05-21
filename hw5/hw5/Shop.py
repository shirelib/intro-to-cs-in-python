import copy
from hw5.AnimalFactory import AnimalFactory


class Shop:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.__animal_list = {}    # key: nick_name, value: instance

    def get_name(self):
        return str(self.name)

    def __add__(self, other):
        # input: animal or list
        if not type(other) == list:
            other = [other]
        # other is now a list.

        # creating a for_sale animals dict and an animals-bought counter
        for_sale = {}
        bought = 0

        # adding animals in list into the new dictionary
        for animal_for_sale in other:
            for_sale[animal_for_sale.nick_name] = (animal_for_sale.price, animal_for_sale) # {nick_name: price, instance}
        sorted_price_animal = sorted(for_sale, key=lambda key: for_sale[key][0])
        # adding animals according to the sorted list, as much as the balance allows
        for animal_name in sorted_price_animal:
            if self.balance - for_sale[animal_name][0] >= 0:
                self.balance -= for_sale[animal_name][0]
                self.__animal_list[animal_name] = for_sale[animal_name][1]
                bought += 1
            else: # balance is below 0
                break

        return bought

    def get__animals(self):
        # creating the animals again and adding them into a new dictionary, which is returned
        new_dict = {}
        for animal_name in self.__animal_list:
            animal_instance = self.__animal_list[animal_name]
            new_dict[animal_name] = AnimalFactory.create(animal_instance.type, animal_name,
                                                         animal_instance.price, animal_instance._get__power())
        return new_dict

    def sell(self, nick_name):
        # sells an animal and returns it
        for listed_animal in self.__animal_list:
            if listed_animal == nick_name:
                self.balance += self.__animal_list[listed_animal].price
                to_remove = self.__animal_list[listed_animal]
                del self.__animal_list[listed_animal]
                return to_remove

    def num_of_animals(self):
        # returns num of animals in dictionary
        return len(self.__animal_list)

    def play(self, animal_1, animal_2):
        # two animals play and one wins, one loses
        ins_animal_1, ins_animal_2 = None, None
        for animal_name in self.__animal_list:
            if animal_name == animal_1:
                ins_animal_1 = self.__animal_list[animal_name]
            elif animal_name == animal_2:
                ins_animal_2 = self.__animal_list[animal_name]
        if ins_animal_1 == None or ins_animal_2 == None:
            return False
        elif ins_animal_1 >= ins_animal_2:
            return ins_animal_1.win() + "\n" + ins_animal_2.loss()
        else:
            return ins_animal_2.win() + "\n" + ins_animal_1.loss()
