#coding: cp949

while True:
    input_odd = int(input("Ȧ���� �Է��ϼ���(0<-����):"))
    
    sc=1
    bc=(input_odd - sc)//2

    if not input_odd: #0 �Է½� ����
        print("������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
        break

    print((''*bc)+('*'*sc))
    bc-=1
    sc+=2

        



    
