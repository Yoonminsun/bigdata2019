from xml.etree.ElementTree import parse

tree = parse('note.xml')
note = tree.getroot() # 가장 상위 Element 가져옴

# print(note.get("date"))
# print(note.get("foo"))
# print(note.get("foo","default")) # 키 중에 foo 가 없으면 default를 가져옴
# print(note.keys()) # key 값들을 리스트로 리턴
# print(note.items()) # key,value 쌍을 튜플로 만들고 그 튜플들을 리스트로 리턴

# 상위태그.함수('하위태그명')
# from_tag = note.find('from') # note태그 하위에 from과 일치하는 첫 번째 태그 리턴,없으면 None
# print(from_tag.text)
# from_tags = note.findall('from') # note태그 하위에 from과 일치하는 모든 태그를 리스트로 리턴
# for i in from_tags:
#     print(i.text)
# from_text= note.findtext('from') # note 태그 하위에 from과 일치하는 첫 번째 태그의 텍스트값 리턴
# print(from_text)

child = note.getiterator()
print(list(child))

