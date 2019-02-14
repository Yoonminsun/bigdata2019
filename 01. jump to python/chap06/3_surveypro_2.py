from surveypro import survey

choice_menu=0
my_path = ''
def read_content():
    try:
        if my_path=='':
            f = open('./poll.txt','r',encoding='UTF-8')
        else:
            f = open('./%s/poll.txt'%my_path,'r',encoding='UTF-8')
    except FileNotFoundError:
        print("기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.")
        choice_menu = int(input("1.종료  2.새로운 파일 생성  3.변경된 파일 경로 입력:"))
        return choice_menu
    else:
        print('<현재 누적 응답 현황>\n'+f.read())
        f.close()


choice_menu = read_content()

if choice_menu == 1:
    exit()
elif choice_menu == 2:
    survey(my_path)
    read_content()
elif choice_menu == 3:
    my_path = input("경로 입력: ")+'/'
    read_content()
    survey(my_path)
    read_content()
