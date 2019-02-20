import re

p=re.compile('\w')
m=p.search('ABCDEFabcdef123450')
print(m)
m=p.search('*&%@#!}{')
print(m)
