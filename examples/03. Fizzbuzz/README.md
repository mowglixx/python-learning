# Fizzbuzz

Fizzbuzz is a coding challenge designed for developers to show their understanding of `control-flow` aka `if-else`.

## Control Flow (If Else)

Control Flow is something we use in Python and many other programming languages to say if a condition is `True`, like `4 < 6`, then run a certain operation.

### Plain English
A good way to imagine control flow is

- `if` this `condition` is `True`
  - run this code

-or-

- `if` this `condition` is `True`
  - run this code
- `else` 
  - run this other code

-or-

- `if` this `condition` is `True`
  - run this code
- `elif` this other `condition` is `True` `and` the conditon above isn't `True`
  - run this other code 
- `else` 
  - run this other, other code if nothing else has run

### Python

Here is an example of an if statement in `Python`

```python
# declare a variable called magic_number 
magic_number = 3
# declare a variable called comparison_number
comparison_number = 8

# if the magic number is less than the comparison number 
if magic_number < comparison_number:
  # run this
  print("magic_number is LESS than 8")
else: 
  # otherwise
  # run this
  print("magic_number is MORE than 8")

```

#### Note
`Python` is not like the other girls.

It uses `elif` instead of `if else` or `else if` like other languages.



## Fizzbuzz Challenge

Write a function that takes a number and...

- if the value of `x` is divisible by `3`, print `fizz` to the screen 
- if the value of `x` is divisible by `5`, print `buzz` to the screen
- if the value of `x` is divisible by `3` AND `5`, print `fizzbuzz` to the screen
- if the value of `x` is NOT divisble by`3` or `5`, print the value of `x`