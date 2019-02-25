import re

data =  'Clearly, he has no excuse for such behavior.' # 부사와 부사의 위치 출력

p=re.compile('[a-zA-Z]*ly')
m = p.finditer(data)
for n in m:
    print(n.span(),':',n.group())
