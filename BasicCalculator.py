class BasicCalculator():
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def addition(self):
        return self.first + self.second
    def subtraction(self):
        return self.first - self.second
    def multiplication(self):
        return self.first * self.second
    def division(self):
        return self.first / self.second

obj = BasicCalculator(10,5)
print("{} {}".format("Addition: 10 + 5 = ",obj.addition()))
print("{} {}".format("Subtraction: 10 - 5 = ",obj.subtraction()))
print("{} {}".format("Multiplication: 10 * 5 = ",obj.multiplication()))
print("{} {}".format("Division: 10 / 5 = ",obj.division()))