import re

p=re.compile('[a-c]') # a,b,c
m=p.match('a') # 첫글자가 a 이므로 매칭O
print(m)
m=p.match('b') # 첫글자가 b 이므로 매칭O
print(m)
m=p.match('c') # 첫글자가 c 이므로 매칭O
print(m)
print()

p=re.compile('[1-3]') # 1,2,3
m=p.match('1')
print(m)
m=p.match('2')
print(m)
m=p.match('3')
print(m)
