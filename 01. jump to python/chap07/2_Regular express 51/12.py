import re

p=re.compile('\w*z\w*')
m = p.search('The quick brown fox jumps over the lazy dog.')
print(m)
m = p.search('Python Exercises.')
print(m)
