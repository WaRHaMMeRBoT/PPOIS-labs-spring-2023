#!/usr/bin/python
# -*- coding: utf8 -*-
import copy

import Classes
import TurnLogic
import Visualizer
import math


def load_save(path: str) -> tuple:
    save_file = open(path, "r")
    save_container = []
    for line in save_file:
        save_container.append(line)
    cells_num = save_container[0]
    turn = save_container[1]
    save_container.remove(turn)
    save_container.remove(cells_num)
    field_info = []
    for line in save_container:
        list_of_objects = line.split(";")
        temp_cell_info = []
        for obj in list_of_objects:
            temp_cell_info.append(obj.split(","))
        field_info.append([temp_cell_info])
    inp = (cells_num, turn, field_info)
    save_file.close()
    return inp


def field_constructor(cells_in_row: int) -> Classes.Field:
    cells_in_row = int(math.sqrt(cells_in_row))
    matrix = []
    for iterator in range(0, cells_in_row):
        matrix.append([])
    for first_iter in matrix:
        for second_iter in range(0, cells_in_row):
            temp_cell = Classes.Cell()
            first_iter.append(temp_cell)
    out_field = Classes.Field(matrix)
    return out_field


def animal_reconstructor(info: list):
    if info[0] != "Tree" and info[0] != "Grass":
        coordinates = (info[5].split("|"))
        coordinates[0] = int(coordinates[0])
        coordinates[1] = int(coordinates[1])
    else:
        coordinates = (info[4].split("|"))
        coordinates[0] = int(coordinates[0])
        coordinates[1] = int(coordinates[1])
    if info[0] == "Owl":
        output = Classes.Owl(int(info[2]), int(info[3]), coordinates, info[6], float(info[4]), "Owl", info[1])
    elif info[0] == "Wolf":
        output = Classes.Wolf(int(info[2]), int(info[3]), coordinates, info[6], float(info[4]), "Wolf", info[1])
    elif info[0] == "Bison":
        output = Classes.Bison(int(info[2]), int(info[3]), coordinates, info[6], float(info[4]), "Bison", info[1])
    elif info[0] == "Mouse":
        output = Classes.Mouse(int(info[2]), int(info[3]), coordinates, info[6], float(info[4]), "Mouse", info[1])
    elif info[0] == "Deer":
        output = Classes.Deer(int(info[2]), int(info[3]), coordinates, info[6], float(info[4]), "Deer", info[1])
    else:
        if info[0] == "Tree":
            output = Classes.Tree(int(info[3]), float(info[2]), info[1],  coordinates)
        else:
            output = Classes.Grass(int(info[3]), float(info[2]), info[1],  coordinates)
    return output


def filler(save_info: list, field: Classes.Field):
    filled_field = field.get_matrix()
    first_iterator = 0
    second_iterator = 0
    for rows in save_info:
        for cells in rows:
            for obj in cells:
                temp_obj = animal_reconstructor(obj)
                filled_field[first_iterator][second_iterator].add(temp_obj)
            second_iterator += 1
            if second_iterator == 3:
                first_iterator += 1
                second_iterator = 0
    field.set_matrix(filled_field)
    return field


def encoder(turn: int, field: Classes.Field, path: str):
    num_of_cells = len(field.get_matrix()) ** 2
    save = [num_of_cells, turn]
    for row in field.get_matrix():
        for cell in row:
            temp_row = ""
            for obj in cell.get_content():
                if type(obj) != Classes.Grass and type(obj) != Classes.Tree:
                    if type(obj) == Classes.Wolf:
                        obj: Classes.Wolf
                        temp_row += "Wolf,"
                    elif type(obj) == Classes.Owl:
                        obj: Classes.Owl
                        temp_row += "Owl,"
                    elif type(obj) == Classes.Mouse:
                        obj: Classes.Mouse
                        temp_row += "Mouse,"
                    elif type(obj) == Classes.Deer:
                        obj: Classes.Deer
                        temp_row += "Deer,"
                    elif type(obj) == Classes.Bison:
                        obj: Classes.Bison
                        temp_row += "Bison,"
                    temp_row += (obj.get_name() + "," + str(obj.get_satiety()) + "," + str(
                        obj.get_age()) + "," +
                                 str(obj.get_body_size()) + "," + str(obj.get_coordinates()[0]) + "|" + str(
                                obj.get_coordinates()[1])
                                 + "," + obj.get_gender() + ";")
                else:
                    if type(obj) == Classes.Tree:
                        obj: Classes.Tree
                        temp_row += "Tree,"
                    elif type(obj) == Classes.Grass:
                        obj: Classes.Grass
                        temp_row += "Grass,"
                    temp_row += (obj.get_name() + "," + str(obj.get_size()) + "," + str(obj.get_age()) + "," +
                                 str(obj.get_coordinates()[0]) + "|" + str(obj.get_coordinates()[1]) + ";")
            save.append(temp_row)
    save_file = open(path, "w")
    counter = 0
    for line in save:
        if counter > 1:
            line = line.removesuffix(';')
        if counter < 1:
            save_file.write(str(line)+"\n")
        elif counter > 1 and "\n" in line:
            save_file.write(str(line))
        else:
            if counter == 2+save[0]:
                save_file.write(str(line))
            else:
                save_file.write(str(line)+"\n")
        counter += 1
    save_file.close()


