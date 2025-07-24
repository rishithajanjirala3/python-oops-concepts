# Constructor (__init__)
# Special method to initialize an object.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

e = Employee("Bob", 101)
print(e.name, e.id)