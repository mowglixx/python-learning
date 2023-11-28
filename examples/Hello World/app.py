# how to store a variable
greeting = "hello world"
my_age = 33


# print the variable to the screen (in the console/terminal)
print(greeting, greeting.title(), greeting, my_age)


################################################################
# defining what a function does called greeter


def greeter(username: str):
    # returning a value
    return f"Hello, {username.title()}"


# delaring a `List` or users
users = ["dave", "jimmy38", "big_Dog12", "mowglixx"]
greetedUsersCount = 0

# for eachUser in the users list
for eachUser in users:
    # `call` the `greeter` function to greet `eachUser`
    print(greeter(eachUser))
    greetedUsersCount = greetedUsersCount + 1

print(f"We have greeted {greetedUsersCount} Users this time! 😃")
