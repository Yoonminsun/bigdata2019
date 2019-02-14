def survey(ori_path):
    f = open('./%spoll.txt'%ori_path, 'a', encoding='UTF-8')
    answer = ''
    name = ''

    while True:
        answer = input("프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료): ")
        if answer == '종료' and ori_path!='':
            return
        if answer == '종료':
            exit()
        name = input("이름을 입력하세요: ")

        f.write('[%s] %s\n' % (name, answer))
        print("설문에 응답해 주셔서 감사합니다.")
        print('[%s] %s\n' % (name, answer))



if __name__ == '__main__':
        survey('')