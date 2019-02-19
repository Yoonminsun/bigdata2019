import re
def hexrep1(match):
    value = int(match.group())
    return hex(value)

# p = re.compile(r'\d+')
p = re.compile('\d+') # '\d' 자체가 정규식에서의 escape 문자 이므로 raw string 옵션 없이도 사용 가능하다
print(p.sub(hexrep1,'Call 65490 for printing, 4915 for  user code.'))
# 매칭된 숫자로만 이루어진 문자열을 hexrep1 함수를 통해 16진수로 바뀐 값을 리턴받아 sub함수를 실행하는것

