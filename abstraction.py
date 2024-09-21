# abstraction is the concept of hiding complex implementation details and exposing 
# only the necessary features of an object

from abc import ABC, abstractmethod 

class Animal(ABC):
    @abstractmethod

    def sound(self):
        pass #Abstract method must be implemented by subclasses

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

#using abstraction 
d = Dog()
cat = Cat()
print(d.sound())
print(cat.sound())


