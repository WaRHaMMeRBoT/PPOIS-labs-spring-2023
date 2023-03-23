import PySimpleGUI as sg

import players


def curr_player_data(data):
    player = [data['name'], data['year'], data['club'], data['town'],
              data['team'], data['position']]
    print(player)
    return player


def next_page(curr_player):
    data_model = players.DataPlayers()
    data = data_model.get_data()
    j = 0
    rows = []

    for i in data['players']:
        if curr_player <= j < curr_player + 5 and j < len(data['players']):
            rows.append(curr_player_data(i))
        j += 1
    print(rows)
    toprow = ['Name', 'Year of birth', 'Football club', 'Hometown', 'Team', 'Position']
    table = sg.Table(values=rows, headings=toprow, auto_size_columns=True,
                     display_row_numbers=False,
                     justification='center', key='-TABLE-', )
    return table


def prev_page(curr_player):
    data_model = players.DataPlayers()
    data = data_model.get_data()
    j = 0
    rows = []

    for i in data['players']:
        if curr_player - 1 < j < curr_player + 5 and j >= 0:
            rows.append(curr_player_data(i))
        j += 1
    print(rows)
    toprow = ['Name', 'Year of birth', 'Football club', 'Hometown', 'Team', 'Position']
    table = sg.Table(values=rows, headings=toprow, auto_size_columns=True,
                     display_row_numbers=False,
                     justification='center', key='-TABLE-', )
    return table


def find(first_val, second_val):
    player_data = ""
    check = 0
    data_model = players.DataPlayers()
    data = data_model.get_data()
    for i in data['players']:
        if i['name'].find(first_val) != -1 and i['year'] == second_val:
            player_data += i['name'] + " " + i['year'] + " " + i['club'] + " " + i['town'] + " " + \
                           i['team'] + " " + i['position'] + "\n"
            check = 1
            #break
        if i['club'] == first_val and i['town'] == second_val:
            player_data += i['name'] + " " + i['year'] + " " + i['club'] + " " + i['town'] + " " + \
                           i['team'] + " " + i['position'] + "\n"
            check = 1
            #break
        if i['team'] == first_val and i['position'] == second_val:
            player_data += i['name'] + " " + i['year'] + " " + i['club'] + " " + i['town'] + " " + \
                           i['team'] + " " + i['position'] + "\n"
            check = 1
            #break
    if check == 0:
        sg.popup('No Data')
    else:
        sg.popup(player_data)


def delete(first_val, second_val):
    check = 0
    data_model = players.DataPlayers()
    data = data_model.get_data()
    for i in data['players']:
        if i['name'].find(first_val) != -1 and i['year'] == second_val:
            data['players'].remove(i)
            sg.popup('Deleted')
            check = 1
            break
        if i['club'] == first_val and i['town'] == second_val:
            data['players'].remove(i)
            sg.popup('Deleted')
            check = 1
            break
        if i['team'] == first_val and i['position'] == second_val:
            data['players'].remove(i)
            sg.popup('Deleted')
            check = 1
            break
    if check == 0:
        sg.popup('No Data')

    data_model.refresh_data(data)
    data_model.push_data()


def refresh_data():
    data_model = players.DataPlayers()
    data = data_model.get_data()
    j = 0
    rows = []
    for i in data['players']:
        if j < 5:
            rows.append(curr_player_data(i))
        j += 1
    toprow = ['Name', 'Year of birth', 'Football club', 'Hometown', 'Team', 'Position']

    table = sg.Table(values=rows, headings=toprow, auto_size_columns=True,
                     display_row_numbers=False,
                     justification='center', key='-TABLE-', )

    return table
