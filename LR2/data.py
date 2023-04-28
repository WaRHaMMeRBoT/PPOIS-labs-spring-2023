import xml.etree.ElementTree as ET

file:str = "d.xml"

def read_xml(file_xml):
    tree = ET.parse(file_xml)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)
        for child_b in child:
            print("\t",child_b.tag, child_b.attrib)
     
def find(file_xml, value:str, key:str):
    answer:list=[]
    tree = ET.parse(file_xml)
    root = tree.getroot()
    for item in root:
        field = item.find(key)
        data_value = field.text
        if value == data_value:
            element:list=[]
            for el in item:
                element.append(el.text)
            answer.append(element)
    return answer

def add(file_xml, item:str, dict:dict):
    tree = ET.parse(file_xml)
    root = tree.getroot()
    new_item = ET.SubElement(root, item)
    for key,el in dict.items():
        sub_item = ET.SubElement(new_item, key)
        sub_item.text = el
    tree.write(file)

def delete(file_xml, value:str, key:str):
    answer:list=[]
    tree = ET.parse(file_xml)
    root = tree.getroot()
    for item in root:
        field = item.find(key)
        data_value = field.text
        if value == data_value:
            element:list=[]
            for el in item:
                element.append(el.text)
            answer.append(element)
            root.remove(item)
            tree.write(file)
    return answer

