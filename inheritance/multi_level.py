#A child class inherits from a parent, and then another class inherits from that child
#-Implementation of multi level inheritance
class Grandparent:
    def show_grandparent(self):
        print("Grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent")

class Child(Parent):
    def show_child(self):
        print("Child")

c = Child()
c.show_grandparent()
c.show_parent()
c.show_child()
