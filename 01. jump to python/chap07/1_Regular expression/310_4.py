import re
p= re.compile('.*python$',re.MULTILINE)
# p= re.compile('.*python$')

data = '''python one python debug
life is too short
python two
you nees python
python three
I will study python'''

print(p.findall(data))
