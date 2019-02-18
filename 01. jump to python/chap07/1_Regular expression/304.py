import re

p = re.compile('[a-z]+')
# m=p.match('python')
m=p.match('3 python')
print('1.',m)
if m:
    print("Match Found: ",m.group())
else:
    print("No Match")