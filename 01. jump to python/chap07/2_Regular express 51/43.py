import re

data =  'PythonTutorialAndExercises'

p=re.compile('([A-Z][a-z]*)')
m=p.findall(data)
print(m)
