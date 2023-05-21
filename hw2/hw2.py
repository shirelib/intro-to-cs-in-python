# *************** HOMEWORK 2 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
### WRITE CODE HERE
def rhombus(side_size):
    # calculating the diagonal by *s and using it to produce the shape of the rhombus, then printing.
    diagonal = side_size*2-1
    shaping_range = list(range(1,diagonal,2)) + list(range(diagonal,0,-2))
    for i in shaping_range:
        print(" "*((diagonal-i)//2) + "*"*i)


# ************************ QUESTION 2 **************************
### WRITE CODE HERE
def lagrange_four_square_theorem(num):
    # finding what possible squares can be used to get a sum of the input num:
    # to do this, finding all numbers, equal or smaller than input num, that have integer roots.
    squares_until_input = []
    for i in range(num+1):
        if i**0.5 % 1 == 0:
            squares_until_input.append(i)

    sets = []

    # assigning each of squares_until_input items in four variables than represent the 4 numbers:
    #  [1st, 2nd, 3rd, 4th]. List should be ascending, so if 2nd<1st, continues loop (also prevents duplicates).
    for i in squares_until_input:
        n_1st = i
        for i in squares_until_input:
            n_2nd = i
            if n_2nd < n_1st:
                continue # ignores this combination because it's not the ascending version of this combination
            for i in squares_until_input:
                n_3rd = i
                if n_3rd < n_2nd:
                    continue
                for i in squares_until_input:
                    n_4th = i
                    if n_4th < n_3rd:
                        continue
                    sum_of_squares = n_1st + n_2nd + n_3rd + n_4th
                    if sum_of_squares == num:  # checking if condition is met
                        squared_set = [n_1st, n_2nd, n_3rd, n_4th]
                        set = [int(n**.5) for n in squared_set]  # returning series to square roots
                        sets.append(set)
    return sets


# ************************ QUESTION 3 **************************
### WRITE CODE HERE
def max_series(numbers):
    # preparing variables
    uneven_series = [0]   # the list is not empty because of a future line. first number is always 0
    longest_series = 0
    largest_divided_3 = -1

    for i in range(len(numbers)):

        # checking if uneven
        if numbers[i] % 2 != 0:
            if longest_series == 0:
                longest_series = 1

            # checking every two numbers to find ascending uneven series whose length >= 2
            if i > 0:
                if numbers[i]%2 != 0 and numbers[i-1]%2 != 0 and numbers[i] > numbers[i-1]:
                    if numbers[i-1] != uneven_series[-1]: # the reason uneven_series is never empty - to avoid errors here
                        uneven_series.append(numbers[i-1])
                    uneven_series.append(numbers[i])
                    if len(uneven_series) > longest_series:
                        longest_series = len(uneven_series)-1  # -1 because of the first 0
                else:   # if the two numbers don't meet the conditions, it means the series was broken
                    uneven_series = [0]  # reset

        # checking if divides by 3 and largest so far
        if numbers[i] % 3 == 0 and numbers[i] > largest_divided_3:
            largest_divided_3 = numbers[i]

    return([longest_series,largest_divided_3])

