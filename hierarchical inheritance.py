"""hierarchical inheritance -- multiple child class from single parent class"""
"""parent class"""
class showroom:
    def __init__(self,city,car):
        self.city_name = city
        self.car_name = car
    def showroom_details(self):
        print(f"{self.city_name} sells only {self.car_name}")
showrrom = showroom(city="showrrom",car=["ford","hyundai","tata","maruthi suzuki"])
showrrom.showroom_details()

"""child class 3"""
class chennai(showroom):
    def __init__(self,city, car):
        super().__init__(city, car)
chennai = chennai(city="chennai",car=["ford","tata"])
chennai.showroom_details()

"""child class 2"""
class delhi(showroom):
    def __init__(self,city,car):
        super().__init__(city,car)
delhi = delhi(city="delhi",car=["hyundai","maruthi suzuki"])
delhi.showroom_details()