class Calculator:
    result_sum=0
    result_avg=0
    my_list=[]
    def __init__(self,my_list):
        self.my_list = my_list
    def sum(self):
        for i in self.my_list:
            self.result_sum += i
        print(self.result_sum)
    def avg(self):
        result_avg=self.result_sum / len(self.my_list)
        print(result_avg)

if __name__ == '__main__':
    cal1 = Calculator([1,2,3,4,5])
    cal1.sum()
    cal1.avg()
    cal2 = Calculator([6,7,8,9,10])
    cal2.sum()
    cal2.avg()