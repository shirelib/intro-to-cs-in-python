import copy


class Monom:
    def __init__(self, power, coef=1):
        self.power = power
        if coef % 1 != 0:
            self.coef = round(coef, ndigits=2)
            if self.coef % 1 == 0:
                self.coef = int(self.coef)
        else:
            self.coef = coef
        self.next = None


    def __repr__(self):
        # defaults
        coef_to_print = self.coef
        power_to_print = self.power
        x_to_print = "X^"

        # if coef is a float
        if type(self.coef) == float:
            if self.coef % 1 == 0:
                coef_to_print = int(self.coef)
            else:  # coef isn't whole
                coef_to_print = round(self.coef, ndigits=2)
                if coef_to_print % 1 == 0:
                    coef_to_print = int(coef_to_print)

        # if power == 0 or 1
        if self.power == 1:
            x_to_print, power_to_print = "X", ""
        elif self.power == 0:
            x_to_print, power_to_print = "", ""
        # if coef == negative, 0 or 1
        if coef_to_print < 0:
            return "(" + str(coef_to_print) + x_to_print + str(power_to_print) + ")"
        elif coef_to_print == 1 and self.power != 0:
            coef_to_print = ""
        elif coef_to_print == 0:
            return str(0)

        return str(coef_to_print) + x_to_print + str(power_to_print)


    def __mul__(self, other):
        if isinstance(other, Monom):
            return Monom(self.power+other.power, self.coef*other.coef)

        else: # scalar
            return Monom(self.power, self.coef*other)

    def __rmul__(self, other):
        return self * other

    def derivative(self):
        new_coef = self.coef * self.power
        new_power = self.power - 1
        if new_power < 0:
            new_power = 0 ##
        return Monom(new_power, new_coef)

    def integral(self):
        if self.coef == 0:
            return Monom(0,0)
        new_power = self.power + 1
        return Monom(new_power, self.coef * 1/new_power)

    def __neg__(self):
        return Monom(self.power, -self.coef)



from functools import total_ordering

