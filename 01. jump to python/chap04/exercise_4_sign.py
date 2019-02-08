def search_visitor(input_name):
    if read_visitor.find(input_name)==-1:
        return ''
    else:
        return input_name


f = open("./방명록.txt",'r',encoding='UTF-8')
read_visitor = f.read()
f.close()

input_name = input("이름을 입력하세요:")
name = search_visitor(input_name)

if name=='':
    f = open("./방명록.txt",'a',encoding='UTF-8')
    birth = input("생년월일을 입력하세요 (예:801212):")
    print("%s님 환영합니다. 아래 내용을 입력하셨습니다."%input_name)
    print("%s %s"%(input_name,birth))
    f.write("%s %s\n"%(input_name,birth))
    f.close()


else:
    print("%s님 다시 방문해 주셔서 감사합니다. 즐거운 시간 되세요."%input_name)