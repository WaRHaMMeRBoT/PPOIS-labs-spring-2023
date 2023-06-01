import PySimpleGUI as sg


def get_money_window():
    money = sg.Input('money', enable_events=True, key='-money-', expand_x=True)
    button = sg.Button(button_text="Enter", key="-enter-")

    layout = [[money], [button]]

    window = sg.Window("Get money", layout, size=(500, 210), resizable=True)

    while True:
        event, values = window.read()

        if event == '-enter-':
            window.close()
            return values['-money-']

        if event == sg.WIN_CLOSED:
            break


def verify():
    card = sg.Input('card', enable_events=True, key='-card-', expand_x=True)
    pin = sg.Input('pin', enable_events=True, key='-pin-', expand_x=True)
    button = sg.Button(button_text="Enter", key="-enter-")

    layout = [[card], [pin], [button]]

    window = sg.Window("Card_number", layout, size=(500, 210), resizable=True)

    while True:
        event, values = window.read()

        if event == '-enter-':
            window.close()
            return values['-card-'], values['-pin-']

        if event == sg.WIN_CLOSED:
            break
