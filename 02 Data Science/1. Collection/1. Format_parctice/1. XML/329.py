from xml.etree.ElementTree import Element,dump,SubElement

note = Element('note')

to = Element('to')
to.text = "Tove"
note.append(to)

SubElement(note,"from").text = 'Jani'
dump(note)

dummy = Element('dummy')
note.insert(1,dummy) # 1번째 이므로 to 다음에 insert 하는 것
dummy.text = 'dummy' # 값을 추가하지 않으면 </dummy>로 만 저장된다
dump(note)
note.remove(dummy) # 해당 Element명을 이용하여 삭제가능하며, 부모Element를 기준으로 remove 해야한다
dump(note)



