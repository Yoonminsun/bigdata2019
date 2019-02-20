import re

data = 'Python exercises, PHP exercises, C# exercises'
p=re.compile('exercises')
m = p.finditer(data)
for i in m:
    if i:
        print(i.start(), i.end())
