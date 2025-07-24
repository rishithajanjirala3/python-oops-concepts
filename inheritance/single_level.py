#  inheritance allows one class (child/derived) to inherit attributes and methods from another class (parent/base).

#implementation of single level inheritance
#--One child class inherits from one parent class.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # from Animal
d.bark()   # from Dog
