#-Multiple inheritance allows a child class to inherit attributes and methods from more than one parent class
#-Implementation of multiple inheritance

class Father:
    def show_father(self):
        print("Father")

class Mother:
    def show_mother(self):
        print("Mother")

class Child(Father, Mother):
    def show_child(self):
        print("Child")

c = Child()
c.show_father()
c.show_mother()
c.show_child()
