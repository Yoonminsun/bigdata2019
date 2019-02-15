from surveypro import survey

choice_menu=0
my_path = '.'
def read_content():
    try:
        f = open('%s\poll.txt'%my_path,'r',encoding='UTF-8')
        # D:\Python_local_repository\01. jump to python\chap06\new_repo
        #.\new_repository\
    except FileNotFoundError:
        print("기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.")
    else:
        print('<현재 누적 응답 현황>\n'+f.read())
        f.close()



while True:
    read_content()
    choice_menu = int(input("1.종료  2.새로운 파일 생성  3.변경된 파일 경로 입력:"))
    if choice_menu == 1:
        exit()
    elif choice_menu == 2:
        survey(my_path)
    elif choice_menu == 3:
        my_path = input("경로 입력: ")
        read_content()
        survey(my_path)
