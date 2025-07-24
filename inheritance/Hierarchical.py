# Hierarchical Inheritance Example
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Multiple child classes inherit from the same parent class (Hierarchical Inheritance)
dog = Dog()
cat = Cat()

dog.speak()  # Inherited from Animal
dog.bark()

cat.speak()  # Inherited from Animal
cat.meow()  