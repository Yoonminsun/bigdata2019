sum=0
digit_num = int(input("정수의 개수: "))
digit_list = input('정수 입력(갯수만큼, 공백나눔):').split(' ')
for num in digit_list:
    sum+=int(num)
print("정수 합:%d  평균 값:%f"%(sum,sum/digit_num))
del digit_list