import re

data = '**//Python Exercises// - 12. '

p=re.compile('\W')
print(p.sub('',data))


