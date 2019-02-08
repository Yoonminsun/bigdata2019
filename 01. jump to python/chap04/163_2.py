f = open("./file3.txt",'r',encoding="UTF-8")
while True:
    line = f.readline()
    if not line:
        break
    print(line,end='') # 원본에 \n이 있기 때문에 원본 그대로 출력하기 위해서 end='' 추가
f.close()