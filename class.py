class Calculator:

    #constructor
    def __init__(self, num1,num2,num3,num4):
        self.num1=num1
        self.num2=num2
        self.num3= num3
        self.num4=num4

    #methods  
    def add(self):
        return self.num1 + self.num2 +self.num3 +self.num4
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
    
calc = Calculator(50,25,10,20)



# def add(a,b):
#     return a+b



print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())
# print(add(60,40))