class Engine:
    def __init__(self):
        self.path = 'Test_save.txt'
        field_info = load_save(self.path)
        self.current_field = field_constructor(int(field_info[0]))
        self.current_field = filler(field_info[2], self.current_field)
        self.turn_counter = int(field_info[1])

    def next_turn(self):
        try:
            self.turn_counter += 1
            TurnLogic.turn_processor(self.current_field)
        except ImportError as ie:
            print(ie)
            exit()

    def save(self, new_path=None):
        try:
            if not new_path:
                print("Input save file name")
                path = input()
            else:
                path = copy.deepcopy(new_path)
            encoder(int(self.turn_counter), self.current_field, path)
        except SyntaxError as se:
            print(se)
            exit()

    def load(self, new_path=None):
        try:
            if not new_path:
                print("Input save file path")
                self.path = input()
            else:
                self.path = new_path
            field_info = load_save(self.path)
            self.current_field = field_constructor(int(field_info[0]))
            self.current_field: Classes.Field
            self.current_field = filler(field_info[2], self.current_field)
            self.turn_counter = int(field_info[1])
        except ImportError:
            print(ImportError)
            exit()

    def add_creature(self, new_specie=None, creature_stats_animal=None, creature_stats_plant=None):
        try:
            if not new_specie:
                print("Input creature specie")
                specie = input()
            else:
                specie = copy.deepcopy(new_specie)
            if specie != "Tree" and specie != "Grass":
                if not creature_stats_animal:
                    print("Input:name, satiety, age, body size, coordinates, gender")
                    coordinates: list
                    creature_stats_row: str
                    creature_stats_row = input()
                else:
                    creature_stats_row = creature_stats_animal
                print(creature_stats_row)
                list_of_stats = creature_stats_row.split(" ")
                coordinates = [int(list_of_stats[4]), int(list_of_stats[5])]
                if specie == "Wolf":
                    temp_creature = Classes.Wolf(int(list_of_stats[1]), int(list_of_stats[2]), coordinates,
                                                 list_of_stats[6], float(list_of_stats[3]), "Wolf", list_of_stats[0]
                                                 )
                elif specie == "Owl":
                    temp_creature = Classes.Owl(int(list_of_stats[1]), int(list_of_stats[2]), coordinates,
                                                list_of_stats[6], float(list_of_stats[3]), "Owl", list_of_stats[0])
                elif specie == "Mouse":
                    temp_creature = Classes.Mouse(int(list_of_stats[1]), int(list_of_stats[2]), coordinates,
                                                  list_of_stats[6], float(list_of_stats[3]), "Mouse",
                                                  list_of_stats[0])
                elif specie == "Deer":
                    temp_creature = Classes.Deer(int(list_of_stats[1]), int(list_of_stats[2]), coordinates,
                                                 list_of_stats[6], float(list_of_stats[3]), "Deer", list_of_stats[0]
                                                 )
                else:
                    temp_creature = Classes.Bison(int(list_of_stats[1]), int(list_of_stats[2]), coordinates,
                                                  list_of_stats[6], float(list_of_stats[3]), "Bison",
                                                  list_of_stats[0])
                self.current_field.create_animal(temp_creature, coordinates)
            else:
                if not creature_stats_plant:
                    print("Input:name, age, size, coordinates")
                    coordinates: list
                    creature_stats_row: str
                    creature_stats_row = input()
                else:
                    creature_stats_row = creature_stats_plant
                list_of_stats = creature_stats_row.split(" ")
                coordinates = [int(list_of_stats[3]), int(list_of_stats[4])]
                if specie == "Tree":
                    temp_plant = Classes.Tree(age=int(list_of_stats[1]), size=float(list_of_stats[2]),
                                              coordinates=coordinates,
                                              name=list_of_stats[0])
                else:
                    temp_plant = Classes.Grass(int(list_of_stats[1]), float(list_of_stats[2]), coordinates,
                                               list_of_stats[0])
                self.current_field.create_animal(temp_plant, coordinates)
        except ValueError:
            print(ValueError)
            exit()

    def show(self):
        Visualizer.visualizer(self.current_field)


