import xml.etree.ElementTree as ElemTree

file:str = "inform.xml"

def read_xml(file_xml):
    tree = ElemTree.parse(file_xml)
    root = tree. getroot()
    for children in root:
        print(children.tag, children.attrib)
        for child in children:
            print("\t",child.tag, child.attrib)
     
def find(file_xml, value:str, key:str):
    answer:list=[]
    tree = ElemTree.parse(file_xml)
    root = tree.getroot()
    for person in root:
        field = person.find(key)
        data_value = field.text
        if value == data_value:
            element:list=[]
            for elem in person:
                element.append(elem.text)
            answer.append(element)
    return answer

def add(file_xml, person:str, dict:dict):
    tree = ElemTree.parse(file_xml)
    root = tree.getroot()
    new_person = ElemTree.SubElement(root, person)
    for key,elem in dict.items():
        sub_person = ElemTree.SubElement(new_person, key)
        sub_person.text = elem
    tree.write(file)

def delete(file_xml, value:str, key:str):
    answer:list=[]
    tree = ElemTree.parse(file_xml)
    root = tree. getroot()
    for person in root:
        field = person.find(key)
        data_value = field.text
        if value == data_value:
            element:list=[]
            for elem in person:
                element.append(elem.text)
            answer.append(element)
            root.remove(person)
            tree.write(file)
    return answer

def count_for_delete(file_xml):
    count=0
    tree = ElemTree.parse(file_xml)
    root = tree.getroot()
    for person in root:
        count+=1
    return count