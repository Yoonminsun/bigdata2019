# 입력(parameter),출력(return)이 없는 함수
def my_sum():
    # 함수 정의(define), python은 함수 선언부 없음.
    num1, num2 = input("두 수를 입력하세요: ").split()
    print("num1+num2=%d"%(int(num1)+int(num2)))
    # print("num1+num2=%d"+(int(num1)+int(num2))) # 오류 구문을 따로 sample 로 만들어 디버그

print("입력(parameter),출력(return)이 없는 함수테스트")
my_sum()