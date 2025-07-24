# ABSTRACTION:- 
# Hiding the unwanted info and showing the req info 
# There is no object for a abstract class 
# There is no body for the abstract method   
# A class is known as abstract class if it 
#      has atleast one abstract method     


from abc import ABC,abstractmethod 
class Car(ABC):
    @abstractmethod 
    def mileage(self):
        pass 
class BMW(Car):
    def mileage(self):
        print("i go 45kmph") 
class TESLA(Car):
    def mileage(self):
        print("i go 60kmph") 
ob=BMW()   
ob.mileage()  