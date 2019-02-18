import re
original_text = 'life is too short'
p = re.compile('[a-z]+')

m=p.search(original_text) # search는 전체를 검색하여 1개만 match 객체로 리턴
print(m)

m=p.findall(original_text) # findall은 매칭된 것(문자열 타입)들을 리스트로 저장하여 리턴
print(m)
