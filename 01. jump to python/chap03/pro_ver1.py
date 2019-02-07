#coding: cp949
age = int(input("나이를 입력하세요:"))

if age<=3 or age>=66: 		fee='무료'
elif age>=4 and age<=13: 	fee='2000원' 
elif age>=14 and age<=18: 	fee='3000원'
elif age>=19 and age<=65: 	fee='5000원'

print("요금은 %s 입니다."%fee)

