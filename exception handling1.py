"""exception handling with {try,except,finally}--> blocks"""

fruits_list = ["apple","banana","cherry"]

def fruit_name(index):
    try:
        print("fruit_name =",fruits_list[index])
    except IndexError as e:
        print(e,", use the proper indexing for the list")
    finally:
        print("finally will always execute whether there is error or not")
        
fruit_name(5)
    
