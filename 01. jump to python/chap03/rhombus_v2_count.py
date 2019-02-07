#coding: cp949

while True:
    input_odd = int(input("홀수를 입력하세요(0<-종료):"))
    
    sc=1
    bc=(input_odd - sc)//2

    if not input_odd: #0 입력시 종료
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다.")
        break

    print((''*bc)+('*'*sc))
    bc-=1
    sc+=2

        



    
