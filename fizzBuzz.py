# defining functions
def numberHandler(x: int, word: str):
    print(f"{x}: {word}")


def fizzBuzz(x: int):
    """# summary
    - print fizz to the screen if the x is divisible by 3
    - print buzz to the screen if the x is divisible by 5
    - print fizzbuzz to the screen if the x is divisible by 3 and 5
    - print the x if not divisble by 3 or 5

    [HelloWorldCollection](http://helloworldcollection.de/#Python%C2%A03)

    this is pretty cool
    """
    if x % 3 == 0 and x % 5 == 0:
        numberHandler(x, "FizzBuzz")
    elif x % 3 == 0:
        numberHandler(x, "Fizz")
    elif x % 5 == 0:
        numberHandler(x, "Buzz")
    else:
        numberHandler(x, "Not divisble by 3 or 5")


# running code

numbers = range(1, 101)

for number in numbers:
    fizzBuzz(number)
