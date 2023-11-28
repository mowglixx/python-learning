# Fizzbuzz Challenge

# Defining Functions
#############################################################
# Define a function to handle each number and 
# return a pretty version of the answer


def numberHandler(x, word):
    print(f"{x}: {word}")

# Define a function that takes each number


def fizzbuzz(x: int):
    # the modulus (%) operator returns the remainder 
    # from a division
    #
    # example:
    #
    #    3 % 2 = 1 remaining
    #    6 % 2 = 0 remaining
    #
    if (x % 3 == 0) and (x % 5 == 0):
        numberHandler(x, "FizzBuzz")
    elif x % 3 == 0:
        numberHandler(x, "Fizz")
    elif x % 5 == 0:
        numberHandler(x, "Buzz")
    else:
        numberHandler(x, "Not divisble by 3 or 5")


# Running Code
#############################################################

# Declare a range of numbers from 1-100 (101 is not included)

numbers = range(1, 101)

# "loop" through each number in the numbers range
# and run the `fizzbuzz` function on each number
# 1, 2, 3, 4... 100 one after the other until 
# there are no numbers left in the range

for eachNumber in numbers:
    fizzbuzz(eachNumber)

