try:
    result = 4/2
    print(result)
except ZeroDivisionError as e:
    print(e)

print("프로그램 종료")

#try 구문을 쓰지 않는 경우
# result = system_cal()
#
# if result == -1:
#     print("에러 발생")
#     exit()
# else:
#     print(result)
# print("프로그램 종료")