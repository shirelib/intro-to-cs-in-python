def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)


def knapsack_1(lst, weight_lim):
    revenue = 0
    proportional_values = {}
    for item in lst:
        proportional_values[item] = item[1]/item[0]
    proportional_values = sorted(proportional_values, key=lambda x: proportional_values[x], reverse=True)
    for item in proportional_values:
        if item[0] <= weight_lim:
            # takes item
            weight_lim -= item[0]
            revenue += item[1]
        elif weight_lim != 0:
            # example: value 5, weight 4, limit 3. i need 3/4 from value
            revenue += weight_lim/item[0] * item[1]
            weight_lim = 0
            break
    return revenue

#print(knapsack_1([(3,4), (2,1), (4,5), (8,7)], 8))


def total_items_value(item_lst):
    total_val = 0
    for item in item_lst:
        total_val += item[1]
    return total_val
import copy

def knapsack_recur(lst, weight_lim, res_items=[]):
    # stop conditions
    if weight_lim < 0:
        return [(0, float('-inf'))]
    elif lst == []:
        return res_items

    # take first item
    taken = total_items_value(knapsack_recur(lst[1:], weight_lim-lst[0][0], res_items)) + lst[0][1] #value
    not_taken = total_items_value(knapsack_recur(lst[1:], weight_lim, res_items))

    new_res_items = copy.copy(res_items)
    if max(taken, not_taken) == taken:
        new_res_items.append(lst[0])

    return new_res_items

#print(knapsack_recur([(3,4), (2,1), (4,5), (8,7)], 8))

"""
def binary_gen(N):
    result = '0'
    for n in range(N):
        print("i'm in", n)
        # for each n, add 1 to the binary number.
        # search for last 0, turn it into 1     '101'
        # turn all 1s after it to 0
        if result == '0':
            result = '1'
        else:
            for i in range(len(result),0,-1):
                print('-- im in i:', i)
                if result[i] == '0':
                    result = result[:i] + '1' + '0'*(len(result[i+1:]))
                else:
                    result = '1' + '0'*(len(result))
        yield result

iter = binary_gen(3)
print(next(iter))
print(next(iter))
print(next(iter))
"""






# count options
def knapsack(weights, values, weight_lim, p):
    if weight_lim < 0:
        return float('-inf')
    if len(items) == 0:
        if p > 0:
            return float('-inf')
        else:
            return 0

    taken = knapsack(weights[1:], values[1:], weight_lim - weights[0], p - values[0]) + values[0]
    not_taken = knapsack(weights[1:], values[1:], weight_lim, p)
    return max([taken, not_taken])









def reverse_in_segments(str1, segment_length):
    new_str = ""
    for n in range(1,len(str1)+1):
        if n % segment_length == 0:
            segment = str1[n-segment_length : n]    # 0[1], 1[2], 2[3], 3[4]
            new_str += segment[::-1]
    remainder = len(str1) % segment_length
    if remainder != 0:
        last_part = str1[remainder*(-1):]
        new_str += last_part[::-1]
    return new_str

#print(reverse_in_segments('abcdefgh', 4))   # ’dcbahgfe’
#print(reverse_in_segments('abcdefgh', 3))  # ’cbafedhg’


def create_multiple_encoders(code_list):
    func_list = []
    for num in code_list:
        if num > 0:
            func_to_add = lambda x: reverse_in_segments(x, num)
        else:
            func_to_add = lambda x: (x[:num*(-1)])[::-1] + x[num*(-1):]
        func_list.append(func_to_add)
    return func_list

encoders = create_multiple_encoders([3,-4])
#print(encoders[0]('abcdef'))   #‘cbafed’
#print(encoders[1]('abcdefg'))   #‘dcbaefg’



def multi_reverse_encoder_decoder(code_list, decode=False):
    # generate func list
    encoders = create_multiple_encoders(code_list)
    if not decode:
        seder = range(len(encoders))
    else:
        seder = range(len(encoders)-1, -1, -1)
    def func(the_string):
        for i in seder:
            the_string = encoders[i](the_string)
        return the_string
    return func

encoder1 = multi_reverse_encoder_decoder([3])
encoder2 = multi_reverse_encoder_decoder([3,-2])
encoder3 = multi_reverse_encoder_decoder([3,-2,4])
decoder3 = multi_reverse_encoder_decoder([3,-2,4],True)
print(encoder1('abcdef')) #‘cbafed’
print(encoder2('abcdef')) #‘bcafed’
print(encoder3('abcdef')) #‘facbde’
print(decoder3(encoder3('abcdef'))) #‘abcdef









