# polymporhism allows different classes to be treated as instance of the same class
# through a common interface 

class Bird:
    def fly(self):
        return "Bird in the sky"

class Airplane:
    def fly(self):
        return "Airplane flying through engines"
    
bird =Bird()
airplane= Airplane()

print(bird.fly())
print(airplane.fly())