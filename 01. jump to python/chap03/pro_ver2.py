#coding: cp949

age = int(input("나이를 입력하세요:"))
fee='무료'

if age<0: 
    print("다시 입력하세요")
    quit()
elif age<=3 : 
    grade='유아'
elif age>=4 and age<=13: 
    fee='2000원'  
    grade='어린이' 
elif age>=14 and age<=18: 
    fee='3000원' 
    grade='청소년'
elif age>=19 and age<=65:
    fee='5000원' 
    grade='성인'
else: 
    grade='노인'

print("귀하는 %s 등급이며 요금은 %s 입니다."%(grade,fee))

