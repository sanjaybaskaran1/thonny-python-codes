"""exception handling in python using(try,except,else --> blocks)"""
fruits = ["Apple", "Pear", "Orange"]

def fruit_name(index):
    
    try:
        fruit = fruits[index]
    except IndexError as e:
        print(e,", check the index in list")
    finally:
        print("finally block will always execute.")
        print("which means if the except block executes or not the finally block will execute.")
        
    

fruit_name(5)


