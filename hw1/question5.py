# ************************ QUESTION 5 **************************
def question5(my_string):
    # ***** WRITE CODE HERE *****

    # if string length is less than 4, print it as is
    if len(my_string) < 4:
        print(my_string)
    # if string length is 4 or more, slice first part, and add second part (last 3 characters) with upper case
    else:
        result = my_string[:-3] + str.upper(my_string[-3:])
        print(result)
