class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    # def setdata(self,first,second):
    #     self.first = first
    #     self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first // self.second
        return result

a=FourCal(4,2)
b=FourCal(3,7)
# a.setdata(4,2)
# b.setdata(3,7)
print(a.sum(),a.mul(),a.sub(),a.div())
print(b.sum(),b.mul(),b.sub(),b.div())