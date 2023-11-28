# defining what a function does called greeter
def greeter(username: str):
    # returning a value
    return f"Hello, {username.title()}"

# delaring a `List` of users
users = ["dave", "jimmy38", "big_Dog12", "mowglixx"]

# for eachUser in the users list
for eachUser in users:
    # `call` the `greeter` function to greet `eachUser`
    print(greeter(eachUser))