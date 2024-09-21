# OOP -- Object Oriented Programming   
# Four core principle of OOP 

# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism



class Person:
    def __init__(self, name, age):
        self.name=name #public attribute
        self.__age=age  #private attribute
    
    def age(self):
        return self.__age
    def name(self):
        return self.name

person1 = Person("Alice",21)
print(person1.name)
print(person1.age())