import re

data = 'The following example creates an ArrayList with a capacity of 50 elements. ' \
       'Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.'

p = re.compile('\W+(?=a|e)\w*')
m=p.findall(data)
print(m)

