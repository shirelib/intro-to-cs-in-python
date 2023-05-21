# ************************ QUESTION 2 **************************
def question2(input_number):
    ### WRITE CODE HERE
    # Preparations for the code that finds primes
    prime_counter = 1
    prime_list = [2]
    # If first two, it will give the answer
    if input_number == 1 or input_number == 2:
        print(input_number+1)
    # If above the first two, it will calculate k primes
    else:
        num = 3
        while prime_counter < input_number:
            for i in range(2, num):
                if num % i == 0: # if it finds dividers, it breaks
                    break
                if i == num-1: # if it didn't break at the last iteration, means it's a prime
                    prime_counter += 1
                    prime_list.append(num)
                if prime_counter == input_number: # if it found all primes until input_number, print answer
                    print(prime_list[input_number-1])
            num += 1
