#Class is a blueprint.
#Object is an instance of a class.

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)

# Object creation
p1 = Person("Alice")
p1.say_hello()