@total_ordering
class Polynomial:
    def __init__(self, l):
        self.head = None

        # input checks
        valid_input = True
        if type(l) != list:   # if l isn't a list
            valid_input = False
        for tup in l:           # if the list doesn't contain tuples with 2 objects
            if type(tup) != tuple or len(tup) != 2:
                valid_input = False
        if not valid_input:
            raise ValueError('invalid polynomic initiation.')

        sorted_l = sorted(l) # sorted based on power

        for tup in sorted_l:
            if tup[1] == 0: # coef is 0
                continue
            new_monom = Monom(tup[0], tup[1])
            self.add_monom(new_monom)


    def add_monom(self, original_monom):
        # adds a monom to polynomial
        monom = Monom(original_monom.power, original_monom.coef)
        if self.head == None:
            self.head = monom
        else:
            current = self.head
            while True:
                if current == None:
                    # add as a new monom
                    former_head = self.head
                    self.head = monom
                    self.head.next = former_head
                    break
                elif current.power == monom.power:
                    current.coef += monom.coef
                    break
                else: # advance
                    current = current.next
        self.remove_coef_zero()

    def remove_coef_zero(self):
        current = self.head
        if self.head == None:   # empty polynomial
            return
        elif self.head.coef == 0:   # head's coef is 0
            self.head = self.head.next
        while current.next != None:
            if current.next.coef == 0:
                current.next = current.next.next
                if current.next == None: # if skipped a node, and now the next one is None
                    break
            current = current.next # advance


    def __repr__(self):
        sorted = self.sorted()
        to_prnt_list = []

        current = sorted.head
        while current != None:
            to_prnt_list.append(current)
            current = current.next # advancing
        to_prnt = ""
        for i in range(len(to_prnt_list)):
            item = to_prnt_list[i]
            if item.__repr__() != str(0):
                if i < len(to_prnt_list)-1:
                    to_prnt += str(item.__repr__()) + "+"
                else:
                    to_prnt += str(item.__repr__())
        if to_prnt == "":
            to_prnt = "0"
        return "P(X)=" + to_prnt

    def rank(self):
        if self.head == None:
            return 0
        # coef can't be 0 because I removed those
        return self.head.power

    def calculate_value(self, x):
        current = self.head
        res = 0
        while current != None:
            res += (x**current.power) * current.coef
            current = current.next
        return res

    def print_monom_chain(self):
        chain = []
        current = self.head
        while current != None:
            chain.append((current.power, current.coef))
            current = current.next
        print(chain)

    def __neg__(self):
        # use list of tuples to initiate new poly
        tuple_list = []
        current = self.head
        while current != None:
            tuple_list.append((current.power, current.coef*(-1)))
            current = current.next # advancing
        return Polynomial(tuple_list)

    def __sub__(self, other):
        new_poly = copy.deepcopy(self)
        current = other.head
        while current != None:
            new_poly.add_monom(-current)
            current = current.next  # advancing
        return new_poly

    def __add__(self, other):
        # adds polynomial + polynomial
        new_poly = copy.deepcopy(other)
        current = self.head
        while current != None:
            new_poly.add_monom(current) # adds other's monoms to original poly
            current = current.next  # advancing
        return new_poly


    def __mul__(self, other):
        multiplied_poly = Polynomial([])

        if isinstance(other, Polynomial): # multiply each monom by each monom
            current = self.head
            while current != None: # going over each monom in original polynomial, and multuplying it by other
                mul_by_one_monom = other.mul_by_monom(current)
                #mul_by_one_monom = other * current # poly * mon - also works
                multiplied_poly += mul_by_one_monom
                current = current.next  # advancing

        else: # scalar
            current = self.head
            while current != None:
                monom_by_scalar = current * other
                multiplied_poly.add_monom(monom_by_scalar)
                current = current.next  # advancing

        multiplied_poly = multiplied_poly.sorted()

        return multiplied_poly

    def __rmul__(self, other):
        return self * other


    def mul_by_monom(self, monom):
        # creates empty polynomial, and adds to it the product of original monom * other monom
        multiplied_poly = Polynomial([])
        current = self.head
        while current != None:
            multiplied_poly.add_monom(current * monom)
            current = current.next  # advancing
        return multiplied_poly

    def __len__(self):
        current = self.head
        len = 0
        while current != None:
            len += 1
            current = current.next #advancing
        return len

    def sorted(self):
        new_sorted = Polynomial([])
        l_of_powers = []
        # creating a list of powers by looping through the monom linked list
        for member in range(len(self)):
            smallest_power = float('inf')
            current = self.head
            while current != None:
                if current.power < smallest_power and current.power not in l_of_powers:
                    smallest_power = current.power
                current = current.next  # advancing
            if smallest_power not in l_of_powers:                               # not sure i need this line
                l_of_powers.append(smallest_power)

        # adding according to sorted list of powers
        for power in l_of_powers:
            current = self.head
            while current != None:
                if current.power == power:
                    new_sorted.add_monom(current)
                current = current.next  # advancing
        return new_sorted

    def derivative(self):
        derivative_poly = Polynomial([])
        current = self.head
        while current != None:
            derivative_poly.add_monom(current.derivative())
            current = current.next  # advancing
        return derivative_poly.sorted()

    def integral(self, constant = 0):
        integral_poly = Polynomial([])
        integral_poly.add_monom(Monom(0, constant))
        current = self.head
        while current != None:
            integral_poly.add_monom(current.integral())
            current = current.next  # advancing
        return integral_poly.sorted()

    def __eq__(self, other):
        pol1 = self.sorted()
        pol2 = other.sorted()
        if len(pol1) == len(pol2):
            current_1 = pol1.head
            current_2 = pol2.head
            while current_1 != None and current_2 != None:  # condition for both, because of empty poly case
                if current_1.power != current_2.power or current_1.coef != current_2.coef:
                    return False
                current_1 = current_1.next
                current_2 = current_2.next
            return True
        else: # lengths aren't equal
            return False

    def __gt__(self, other):
        pol1 = self.sorted()
        pol2 = other.sorted()
        current_1 = pol1.head
        current_2 = pol2.head
        while True:
            if (current_1 == None and current_2 == None) or (current_1 == None and current_2 != None):
                return False
            elif current_1 != None and current_2 == None or current_1.power > current_2.power: # power greater or existence greater
                return True
            elif current_1.power == current_2.power and current_1.coef > current_2.coef: # power equal, coef greater
                return True
            elif current_1.power == current_2.power and current_1.coef == current_2.coef: # both equal
                current_1 = current_1.next
                current_2 = current_2.next
            else: # power1 < power 2 OR power1 == power2 and coef1 < coef2
                return False



class BinTreeNode:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None


class PolynomialBST:
    def __init__(self):
        self.head = None

    def insert(self, poly):
        node = BinTreeNode(poly)

        def insert_recur(current, node):
            if node.value <= current.value: # if smaller or equal
                if current.left is None:  # add smaller/equal on left leg
                    current.left = node
                    return
                else: # can continue
                    insert_recur(current.left, node)
            elif node.value > current.value: # if larger
                if current.right is None:  # add larger on right leg
                    current.right = node
                    return
                else: # can continue
                    insert_recur(current.right, node)

        if self.head is None:
            self.head = node
        else:
            insert_recur(self.head, node)

    def in_order(self):
        if self.head is None:
            return []
        def in_order_recur(current, res):
            if current is not None:
                in_order_recur(current.left, res)
                res.append(current)
                in_order_recur(current.right, res)
            return res

        return [x.value for x in in_order_recur(self.head, [])]

    def __add__(self, other):
        # adding through recursion:
        # goes through second tree and adds each node into the first tree
        combined_tree = copy.deepcopy(other)

        def add_recur(first_head, second_tree):
            current = first_head # node
            if current is not None:
                add_recur(current.left, second_tree)
                second_tree.insert(current.value)
                add_recur(current.right, second_tree)

        add_recur(self.head, combined_tree)
        return combined_tree


