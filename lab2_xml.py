import xml.dom.minidom as minidom

xmlfile = open('currency.xml')
xmldata = xmlfile.read()
dom = minidom.parseString(xmldata)
dom.normalize()

list_CharCode = []
elements = dom.getElementsByTagName('Valute') #все элементы Valute

for node in elements:
    for child in node.childNodes: #все дочерние узлы Valute
        if child.nodeType == 1: #проверяет что это тег
            if child.tagName == 'Nominal':
                if child.firstChild.nodeType == 3: #ghjdthztn что это текст
                    nominal = int(child.firstChild.data) #извлекает строковое значение
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    CharCode = child.firstChild.data
    if nominal == 10 or nominal == 100:
        list_CharCode.append(CharCode)
print(list_CharCode)

