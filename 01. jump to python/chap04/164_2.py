f = open("./file3.txt",'r',encoding="UTF-8")
data = f.read() # 원본 전체를 문자열로 리턴
print(data)
f.close()
