#coding: cp949
age = int(input("���̸� �Է��ϼ���:"))

if age<=3 or age>=66: 		fee='����'
elif age>=4 and age<=13: 	fee='2000��' 
elif age>=14 and age<=18: 	fee='3000��'
elif age>=19 and age<=65: 	fee='5000��'

print("����� %s �Դϴ�."%fee)

