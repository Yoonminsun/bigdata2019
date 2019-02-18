import re

p = re.compile('[a-z]+')
m=p.search('3 python') # search는 문자열 전체를 검색하기때문에 매칭O
print('1.',m)
if m:
    print("Match Found: ",m.group())
else:
    print("No Match")