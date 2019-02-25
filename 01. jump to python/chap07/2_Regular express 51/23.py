import re

data = 'Python Exercises'
p=re.compile(' |[_]')
m = p.finditer(data)
for i in m:
    if i.group()==' ':
        data = data[:i.start()]+'_'+data[i.start()+1:]
    elif i.group()=='_':
        data = data[:i.start()]+' '+data[i.start()+1:]
print(data)

