from abc import *

class payment(ABC):
    @abstractmethod
    def payment_gateway(self,payment_type):
        pass
    def display(self):
        print("your payment is successfull")

class card(payment):
    def payment_gateway(self,payment_type):
        print(payment_type)
        
        
class phone_pay(payment):
    def payment_gateway(self,payment_type):
        print(payment_type)
        
    
phone_pay = phone_pay()
phone_pay.payment_gateway("phone pay")
phone_pay.display()
card = card()
card.payment_gateway("credit card")
card.display()