from xml.etree.ElementTree import parse

menu=0
tree = parse('students_info.xml')
note = tree.getroot()

# child = note.getiterator()
# print(list(child))
# child2 = child.getiterator()
tag = note.findall("student")
print(tag)
if tag[0].text:
    print('true')
else:
    print('false')
