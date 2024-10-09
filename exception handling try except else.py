"""exception handling in python using(try,except,else --> blocks)"""
fruits = ["Apple", "Pear", "Orange"]

def fruit_name(index):
    
    try:
        fruit = fruits[index]
    except IndexError as e:
        print(e)
    else:
        print("else block will only execute if there is no error.")
        print("which means if the except block execute then else block will not execute.")

fruit_name(1)