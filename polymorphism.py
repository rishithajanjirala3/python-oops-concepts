# def:-one into many forms 
# 1)method overloading 2) method overriding 
 
class Methodoverload:
    def fun1(self,a=None,b=None,c=None):
        print(a,b,c) 
ob=Methodoverload() 
ob.fun1(10,20,30)
ob.fun1(10,20) 
ob.fun1(10) 
ob.fun1() 


class MethodOverride:
    def fun1(self):
        print("i love java!!!") 
class child(MethodOverride):
    def fun1(self):
        print("i love python!!!")
        super().fun1()  # To call parent class 
ob=child() 
ob.fun1() 