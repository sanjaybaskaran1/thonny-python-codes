names = ["sanjay","krishna","jack","joo"]

user_input = input("Enter a name: ")

if user_input in names:
    print(f"{user_input}, is there in names")
else:
    print(f"{user_input}, is not there in names")