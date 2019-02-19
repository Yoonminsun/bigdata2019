import re

p=re.compile('\d+$')
m = p.search('the cat')
if m:
    print('check')
else:
    print('not check')
m = p.search('tha cat3')
if m:
    print('check')
else:
    print('not check')
