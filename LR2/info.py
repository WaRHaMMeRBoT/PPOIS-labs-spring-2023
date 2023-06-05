import xml.etree.ElementTree as ET

file = 'info.xml'

def search(file_xml, key, value):
    tree = ET.parse(file_xml)
    root = tree.getroot()
    found = []
    for tournament in root:
        field = tournament.find(key)
        info_value = field.text
        if info_value == value:
            element = []
            for el in tournament:
                element.append(el.text)
            element.append(str(round(float(element[-1])*0.6)))
            found.append(element)
    return found

def range_search(file_xml, key, min, max):
    if min < 0: min = 0
    if max < 0: max = 999999999
    tree = ET.parse(file_xml)
    root = tree.getroot()
    found = []
    for tournament in root:
        field = tournament.find(key)
        info_value = float(field.text)
        if info_value >= min and info_value <= max:
            element = []
            for el in tournament:
                element.append(el.text)
            element.append(str(round(float(element[-1])*0.6)))
            found.append(element)
    return found

def add(file_xml, dict):
    tree = ET.parse(file_xml)
    root = tree.getroot()
    new_item = ET.SubElement(root, 'tournament')
    for key, el in dict.items():
        sub_item = ET.SubElement(new_item, key)
        sub_item.text = el
    tree.write(file)

def delete(file_xml, key, value):
    tree = ET.parse(file_xml)
    root = tree.getroot()
    deleted = []
    for tournament in root:
        field = tournament.find(key)
        info_value = field.text
        if info_value == value:
            element = []
            for el in tournament:
                element.append(el.text)
            element.append(str(round(float(element[-1]))*0.6))
            deleted.append(element)
            root.remove(tournament)
            tree.write(file)
    return deleted

def range_delete(file_xml, key, min, max):
    if min < 0: min = 0
    if max < 0: max = 999999999
    tree = ET.parse(file_xml)
    root = tree.getroot()
    found = []
    for tournament in root:
        field = tournament.find(key)
        info_value = float(field.text)
        if info_value >= min and info_value <= max:
            element = []
            for el in tournament:
                element.append(el.text)
            element.append(str(round(float(element[-1])*0.6)))
            found.append(element)
            root.remove(tournament)
            tree.write(file)
    return found