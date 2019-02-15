class calculator:
    error_flag=0
    def __init__(self,input_1,input_2):
        self.input_1 = input_1
        self.input_2 = input_2
    def input_cal(self,input_1,input_2):
        try:
            self.input_1 = int(self.input_1)
        except ValueError:
            self.error_flag = 1
            print("1번째 입력이 [%s]입니다. 숫자를 입력하세요." % input_1)
        try:
            self.input_2 = int(self.input_2)
        except ValueError:
            self.error_flag = 1
            print("2번째 입력이 [%s]입니다. 숫자를 입력하세요." % input_2)

class Add(calculator):
    def cal(self):
        print("%d + %d = %d" %(self.input_1,self.input_2,self.input_1+self.input_2))
class Sub(calculator):
    def cal(self):
        print("%d - %d = %d" % (self.input_1, self.input_2, self.input_1 - self.input_2))
class Mul(calculator):
    def cal(self):
        print("%d * %d = %d" % (self.input_1, self.input_2, self.input_1 * self.input_2))
class Div(calculator):
    def cal(self):
        try:
            self.result = self.input_1/self.input_2
        except ZeroDivisionError:
            print("죄송합니다. 두번째 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 안됩니다.")
        else:
            print("%d / %d = %d" % (self.input_1, self.input_2, self.result))

my_str = input("두 수를 입력하세요. (나누기는 분자 분모 입력)('종료' 입력시 프로그램 종료): ")
if my_str == '종료':
    print("프로그램을 종료합니다.")
    exit()
else:
    num1, num2 = my_str.split(' ')

my_choice = input("적용할 연산을 입력하세요:")
if my_choice=='+':
    my_class = Add(num1,num2)
elif my_choice == '-':
    my_class = Sub(num1,num2)
elif my_choice == '*':
    my_class = Mul(num1, num2)
elif my_choice == '/':
    my_class = Div(num1, num2)
else:
    print("없는 연산 입니다.")
    exit()

my_class.input_cal(num1,num2)
if my_class.error_flag==0:
    my_class.cal()
