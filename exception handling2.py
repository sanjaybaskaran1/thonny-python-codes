"""exception handling with {try,except,else}--> blocks"""

fruits_list = ["apple","banana","cherry"]

def fruit_name(index):
    try:
        print("fruit_name =",fruits_list[index])
    except IndexError as e:
        print(e,", use the proper indexing for the list")
    else:
        print("else block will execute only there is no error")
        
fruit_name(5)
    

