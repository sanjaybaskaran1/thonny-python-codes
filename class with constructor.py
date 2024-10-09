"""create a class to check the availabilty of the car in  showroom
if the car is available in that showroom provide details of that car"""
class CAR_DETAILS:
    """constructor method of the class"""
    def __init__(self,car_name,showroom_name):
        self.location = showroom_name
        self.name = car_name
        self.showroom ={
                         "chennai":{"suzuki":700000,"ford":2000000,"bmw":5000000},
                         "delhi":{"suzuki":700000,"ford":2000000,"bmw":5000000}
                       }
    
    def car_details(self):
        if self.location in self.showroom.keys():
            if self.name in self.showroom[self.location].keys():
                print(f"{self.name}, is available in our {self.location} showroom.")
                print(f'{self.name}, price is {self.showroom[self.location][self.name]}')
            else:
                print(f"we dont have, {self.name} car stock.")
        else:
            print(f"we only have branch in chennai and delhi.")

"""customer want to know price of hyundai"""           
car1 = CAR_DETAILS(car_name = "hyundai", showroom_name = "chennai")
car1.car_details(), print(' ')

"""customer want to know price of bmw"""
car2 = CAR_DETAILS(car_name = "bmw", showroom_name = "delhi")
car2.car_details(), print(' ')

"""check for audi car"""
car3 = CAR_DETAILS(car_name = "audi", showroom_name = "mumbai")
car3.car_details()