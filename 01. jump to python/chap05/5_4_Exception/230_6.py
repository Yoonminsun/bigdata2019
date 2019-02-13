input_denominator = int(input("분모를 입력하세요:"))
try:
    result = 4/input_denominator
    print(result)
    f=open('나없는파일.txt','r')
    f.close()
except ZeroDivisionError as e:
    print(e)
    print("분모가 0이 되어서는 안됩니다. 다시 입력하세요.")
except FileNotFoundError as e:
    print(e)
    print("해당 파일이 존재하지 않습니다.\n230_6.py가 있는 경로에 '나없는파일.txt' 파일이 있는지 확인하세요.")

print("프로그램 종료")

#try 구문을 쓰지 않는 경우
# result = system_cal()
#
# if result == -1:
#     print("에러 발생")
#     exit()
# else:
#     print(result)
# result = system_util()
# if result == -1:
#     print("에러 발생")
#     exit()
# else:
#     print(result)
# print("프로그램 종료")
