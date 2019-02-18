import re
# p= re.compile('^python\s\w+') # 문자열 처음이 python이며 뒤에 whitespace 후에 문자or숫자가 1개이상 오는 경우
p= re.compile('^python\s\w+',re.MULTILINE)

data = '''python one
life is too short
python two
you nees python
python three'''

print(p.findall(data))