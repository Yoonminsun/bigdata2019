import re

file_names = ['foo.bar','autoexec.bat','sendmail.cf','hyunki.exe','min.']

# 확장자가 bat 와 exe 파일을 제외해야 하는 조건 추가
# p = re.compile('.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$')
p = re.compile('.*[.](?!bat$|exe$).*$') # 부정형 안에서 $를 붙여주지 않으면 batt, exee같은 경우도 필터링 되버린다
for file_name in file_names:
    print(p.search(file_name))
