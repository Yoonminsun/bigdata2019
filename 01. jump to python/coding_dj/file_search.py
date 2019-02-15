import os

in_text=''
for (path,dir,files) in os.walk("./"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext=='.txt':
            f = open('%s%s'%(path,filename))
            in_text = f.read()
            f.close()
            if in_text.find('LIFE IS TOO SHORT') != -1:
                print(filename)

# 외장함수인 os의 walk 함수를 이용함. .txt인 파일 중 read 한 후
# 'LIFE IS TOO SHORT'라는 문자열이 있는지 find
# find 함수는 해당 문자열이 없는경우 -1을 리턴하므로 리턴값에  따라 출력함