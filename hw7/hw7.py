"""
INTRO
"""


class Plant:
    """
    A representation of a plant. Implements a constructor with defaulting values(except one),
     a represent overload and 2 more methods:
    # get_maintenance_cost.
    # purchase_decision.
    """
    def __init__(self, name: str,
                 aesthetics: int = 1,
                 water_consumption_month: int = 1,
                 average_month_yield: int = 1,
                 seasonal: bool = False):
        """
        Initializes an instance of Plant.
        :param name: (str) the name of the plant.
        :param aesthetics: (int) the level of aesthetics the plant is valued at.
        :param water_consumption_month: (int) the plant's monthly consumption of water amount
        :param average_month_yield: (int) the value the plant creates every month
        :param seasonal: (bool) whether the plant is year-round (True) plantation or only 6 months (False).
        """
        self.name = name
        self.aesthetics = aesthetics
        self.water_consumption_month = water_consumption_month
        self.average_month_yield = average_month_yield
        self.seasonal = seasonal

    def get_maintenance_cost(self, func1):
        """
        Invokes the given argument as a function with the instance itself (self) as input argument.
        :param func1: a function object.
        :return:
        """
        return func1(self)

    def purchase_decision(self, func1, func2):
        """
        Invokes the first given argument as a function with two inputs (by order):
         the instance itself, and the result of the second argument invoked as a function with the instance
         itself (self) as input argument.
        :param func1: a function object.
        :param func2: a function object.
        :return:
        """
        return func1(self, func2(self))

    def __repr__(self):
        """
        overloads the python object __repr__ method.
        :return: str
        """
        return "name={}".format(self.name)


class GardenManager:
    """
    A representation of a garden management system. Implements a constructor with no defaulting values,
     a represent overload and 1 more methods:
     # action.
    """
    def __init__(self, plants_in_garden: list):
        """
        Initializes an instance of GardenManager.
        :param plants_in_garden: a list of the plants which are in the garden.
        """
        self.plants_in_garden = plants_in_garden

    def action(self, func1):
        """
        Invokes the given argument as a function with the instance itself (self) as input argument.
        :param func1: a function object.
        :return:
        """
        return func1(self)

    def __repr__(self):
        """
        overloads the python object __repr__ method.
        :return: str
        """
        return "Number of plants = {0}".format(len(self.plants_in_garden))
#

"""
PART A - Lambda functions
"""

# Q1
get_cost_lmbd = lambda x: x.water_consumption_month

# Q2
get_yearly_cost_lmbd = lambda x: x.water_consumption_month*12 if not x.seasonal else x.water_consumption_month*6

# Q3
worth_investing_lmbd = lambda x: True if x.average_month_yield > x.water_consumption_month else False

# Q4
declare_purchase_lmbd = lambda x, worth_it: "{}:{}".format(x.name,"yes") if worth_it \
                                                            or x.aesthetics >= x.water_consumption_month \
                                         else "{}:{}".format(x.name,"no")

# Q5

get_plants_names_lmbd = lambda x: sorted(list(map(lambda y: y.name, x.plants_in_garden)))



"""
PART B - High order functions
"""

# Q1 -
def retrospect(garden_manager):
    # returns a list of flower names where amount > water consumption
    instances = filter(worth_investing_lmbd, garden_manager.plants_in_garden)
    return list(map(lambda x: x.name, instances))

# Q2 -
def get_total_yearly_cost(garden_manager):
    # returns total yearly cost of all flowers
    from functools import reduce
    costs = map(get_yearly_cost_lmbd, garden_manager.plants_in_garden)
    return reduce(lambda x,y: x+y, costs)

# Q3 -
def get_aesthetics(garden_manager):
    # returns a list of aesthetics
    return list(map(lambda x: x.aesthetics, garden_manager.plants_in_garden))


"""
PART C - University gate
"""

class GateLine:
    def __init__(self, capacity_max):
        # first in line = first to enter
        self.regular_line = []
        self.priority_line = []
        self.capacity_max = capacity_max

    def new_in_line(self, student_id, priority_id_holder):
        current_capacity = len(self.regular_line) + len(self.priority_line)
        # if line is not full
        if current_capacity < self.capacity_max:
            if priority_id_holder:
                self.priority_line.append(student_id)
            else:
                self.regular_line.append(student_id)
        elif priority_id_holder: # if line is full but the student is a priority id holder, add anyway
            if self.regular_line != []:
                self.regular_line.pop()
            self.priority_line.append(student_id)


    def open_gate(self):
        # returns student_id of the student who enters and removes them from the queue
        if self.priority_line != []:
            return self.priority_line.pop(0)
        elif self.regular_line != []:
            return self.regular_line.pop(0)

    def is_empty(self):
        # checks if line is empty
        if self.priority_line == [] and self.regular_line == []:
            return True
        else:
            return False

    def show_who_is_in_line(self):
        # shows who is waiting in line
        return self.priority_line + self.regular_line


