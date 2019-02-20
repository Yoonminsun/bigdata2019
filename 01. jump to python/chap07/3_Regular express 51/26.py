import re

data = ["Python PHP", "Java JavaScript", "c c++"]

p = re.compile('(P.*) (P.*)')
for i in data:
    m= p.search(i)
    if m:
        print(m.group(1),',',m.group(2))

