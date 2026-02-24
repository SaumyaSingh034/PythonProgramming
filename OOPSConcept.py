class Calculator:

    number = 200

    def __init__(self, a,b):
        print("I am called automatically when object is created")
        self.firstNumber = a
        self.secondNumber = b

    def getData(self):
        print("Hey We are in get Data Method of Class")

    def summation(self):
        print("Hey We are in summation Method of Class")
        return self.firstNumber + self.secondNumber + self.number

obj = Calculator(2,3) #way to create object in python
obj.getData()
print(obj.number)
print(obj.summation())

obj1 = Calculator(9,10) #way to create object in python
obj1.getData()
print(obj1.number)
print(obj1.summation())