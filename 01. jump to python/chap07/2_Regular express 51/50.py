import re

data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# [], ()영역 , ""제거하기
p=re.compile('\w+')
for in_str in data:
    m = p.search(in_str)
    print(m.group())
