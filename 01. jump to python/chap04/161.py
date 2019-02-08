f = open('./file3.txt','w',encoding="UTF-8")
# Python에서 한글 설정을 하려면 환경설정에서 file encoding을 EUC-KR로 변환
# 또는 파일 open 마다 encoding="UTF-8" 입력
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()