# Inheritance allows one class to inherit attributes and methods from another class
# this helps in reusing code and creating hierarchy of classes


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return f"you're driving a {self.brand} {self.model} which looks great"
    def test(self):
        return f"you're test driving {self.brand}"
class Car(Vehicle):
    def __init__(self, brand, model, horsepower):
        super().__init__(brand,model)
        self.horsepower = horsepower
    
    def accelerate(self):
        return f" {self.brand} {self.model} is accelerating with {self.horsepower}"

car1 = Car("Toyota", "Corolla", 180)
print(car1.accelerate())
print(car1.start())
print(car1.test())