"""print numbers between 10 to 1 using recursive function"""
def recursive_numbers(number):
    if number > 0:
        print(number)
        recursive_numbers(number=number-1)
        
recursive_numbers(number=10)