#abstraction
#feature
from abc import abc,abstractmethod
class payment(abc):
    @abstractmethod 
    def pay(self):
        pass
class UPI (payment):
    def pay(self):
        print("payment done using upi")
class phonepe(payment):
    def pay(self):
        print("payment done using phonepe")
payment=UPI()
payment.pay()
payment=phonepe
payment.pay 