import re

data = """
one.py
two.text
three.py
four.exe
"""

p = re.compile('.*[.].*',re.MULTILINE)
m=p.findall(data)
print('모든 data 파일: ',m,'\n')

# data 중에 .py 파일만 골라내기
p = re.compile('.*[.](?=py).*',re.MULTILINE) # 긍정형 전방탐색
m=p.findall(data)
print('data 중 .py인 파일: ',m,'\n')
p = re.compile('.*[.](?!text|exe).*',re.MULTILINE) # 부정형 전방탐색
m=p.findall(data)
print('data 중 .py인 파일: ',m,'\n')

# data 중에 .py 가 아닌 파일만 골라내기
p = re.compile('.*[.](?=text|exe).*',re.MULTILINE) # 긍정형 전방탐색
m=p.findall(data)
print('data 중 .py가 아닌 파일: ',m,'\n')
p = re.compile('.*[.](?!py).*',re.MULTILINE) # 부정형 전방탐색
m=p.findall(data)
print('data 중 .py가 아닌 파일: ',m,'\n')

# data 중에 .py의 파일 이름만 골라내기
p = re.compile('.*[.](?=py)',re.MULTILINE) # 긍정형 전방탐색
m=p.findall(data)
print('data 중 .py인 파일의 이름: ',m,'\n')
p = re.compile('(?P<name>.*)[.](?=py).*',re.MULTILINE) # 긍정형 전방탐색
m=p.search(data)
print('data 중 .py인 첫번째 파일의 이름: ',m.group('name'),'\n')