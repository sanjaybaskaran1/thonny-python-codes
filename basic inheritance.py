class PHONE:
    def __init__(self,name,model,price):
        self.name = name
        self.price = price
        self.model = model
    def display(self):
        print("phone name = ",self.name)
        print("model name = ",self.model)
        print("price = ",self.price)
        
        
class SMART_PHONE(PHONE):
    def __init__(self,name,model,price,ram,rom):
        super().__init__(name,model,price)
        self.ram = ram
        self.rom = rom
    

nokia = SMART_PHONE("NOKIA","A11",10000,"4gb","128gb")
nokia.display()
print("ram = ",nokia.ram)
print("rom = ",nokia.rom)


    
        