# Combination of two or more types of inheritance
#-implementation of hybrid inheritance

# Hybrid inheritance allows a child class to inherit from multiple parent classes, which can also be part of a hierarchy.
# In this example, class D inherits from both B and C, which in turn inherit from A.
# This demonstrates a combination of multilevel and multiple inheritance.
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):  # Hybrid: multilevel + multiple
    def showD(self):
        print("Class D")

d = D()
d.showA()  
d.showB()  
d.showC() 
d.showD()  
