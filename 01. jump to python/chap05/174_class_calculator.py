class Calculator: # 사용자 정의 클래스
    def __init__(self): # 생성자(Constructor) 객체 생성시 최초로 수행되는 함수
        self.result = 0 # Class의 멤버 변수

    def adder(self,num): # Class의 멤버 함수(Member Function)
        print("%d값을 입력 받았습니다."%num)
        self.result += num
        self.num1=3 # 멤버변수로 등록은 가능하나 가독성은 떨어짐. 또한 adder함수 최소 1번 호출 후 사용 가능
        return self.result

cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()

print(cal1.adder(3))
print(cal1.num1)
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
print(cal3.adder(3))
print(cal3.adder(2))