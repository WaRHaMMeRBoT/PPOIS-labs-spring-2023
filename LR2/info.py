import xml.etree.ElementTree as ET
import time_1 as time

file = 'info.xml'

def search(file_xml, key, value):
    tree = ET.parse(file_xml)
    root = tree.getroot()
    found = []
    for train in root:
        field = train.find(key)
        info_value = field.text
        if info_value == value:
            element = []
            for i in range(5):
                element.append(train[i].text)
            travel_time = time.time_of_travel(time.to_date(element[3]), time.to_date(element[4]))
            element.append(time.from_time_to_string(travel_time))
            found.append(element)
    return found

def search_time(file_xml, value):
    tree = ET.parse(file_xml)
    root = tree.getroot()
    found = []
    for train in root:
        departure = time.to_date(train.find('departure_data_time').text)
        arrival = time.to_date(train.find('arrival_data_time').text)
        info_time = time.time_of_travel(departure, arrival)
        if info_time == value:
            element = []
            for i in range(5):
                element.append(train[i].text)
            travel_time = time.time_of_travel(time.to_date(element[3]), time.to_date(element[4]))
            element.append(time.from_time_to_string(travel_time))
            found.append(element)
    return found

def range_search(file_xml, key, min, max):
    if min == -1: min = '00.00 00:00'
    if max == -1: max = '31.12 23:59'
    min = time.to_date(min)
    max = time.to_date(max)
    tree = ET.parse(file_xml)
    root = tree.getroot()
    found = []
    for train in root:
        field = train.find(key)
        info_value = time.to_date(field.text)
        if time.compare(info_value, min) != 'earlier' and time.compare(info_value, max) != 'later':
            element = []
            for el in train:
                element.append(el.text)
            travel_time = time.time_of_travel(time.to_date(element[3]), time.to_date(element[4]))
            element.append(time.from_time_to_string(travel_time))
            found.append(element)
    return found

def add(file_xml, dict):
    tree = ET.parse(file_xml)
    root = tree.getroot()
    new_item = ET.SubElement(root, 'train')
    for key, el in dict.items():
        sub_item = ET.SubElement(new_item, key)
        sub_item.text = el
    tree.write(file)

def delete(file_xml, key, value):
    tree = ET.parse(file_xml)
    root = tree.getroot()
    deleted = []
    for train in root:
        field = train.find(key)
        info_value = field.text
        if info_value == value:
            element = []
            for el in train:
                element.append(el.text)
            travel_time = time.time_of_travel(time.to_date(element[3]), time.to_date(element[4]))
            element.append(time.from_time_to_string(travel_time))
            deleted.append(element)
            root.remove(train)
            tree.write(file)
    return deleted

def range_delete(file_xml, key, min, max):
    if min == -1: min = '00.00 00:00'
    if max == -1: max = '31.12 23:59'
    min = time.to_date(min)
    max = time.to_date(max)
    tree = ET.parse(file_xml)
    root = tree.getroot()
    found = []
    for train in root:
        field = train.find(key)
        info_value = time.to_date(field.text)
        if time.compare(info_value, min) == 'later' and time.compare(info_value, max) == 'earlier':
            element = []
            for el in train:
                element.append(el.text)
            travel_time = time.time_of_travel(time.to_date(element[3]), time.to_date(element[4]))
            element.append(time.from_time_to_string(travel_time))
            found.append(element)
            root.remove(train)
            tree.write(file)
    return found

def delete_time(file_xml, value):
    tree = ET.parse(file_xml)
    root = tree.getroot()
    found = []
    for train in root:
        departure = time.to_date(train.find('departure_data_time').text)
        arrival = time.to_date(train.find('arrival_data_time').text)
        info_time = time.time_of_travel(departure, arrival)
        if info_time == value:
            element = []
            for i in range(5):
                element.append(train[i].text)
            travel_time = time.time_of_travel(time.to_date(element[3]), time.to_date(element[4]))
            element.append(time.from_time_to_string(travel_time))
            found.append(element)
            root.remove(train)
            tree.write(file)
    return found