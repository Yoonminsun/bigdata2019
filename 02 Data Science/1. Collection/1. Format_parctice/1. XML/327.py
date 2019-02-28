from xml.etree.ElementTree import Element,dump

note = Element('note')
to = Element('to')
to.text = "Tove"

note.append(to)
dump(note) # note를 기준으로 하위를 보여줌
dump(to)