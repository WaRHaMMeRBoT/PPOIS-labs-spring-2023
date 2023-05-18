import Classes
from prettytable import PrettyTable


def visualizer(field: Classes.Field):
    full_table = []
    counter = 0
    for rows in field.get_matrix():
        temp_table = []
        for cells in rows:
            temp_info = []
            cells: Classes.Cell
            for obj in cells.get_content():
                if type(obj) == Classes.Tree:
                    temp_info.append(obj.get_name() + ":Tree")
                elif type(obj) == Classes.Grass:
                    temp_info.append(obj.get_name() + ":Grass")
                else:
                    if type(obj) == Classes.Wolf:
                        temp_info.append(obj.get_name() + ":Wolf")
                    elif type(obj) == Classes.Owl:
                        temp_info.append(obj.get_name() + ":Owl")
                    elif type(obj) == Classes.Deer:
                        temp_info.append(obj.get_name() + ":Deer")
                    elif type(obj) == Classes.Mouse:
                        temp_info.append(obj.get_name() + ":Mouse")
                    elif type(obj) == Classes.Bison:
                        temp_info.append(obj.get_name() + ":Bison")
            temp_table.append(temp_info)
            counter+=1
        full_table.append(temp_table)
    output = PrettyTable()
    output.add_rows(full_table)
    print(output)
    return full_table
