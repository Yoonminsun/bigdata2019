def addition(input_1,input_2):
    error_flag = 0
    try:
        input_1 = int(input_1)
    except ValueError:
        error_flag=1
        print("1번째 입력이 [%s]입니다. 숫자를 입력하세요." % input_1)
    try:
        input_2 = int(input_2)
    except ValueError:
        error_flag=1
        print("2번째 입력이 [%s]입니다. 숫자를 입력하세요." % input_2)
    if error_flag==0:
        print("%d + %d = %d"%(input_1,input_2,input_1+input_2))


my_str =  input("두 수를 입력하세요 ('종료' 입력시 프로그램 종료): ")
if my_str == '종료':
    print("프로그램을 종료합니다.")
    exit()
else:
    num1,num2 = my_str.split(' ')

addition(num1,num2)


