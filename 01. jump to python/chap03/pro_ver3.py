#coding: cp949

age = int(input("���̸� �Է��ϼ���:"))
fee='����'

if age<0: 
    print("�ٽ� �Է��ϼ���")
    quit() 
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

if fee!='����' :
    sfee = int(input("����� �Է��ϼ���:"))
    ifee=int(fee[:4])

    if ifee==sfee:
        print("�����մϴ�. Ƽ���� �����մϴ�.")
    elif ifee>sfee:
        print("%d���� ���ڶ��ϴ�. �Է� �Ͻ� %d���� ��ȯ�մϴ�."%((ifee-sfee),sfee))
    else:
        print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ �մϴ�."%(sfee-ifee))

else: print("�����մϴ�. Ƽ���� �����մϴ�.")
