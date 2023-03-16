import xml.dom.minidom
import Controller


def __save_data(xml_save) -> None:
    file = open('save.xml', 'w')
    file.write(xml_save)
    file.close()


def __row_info_write(obj: list, save_file: xml.dom.minidom.Document, counter: int):
    athlete_number = save_file.createElement("Sportsman")
    athlete_number.setAttribute("number", str(counter))
    name_of_sportsman = save_file.createElement("name")
    name_of_sportsman.appendChild(save_file.createTextNode(obj[0]))
    line_up = save_file.createElement("line_up")
    line_up.appendChild(save_file.createTextNode(obj[1]))
    position = save_file.createElement("position")
    position.appendChild(save_file.createTextNode(obj[2]))
    achievements = save_file.createElement("achievements")
    achievements.appendChild(save_file.createTextNode(obj[3]))
    sports_discipline = save_file.createElement("sports_discipline")
    sports_discipline.appendChild(save_file.createTextNode(obj[4]))
    rank = save_file.createElement("rank")
    rank.appendChild(save_file.createTextNode(obj[5]))
    return athlete_number, name_of_sportsman, line_up, position, achievements, sports_discipline, rank


def __insert_attributes(athlete_number, name_of_sportsman, line_up, position, achievements, sports_discipline, rank):
    athlete_number.appendChild(name_of_sportsman)
    athlete_number.appendChild(line_up)
    athlete_number.appendChild(position)
    athlete_number.appendChild(achievements)
    athlete_number.appendChild(sports_discipline)
    athlete_number.appendChild(rank)
    return athlete_number


def save_button(data_to_save: list):
    save_file = xml.dom.minidom.Document()
    table = save_file.createElement("Sportsmen")
    save_file.appendChild(table)
    counter = 0
    for obj in data_to_save:
        athlete_number, name_of_sportsman, line_up, position, achievements, sports_discipline, \
         rank = __row_info_write(obj, save_file, counter)
        table.appendChild(athlete_number)
        athlete_number = __insert_attributes(athlete_number, name_of_sportsman, line_up,
                                           position, achievements, sports_discipline, rank)
        counter += 1
    xml_str = save_file.toprettyxml(indent='\t')
    __save_data(xml_str)