def old_main():
    path = 'Test_save.txt'
    field_info = load_save(path)
    current_field = field_constructor(int(field_info[0]))
    current_field: Classes.Field
    current_field = filler(field_info[2], current_field)
    turn_counter = int(field_info[1])
    while True:
        command = input()
        if command == "next_turn":
            try:
                turn_counter+=1
                TurnLogic.turn_processor(current_field)
            except ImportError as ie:
                print(ie)
                exit()
        elif command == "save":
            try:
                print("Input save file name")
                path = input()
                encoder(int(turn_counter), current_field, path)
            except SyntaxError as se:
                print(se)
                exit()
        elif command == "load":
            try:
                print("Input save file path")
                path = input()
                field_info = load_save(path)
                current_field = field_constructor(int(field_info[0]))
                current_field: Classes.Field
                current_field = filler(field_info[2], current_field)
                turn_counter = int(field_info[1])
            except ImportError:
                print(ImportError)
                exit()
        elif command == "add_creature":
            try:
                print("Input creature specie")
                specie = input()
                if specie != "Tree" and specie != "Grass":
                    print("Input:name, satiety, age, body size, coordinates, gender")
                    coordinates: list
                    creature_stats_row: str
                    creature_stats_row = input()
                    print(creature_stats_row)
                    list_of_stats = creature_stats_row.split(" ")
                    coordinates = [int(list_of_stats[4]), int(list_of_stats[5])]
                    if specie == "Wolf":
                        temp_creature = Classes.Wolf(int(list_of_stats[1]), int(list_of_stats[2]), coordinates,
                                                     list_of_stats[6], float(list_of_stats[3]), "Wolf", list_of_stats[0]
                                                     )
                    elif specie == "Owl":
                        temp_creature = Classes.Owl(int(list_of_stats[1]), int(list_of_stats[2]), coordinates,
                                                    list_of_stats[6], float(list_of_stats[3]), "Owl", list_of_stats[0])
                    elif specie == "Mouse":
                        temp_creature = Classes.Mouse(int(list_of_stats[1]), int(list_of_stats[2]), coordinates,
                                                      list_of_stats[6], float(list_of_stats[3]), "Mouse",
                                                      list_of_stats[0])
                    elif specie == "Deer":
                        temp_creature = Classes.Deer(int(list_of_stats[1]), int(list_of_stats[2]), coordinates,
                                                     list_of_stats[6], float(list_of_stats[3]), "Deer", list_of_stats[0]
                                                     )
                    else:
                        temp_creature = Classes.Bison(int(list_of_stats[1]), int(list_of_stats[2]), coordinates,
                                                      list_of_stats[6], float(list_of_stats[3]), "Bison",
                                                      list_of_stats[0])
                    current_field.create_animal(temp_creature, coordinates)
                else:
                    print("Input:name, age, size, coordinates")
                    coordinates: list
                    creature_stats_row: str
                    creature_stats_row = input()
                    list_of_stats = creature_stats_row.split(" ")
                    coordinates = [int(list_of_stats[3]), int(list_of_stats[4])]
                    if specie == "Tree":
                        temp_plant = Classes.Tree(int(list_of_stats[1]), float(list_of_stats[2]), coordinates,
                                                  list_of_stats[0])
                    else:
                        temp_plant = Classes.Grass(int(list_of_stats[1]), float(list_of_stats[2]), coordinates,
                                                   list_of_stats[0])
                    current_field.create_animal(temp_plant, coordinates)
            except ValueError:
                print(ValueError)
                exit()
        elif command == "show":
            Visualizer.visualizer(current_field)
        elif command == "exit":
            break
        else:
            print("Command not found try again\n")

