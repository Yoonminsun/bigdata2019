def sum_and_mul(*args):
    sum=0
    mul=1
    for i in args:
        sum+=i
        mul*=i
    return sum,mul # 튜플 형태로 return 된다


input_list = list(map(int,input("리스트 입력:").split())) #리스트로 입력받음
sum,mul=sum_and_mul(*input_list) # 입력받은 리스트를 인자로 함수 호출하여 튜플값 각각 대입
print("sum= %d mul=%d"%(sum,mul)) # 출력