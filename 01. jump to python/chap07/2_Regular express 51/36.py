import re

data = 'PythonExercises'

p=re.compile('([A-Z][a-z]\w*)([A-Z][a-z]\w*)')
print(p.sub('\g<1>_\g<2>',data).lower())

