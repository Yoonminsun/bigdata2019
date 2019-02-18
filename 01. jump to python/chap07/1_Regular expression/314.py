import re
p=re.compile('Crow|Servo')

m=p.match('Nothing')
print(m)
m=p.match('Crow')
print(m)
m=p.match('Servo')
print(m)
m=p.match('CrowServo')
print(m)
m=p.search('CrowServo')
print(m)
m=p.findall('CrowServo')
print(m)
m=p.finditer('CrowServo')
print(m)

