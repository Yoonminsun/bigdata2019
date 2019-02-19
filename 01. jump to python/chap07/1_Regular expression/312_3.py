import re
p=re.compile(r'\section') # \s가 공백문자를 표현하는 정규식이기 때문에
print(p.search('\section')) # Not Match
p=re.compile('\\section') # 정규식에서는 '\\'을 '\'로 인식하지 않는다
print(p.search('\section'))
p=re.compile(r'\section') # 정규식에서는 raw string 포맷을 사용해도 '\' 한개는 문자로 인식하지 않는다
print(p.search('\section'))
p=re.compile(r'\\section') # raw string 문법으로 보면 r'\\'은 '\\\\'의 의미 이지만
                           # 아래 '\' 가 한개인 string 에도 매치가 되지만 '\\'로 매치가 된다
print(p.search('\section'))
p=re.compile('\\\\section')
print(p.search('\\section'))
p=re.compile(r'\\section')
print(p.search('\\section'))
p=re.compile('\\\section')
print(p.search('\section'))
