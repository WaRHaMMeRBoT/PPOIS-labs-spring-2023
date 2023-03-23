import PySimpleGUI as sg

import functions as func
import players


def window_find():
    input_find = sg.Input('Name or Club or Team', enable_events=True, key='-INPUT-', expand_x=True,
                          justification='left')
    additional_input = sg.Input('Year or Town or Position', enable_events=True, key='-ADDIT-', expand_x=True,
                                justification='left')
    button_find = sg.Button(button_text="Find", key='-Find-')
    layout = [[input_find], [additional_input], [button_find]]
    window = sg.Window("Find", layout, size=(550, 90), resizable=True)

    while True:
        event, values = window.read()
        if event == '-Find-':
            first_val = values['-INPUT-']
            second_val = values['-ADDIT-']
            print(second_val)
            func.find(first_val, second_val)

        if event == sg.WIN_CLOSED:
            return False


def delete_player():
    input_find = sg.Input('Name or Club or Team', enable_events=True, key='-INPUT-', expand_x=True,
                          justification='left')
    additional_input = sg.Input('Year or Town or Position', enable_events=True, key='-ADDIT-', expand_x=True,
                                justification='left')
    button_find = sg.Button(button_text="Delete", key='-Del-')
    layout = [[input_find], [additional_input], [button_find]]
    window = sg.Window("Delete", layout, size=(550, 90), resizable=True)

    while True:
        event, values = window.read()
        if event == '-Del-':
            first_val = values['-INPUT-']
            second_val = values['-ADDIT-']
            print(second_val)
            func.delete(first_val, second_val)

        if event == sg.WIN_CLOSED:
            break


def add_player():
    name = sg.Input('name', enable_events=True, key='-name-', expand_x=True)
    year = sg.Input('year', enable_events=True, key='-year-', expand_x=True)
    club = sg.Input('club', enable_events=True, key='-club-', expand_x=True)
    town = sg.Input('town', enable_events=True, key='-town-', expand_x=True)
    team = sg.Input('team', enable_events=True, key='-team-', expand_x=True)
    position = sg.Input('position', enable_events=True, key='-position-', expand_x=True)

    layout = [[name], [year], [club], [town], [team], [position], [sg.Button(button_text="Add", key='-Add-')]]

    window = sg.Window("Add", layout, size=(500, 210), resizable=True)

    while True:
        event, values = window.read()

        if event == '-Add-':
            new_player = dict(name=values['-name-'],
                              year=values['-year-'],
                              club=values['-club-'],
                              town=values['-town-'],
                              team=values['-team-'],
                              position=values['-position-'])
            data_model = players.DataPlayers()
            data = data_model.get_data()

            data['players'].append(new_player)
            print(data)
            data_model.refresh_data(data)
            data_model.push_data()

        if event == sg.WIN_CLOSED:
            break


def update_layout(table):
    layout = [[table],
              [sg.Button(key='Bback', image_filename="arrows/doubleL.png"),
               sg.Button(key='back', image_filename="arrows/left.png"),
               sg.Button(key='next', image_filename="arrows/right.png"),
               sg.Button(key='Nnext', image_filename="arrows/doubleR.png")],
              [sg.Button(button_text="Find", key='-Find-'),
               sg.Button(button_text="Delete", key='-Del-')],
              [sg.Button(button_text="Add player", key='ADD')]]

    return layout
