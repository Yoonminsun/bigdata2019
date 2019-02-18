import re
p=re.compile(r'(?P<one>\b\w+)\s+(?P=one)') # 그룹에 이름을 지정하고 재참조
print(p.search('Paris in the the spring').group())
