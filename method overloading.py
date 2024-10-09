"""method overloading"""
class CALCULATOR:
    def multiply(self,*numbers):
        if len(numbers)==2:
            result = numbers[0]*numbers[1]
            print(f"{numbers[0]}*{numbers[1]} = {result}")
        elif len(numbers)==3:
            result = numbers[0]+numbers[1]+numbers[2]
            print(f"{numbers[0]}+{numbers[1]}+{numbers[2]} = {result}")
        else:
            print(f"Enter only 3 or 2 inputs")
    
            

calculator = CALCULATOR()
calculator.multiply(1,2)
calculator.multiply(1,2,3)
