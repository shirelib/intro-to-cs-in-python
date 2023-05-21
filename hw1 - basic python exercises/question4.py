# ************************ QUESTION 4 **************************
def question4(input_number):
    # ***** WRITE CODE HERE *****

    # finding all dividers of the input number
    dividers = []
    for i in range(1,input_number):
        if input_number % i == 0:
            dividers.append(i)

    # checking if it's a perfect number
    if sum(dividers) == input_number:
        print(True)
    else:
        print(False)
