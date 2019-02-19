import re

file_names = ['foo.bar','autoexec.bat','sendmail.cf','hyunki.exe']

# 확장자가 bat 와 exe 파일을 제외해야 하는 조건 추가
# p = re.compile('.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$')
p = re.compile('.*[.](?!bat$).*$')
for file_name in file_names:
    print(p.search(file_name))
