i,j = map(int,input("i,j 입력 (공백 구분): ").split(' ')) #input받은 문자열을 split 한 후 int함수를 거쳐 i,j에 들어가는 것
cycle = 1
cycle_list=[]

for n in range (i,j+1):
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        cycle+=1
    cycle_list.append(cycle)
    cycle=1

print(max(cycle_list))

# 내장함수 map,input,list,max 사용