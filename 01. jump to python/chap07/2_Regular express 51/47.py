import re

data =  'The quick brown\nfox jumps*over the lazy dog.'

p=re.compile('\\n|[*]|;|,') # 구분자를 기준으로 나누기
m = p.split(data)
print(m)
