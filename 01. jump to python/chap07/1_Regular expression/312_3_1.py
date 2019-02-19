import re

# str='\' # '\' 다음에 escape 코드가 와야 하지만 없으므로 문법적으로 오류를 발생시킨다
str = '\\' # str은 내부적으로 '\\' 저장이 된다. 하지만 문자로써는 '\'의 의미이다
print('str=',str) # str의 출력 결과는 '\'
str = '\\\\' # str은 내부적으로 '\\\\' 저장이 된다. 하지만 문자로써는 '\\'의 의미이다
print('str=',str) # str의 출력 결과는 '\\'
str = r"\\" # raw string을 사용했으므로 str은 내부적으로 '\\' 저장이 되며 문자로도 '\\'의 의미이다
print('str=',str) # str의 출력 결과는 '\\'
# str = r"\" # 현재 버전에서는 'r',raw string 사용해도 '\'의 한개 사용은 허용되지 않는다
str = '\\nection'
print(str)
