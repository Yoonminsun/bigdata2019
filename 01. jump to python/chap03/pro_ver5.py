#coding: cp949

fticket=3
dticket=5
count=0

while True:
    age = int(input("���̸� �Է��ϼ���:"))
    fee = '����'
    buy = 1

    if age<0: 
        print("�ٽ� �Է��ϼ���")
        continue 
    elif age<=3 : 
        grade='����'
    elif age>=4 and age<=13: 
        fee='2000��'  
        grade='���' 
    elif age>=14 and age<=18: 
        fee='3000��' 
        grade='û�ҳ�'
    elif age>=19 and age<=65:
        fee='5000��' 
        grade='����'
    else: 
        grade='����'

    print("���ϴ� %s ����̸� ����� %s �Դϴ�."%(grade,fee))

    if fee!='����':
        count+=1
        ifee=int(fee[:4])
        select = int(input("��� ������ �����ϼ���. (1:����, 2:���� ���� �ſ�ī��)"))

        if select==1:

                sfee = int(input("����� �Է��ϼ���:"))

                if ifee==sfee:
                    print("�����մϴ�. Ƽ���� �����մϴ�.")
                elif ifee>sfee:
                    print("%d���� ���ڶ��ϴ�. �Է� �Ͻ� %d���� ��ȯ�մϴ�."%((ifee-sfee),sfee))
                    buy = 0
                    count-=1
                else:
                    print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ �մϴ�."%(sfee-ifee))

        elif select==2:
             dfee=ifee*0.9
             if age>=60 and age<=65: dfee*=0.95

             print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�."%dfee)

    else: print("�����մϴ�. Ƽ���� �����մϴ�.")

    if fticket and count%7==0 and fee!='����' and buy:
        fticket-=1
        print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��"%fticket)

    elif dticket and count%4==0 and fee!='����'and buy:
        dticket-=1
        print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��"%dticket)

