def handle_add_new_student(controller):
    def callback(x):
        controller.add_student_in_table()
    return callback

def hadle_cancel_add_new_student(controller):
    def callback(x):
        controller.close_add_window()
    return callback

def handle_filter_student(controller):
    def callback(x):
        controller.filter()
    return callback

def handle_confirm_delete(controller):
    def callback(x):
        controller.delete_rows()
    return callback

def handle_cancel_filter_student(controller):
    def callback(x):
        controller.close_filter_window()
    return callback

def handle_cancel_result_filter_student(controller):
    def callback(x):
        controller.close_result_filter_window()
    return callback

def handle_cancel_confirm_delete_student(controller):
    def callback(x):
        controller.close_confirm_delete_window()
    return callback 

def handle_error_add_student(controller):
    def callback(x):
        controller.close_error_window()
    return callback