s = [1,3,4,7,13,17,20]
# s=[1,2,5,8,9,13,15,16]
distance=[]
min_index = []
for i in range(len(s)-1):
    distance.append(s[i+1]-s[i])

for dindex,dvalue in enumerate(distance):
    if dvalue==min(distance):
        print("(%d,%d)"%(s[dindex],s[dindex+1]))

## 원하는 값이 있는 인덱스를 찾는데 여러개일때__enumerate 내장 함수 사용
