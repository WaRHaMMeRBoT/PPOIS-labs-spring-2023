import xml.etree.ElementTree as ET

def write(lst: list, path):
    data = ET.Element('data')
    for elem in lst:
        player = ET.SubElement(data, 'player')
        name = ET.SubElement(player, 'name')
        name.text = elem[0]
        date = ET.SubElement(player, 'date')
        date.text = str(elem[1])
        team = ET.SubElement(player, 'team')
        team.text = str(elem[2])
        town = ET.SubElement(player, 'town')
        town.text = str(elem[3])
        line_up = ET.SubElement(player, 'line_up')
        line_up.text = str(elem[4])
        position = ET.SubElement(player, 'position')
        position.text = elem[5]
    ET.ElementTree(data).write(path)




