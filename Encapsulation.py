#Wrapping data and methods together.
#Use _ or __ to make variables/methods protected/private.

class Father:
    def __init__(self):
        self._a=10 # protected 
        self.__b=20 # private 
    def _fun1(self):  # protected 
        print("this is our house")
    def __fun2(self): # private 
        print("this is my farm house") 
class Son(Father):
    def fun3(self):
        print("i have 20cr") 
#ob=Son() 
#ob._fun1()  
#print(ob._a)  
ob1=Father() 
ob1._Father__fun2()  # Data Mangling
