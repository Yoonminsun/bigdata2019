import re

data = 'The quick brown fox jumps over the lazy dog.'
# 1~ 주어진 숫자 사이의 길이를 가진 문자열 삭제하기
# 주어진 숫자는 3으로 줌
p = re.compile(r'\b\w{1,3}\b') # '\b'를 단어의 경계를 의미하는 escape로 쓰기위해 raw string 옵션을 붙여줌
m = p.sub('',data)
print(m)
