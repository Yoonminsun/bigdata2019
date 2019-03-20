from xml.etree.ElementTree import parse,Element,SubElement,dump,ElementTree

note = Element('note')
to3 = SubElement(note,'to')
dump(note)
to3.attrib['value']='a'
tosub = SubElement(to3,'tosub')
tosub.attrib['name']='name'
dump(note)