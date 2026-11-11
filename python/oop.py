# Object-oriented programming is a programming approach in which we organise programs using classes and objects.
# A class is a blueprint or template used to create objects. An object is an instance of a class.
# A method is a function defined inside a class.
# Class names are case-sensitive.
# self refers to the current object that is calling a method. It allows an object to access its own attributes and methods inside a class.
# self is used inside instance methods, not in the class declaration.

class Student():
    def greet(self): # method
        print("Hello ", self.name)

s1 = Student()
s1.name = "John"
s1.greet()

s2 = Student()
s2.name = "Doe"
s2.greet()

# Inheritance means one class(child) can inherit properties of another class(parent).
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal): # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.bark() ; d.sound() # d can use methods of Dog() and Animal()
c.meow() ; c.sound()

# Magic methods are special methods with double underscores (Eg. init, add, str )
# __init__ method is always executed when the class is being initiated. 
# Used to assign values to object properties, or to perform operations that are necessary when the object is being created.
# Without the __init__(), you would need to set properties manually for each object; With __init__(), you can set initial values when creating the object
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Adam",23) # Possible because __init__() was used
p2 = Person("Alex",60)
print(p1.name , p1.age)
print(p2.name , p2.age)

# Polymorphism means the same function or method name can behave differently depending on the object.
# With polymorphism, you can use a common method name [pay()] and allow each class [payment] to implement it differently.

class UPI():
    def pay(self):
        print("Paid using UPI")

class Card():
    def pay(self):
        print("Paid using card")

class Cash():
    def pay(self):
        print("Paid using cash")

p1 = UPI()
p2 = Card()
p3 = Cash()
p1.pay() ; p2.pay() ; p3.pay() # Same method but result is different


# Abstraction hides internal implementation details and shows only the essential features to the user.
# The child class must have the abstarct method class in it, else a error will be given

# Abstraction is useful because the parent class decides all child class should have a comman class.
# The child class decides how the abstract class is implemented. This gives consistency across child classes.

import abc # imported Abstract Base Classes

class shape(abc.ABC): # ABC is used as a base(parent) class for creating abstract classes.
    @abc.abstractmethod # This is a decorator used to declare abstract methods.
    def area(self):
        pass

# Square inherits from Shape. Since Shape has an abstract method called area(), the Square class must implement it.
class Square(shape):
    def area(self):
        print("Area of square is side * side")

class Rectangle(shape):
    def area(self):
        print("Area of rectangle is length * breadth")

s = Square()
s.area()
r = Rectangle()
r.area()