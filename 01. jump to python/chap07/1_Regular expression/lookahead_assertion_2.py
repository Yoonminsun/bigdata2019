import re

file_names = ['foo.bar','autoexec.bat','sendmail.cf','minsun.','hyunki.exe']

# 확장자가 bat 와 exe 파일을 제외해야 하는 조건 추가
p = re.compile('.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$')
# 유닉스 시스템에서 파일명이 .으로 끝나는 파일은 필터링 되는 오류가 발생될 수 있다
# 필터링하고 싶은 확장자의 조건이 추가될수록 정규식은 기하급수적으로 복잡해진다.
for file_name in file_names:
    print(p.search(file_name))
