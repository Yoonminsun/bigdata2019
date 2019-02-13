try:
    result = 4/2
    print(result)
    f=open('나없는파일.txt','r')
    f.close()
except Exception as e:
# 모든 Failure를 동일하게 처리하고 싶을때, Exception의 유형을 정확히 모를 때 유용함
# (일반적인 상황에서 적용할 수 있는 Tip)
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
# result = system_util()
# if result == -1:
#     print("에러 발생")
#     exit()
# else:
#     print(result)
# print("프로그램 종료")
