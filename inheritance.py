class CarShowroom:
    def chennai(self):
        print("Chennai sells only Nano and Tata")
    
    def delhi(self):
        print("Delhi sells only Benz and Audi")

class Chennai(CarShowroom):
    def __init__(self):
        
        self.chennai()# Call the superclass method within the instance method

# Create an instance of the Chennai class
chennai_showroom = Chennai()