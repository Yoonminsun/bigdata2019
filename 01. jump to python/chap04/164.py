f = open("./file3.txt",'r',encoding="UTF-8")
lines = f.readlines() # 모든 라인을 list에 저장한다
# print(lines)
for line in lines:
    print(line,end='')
f.close()
