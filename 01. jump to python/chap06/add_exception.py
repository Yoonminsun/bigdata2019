class not_int(Exception):
    pass

class My_class:
    def __init__(self,input_1,input_2):
        self.input_1 = input_1
        self.input_2 = input_2
        try:
            self.input_1 = int(self.input_1)
        except ValueError:
            print("1번째 입력이 [%s]입니다. 숫자를 입력하세요."%num1)
        try:
            self.input_2 = int(self.input_2)
        except ValueError:
            print("2번째 입력이 [%s]입니다. 숫자를 입력하세요."%num2)

    def addition(self,input_1,input_2):
     return  input_1 + input_2





try:
    num1,num2 = input("두 수를 입력하세요 ('종료' 입력시 프로그램 종료): ").split(' ')
    my_add = My_class(num1,num2)


