from OOPSConcept import Calculator


class ChildImplementation(Calculator):
    number2 = 900



    def getCompleteData(self):
        return self.number2 + self.number + self.summation()

print("**********************************")
obj = ChildImplementation(2,3)
print(obj.getCompleteData())