def handle_add_new_plant(controller):
    def callback(x):
        controller.add_plant_in_table()
    return callback

def hadle_cancel_add_new_plant(controller):
    def callback(x):
        controller.close_add_window()
    return callback

def close_general_info(controller):
    def callback(x):
        controller.close_ganeral_data()
    return callback

def hadle_cancel_action_window(controller):
    def callback(x):
        controller.close_action_window()
    return callback

def handle_action_window(controller):
    def callback(x):
        controller.action_window()
    return callback