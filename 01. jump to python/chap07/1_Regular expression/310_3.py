import re
# p= re.compile('python$') # python 으로 끝나는 문자열, data는 three로 끝나므로 매칭X
# p= re.compile('python$',re.MULTILINE)
# python으로 끝나는 문자열이나 각 라인의 끝을 문자열끝으로 인식하므로 10line의 python이 매칭O
p= re.compile('\w+ python$',re.MULTILINE)
# 각라인의 끝이 python인 경우 그라인의 앞 문자+숫자 와 공백인경우 까지 매칭하고 싶은 경우

data = '''python one python debug
life is too short
python two
you nees python
python three'''

print(p.findall(data))
