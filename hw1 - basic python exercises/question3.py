# ************************ QUESTION 3 **************************
def question3(input_list):
    ### WRITE CODE HERE

    # finding 0's index
    dex = -1
    dex_0 = 0
    for n in input_list:
        dex += 1
        if n == 0:
            dex_0 = dex
            break # breaks once it found 0's index

    # slicing the list until 0, and separating evens and unevens into two lists
    sliced = input_list[:dex_0]
    evens = [n for n in sliced if n % 2 == 0]
    unevens = [n for n in sliced if n % 2 != 0]

    # minimum-finding function
    def minimum(lst):
        minim = lst[0]
        for n in lst:
            if n < minim:
                minim = n
        return minim

    # in each list, finding 1st minimum, removing it and finding next minimum
    even_min1 = minimum(evens)
    evens.remove(even_min1)
    even_min2 = minimum(evens)
    uneven_min1 = minimum(unevens)
    unevens.remove(uneven_min1)
    uneven_min2 = minimum(unevens)

    # calculating average of aforementioned minimums and printing answer
    avg = (even_min1 + even_min2 + uneven_min1 + uneven_min2) / 4
    print(avg)

