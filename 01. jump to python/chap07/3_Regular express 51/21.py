import re

data = 'Python exercises, PHP exercises, C# exercises'
p=re.compile('exercises')
for i in data.split(','):
    m = p.search(i)
    if m:
        print("Found Excercises")
