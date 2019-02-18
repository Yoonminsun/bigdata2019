import re
# p= re.compile('^python\s\w+')
p= re.compile('^python\s\w+',re.MULTILINE)

data = '''python one python debug
life is too short
python two
you nees python
python three'''

print(p.findall(data))
# MULTILINE을 쓰더라도 python debug의 python은 문자열 처음이 아니므로 findall로도 리턴되지 않음