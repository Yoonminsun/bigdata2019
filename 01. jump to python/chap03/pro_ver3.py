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

if fee!='무료' :
    sfee = int(input("요금을 입력하세요:"))
    ifee=int(fee[:4])

    if ifee==sfee:
        print("감사합니다. 티켓을 발행합니다.")
    elif ifee>sfee:
        print("%d원이 모자랍니다. 입력 하신 %d원을 반환합니다."%((ifee-sfee),sfee))
    else:
        print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환 합니다."%(sfee-ifee))

else: print("감사합니다. 티켓을 발행합니다.")
